# encoding: utf-8

#
# Copyright 2019-Present Sonatype Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import argparse
import os
from decimal import Decimal
from typing import List, Optional

from cyclonedx.model import XsUri
from cyclonedx.model.bom import Bom
from cyclonedx.model.component import Component
from cyclonedx.model.impact_analysis import ImpactAnalysisAffectedStatus
from cyclonedx.model.vulnerability import BomTarget, BomTargetVersionRange, Vulnerability, VulnerabilityAdvisory, \
    VulnerabilityRating, VulnerabilityReference, VulnerabilityScoreSource, VulnerabilitySeverity, VulnerabilitySource
from cyclonedx.output import get_instance, OutputFormat, SchemaVersion
from cyclonedx_py.parser.environment import EnvironmentParser
from ossindex.model import OssIndexComponent
from ossindex.ossindex import OssIndex
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress
from rich.table import Table
from rich.tree import Tree

from . import BaseCommand


class OssCommand(BaseCommand):
    _console: Console

    def handle_args(self) -> int:
        self._console = Console()

        exit_code: int = 0

        with Progress() as progress:
            task_parser = progress.add_task(
                description="[yellow]Collecting packages in your Python Environment", start=True, total=10
            )
            task_query_ossi = progress.add_task(
                description="[yellow]Querying OSS Index for details on your packages", start=True, total=10
            )
            task_sanity_checking = progress.add_task(
                description="[cyan]Sanity checking...", start=True, total=10
            )

            parser = EnvironmentParser()
            total_packages_collected = len(parser.get_components())
            progress.update(
                task_parser, completed=10,
                description=f'🐍 [green]Collected {total_packages_collected} packages from your environment'
            )

            oss_index_results: List[OssIndexComponent]
            oss = OssIndex()
            if self._arguments.oss_clear_cache:
                progress.update(task_query_ossi, completed=1, description='Clearing OSS Index local cache')
                oss.purge_local_cache()
                progress.update(task_query_ossi, completed=2, description='Cleared OSS Index local cache')

            progress.update(task_query_ossi, completed=3, description='Querying OSS Index for details on your packages')

            oss_index_results = oss.get_component_report(
                packages=list(map(lambda c: c.purl if c.purl else None, parser.get_components()))
            )
            progress.update(
                task_query_ossi, completed=10,
                description='🐍 [green]Successfully queried OSS Index for package and vulnerability info'
            )

            progress.update(task_sanity_checking, completed=1)
            if len(parser.get_components()) > len(oss_index_results):
                progress.update(
                    task_sanity_checking, completed=10,
                    description="🐍 [red]Some components not identified by OSS Index - perhaps these are InnerSource?"
                )
            else:
                progress.update(
                    task_sanity_checking, completed=10,
                    description="🐍 [green]Sane number of results from OSS Index"
                )

            task_munching_data = progress.add_task(
                description="🐍 [green]Munching & crunching data...", start=True, total=len(parser.get_components())
            )

            components: List[Component] = []
            for component in parser.get_components():
                oss_index_component: OssIndexComponent = list(filter(
                    lambda oic: oic.get_package_url().to_string() == component.purl.to_string(), oss_index_results
                )).pop()

                if oss_index_component.has_known_vulnerabilities():
                    for oic_vulnerability in oss_index_component.get_vulnerabilities():

                        ratings: List[VulnerabilityRating] = []
                        if oic_vulnerability.get_cvss_score():
                            ratings.append(
                                VulnerabilityRating(
                                    source=VulnerabilitySource(
                                        name='OSS Index', url=XsUri(oic_vulnerability.get_oss_index_reference_url())
                                    ),
                                    score=Decimal(
                                        oic_vulnerability.get_cvss_score()
                                    ) if oic_vulnerability.get_cvss_score() else None,
                                    severity=VulnerabilitySeverity.get_from_cvss_scores(
                                        (oic_vulnerability.get_cvss_score(),)
                                    ) if oic_vulnerability.get_cvss_score() else None,
                                    method=VulnerabilityScoreSource.get_from_vector(
                                        vector=oic_vulnerability.get_cvss_vector()
                                    ) if oic_vulnerability.get_cvss_vector() else None,
                                    vector=oic_vulnerability.get_cvss_vector()
                                )
                            )

                        vulnerability: Vulnerability = Vulnerability(
                            bom_ref=str(oic_vulnerability.get_id()) if oic_vulnerability.get_id() else None,
                            id=str(oic_vulnerability.get_id()),
                            source=VulnerabilitySource(
                                name='OSS Index', url=XsUri(oic_vulnerability.get_oss_index_reference_url())
                            ),
                            cwes=[int(oic_vulnerability.get_cwe()[4:])] if oic_vulnerability.get_cwe() else None,
                            description=oic_vulnerability.get_title(),
                            detail=oic_vulnerability.get_description(),
                            ratings=ratings,
                            references=[
                                VulnerabilityReference(
                                    id=str(oic_vulnerability.get_cve()), source=VulnerabilitySource(
                                        name='OSS Index', url=XsUri(oic_vulnerability.get_oss_index_reference_url())
                                    )
                                )
                            ]
                        )
                        if oic_vulnerability.get_external_reference_urls():
                            advisories: List[VulnerabilityAdvisory] = []
                            for ext_ref_url in oic_vulnerability.get_external_reference_urls():
                                advisories.append(
                                    VulnerabilityAdvisory(url=XsUri(uri=ext_ref_url))
                                )
                            vulnerability.advisories = advisories

                        vulnerability.affects = [
                            BomTarget(
                                ref=component.bom_ref,
                                versions=[
                                    BomTargetVersionRange(
                                        version=component.version, status=ImpactAnalysisAffectedStatus.AFFECTED
                                    )
                                ]
                            )
                        ]

                        component.add_vulnerability(vulnerability=vulnerability)

                components.append(component)
                progress.update(task_munching_data, advance=1)

        print('')
        self._print_oss_index_report(components=components)

        if self._arguments.oss_output_file:
            cyclonedx_output = get_instance(
                bom=OssCommand._build_bom(components=components),
                output_format=OutputFormat[str(self._arguments.oss_output_format).upper()],
                schema_version=SchemaVersion['V{}'.format(
                    str(self._arguments.oss_schema_version).replace('.', '_')
                )])

            output_filename = os.path.realpath(self._arguments.oss_output_file)
            cyclonedx_output.output_to_file(filename=output_filename, allow_overwrite=True)
            print('')
            print('CycloneDX has been written to {}'.format(output_filename))

        # Update exit_code if warn only is not enabled and issues have been detected
        if not self._arguments.warn_only:
            for oic in oss_index_results:
                if oic.has_known_vulnerabilities():
                    exit_code = 1
                    break

        return exit_code

    def setup_argument_parser(self, subparsers: argparse._SubParsersAction):
        parser = subparsers.add_parser('ddt', help='perform a scan backed by OSS Index')

        parser.add_argument('--clear-cache', help='Clears any local cached OSS Index data prior to execution',
                            action='store_true', dest='oss_clear_cache', default=False)

        parser.add_argument('-o', '--output-file', help='Specify a file to output the SBOM to. If not specified the '
                                                        'report will be output to the console. '
                                                        'STDOUT is not supported.',
                            metavar='PATH/TO/FILE', dest='oss_output_file', default=None)
        parser.add_argument('--output-format', help='SBOM output format (default = xml)', choices={'json', 'xml'},
                            default='xml', dest='oss_output_format')
        parser.add_argument('--schema-version', help='CycloneDX schema version to use (default = 1.3)',
                            choices={'1.4', '1.3', '1.2', '1.1', '1.0'}, default='1.3',
                            dest='oss_schema_version')

    @staticmethod
    def _build_bom(components: List[Component]) -> Bom:
        bom = Bom()
        bom.components = components
        return bom

    def _print_oss_index_report(self, components: List[Component]):
        total_vulnerabilities = 0
        total_packages = len(components)

        component: Component
        i: int = 1
        for component in components:
            if component.has_vulnerabilities():
                self._console.print(
                    f"[{i}/{total_packages}] - {component.name}@{component.version} [VULNERABLE]",
                    style=OssCommand._get_color_for_cvss_score(
                        cvss_score=OssCommand._get_max_cvss_score(component=component)
                    )
                )

                total_vulnerabilities += len(component.get_vulnerabilities())
                if component.get_vulnerabilities():
                    tree = Tree(f'Vulnerability Details for [bright_white]{component.name}@{component.version}[white]')
                    for v in component.get_vulnerabilities():
                        OssCommand._print_vulnerability(tree=tree, v=v)
                    self._console.print(tree)
                else:
                    self._console.print(
                        f"[{i}/{total_packages}] - {component.name}@{component.version}",
                        style=OssCommand._get_color_for_cvss_score(
                            cvss_score=OssCommand._get_max_cvss_score(component=component)
                        )
                    )

            i += 1

        self._console.print('')

        table = Table(title='Summary')
        table.add_column("Audited Dependencies", justify="left", no_wrap=True)
        table.add_column("Vulnerabilities Found", justify="left", no_wrap=True)
        table.add_row('{}'.format(len(components)), f'{total_vulnerabilities}')

        self._console.print(table)

    @staticmethod
    def _get_max_cvss_score_for_vulnerability(vulnerability: Vulnerability) -> float:
        max_score: float = 0.0
        for rating in vulnerability.ratings:
            if float(rating.score) > max_score:
                max_score = float(rating.score)
        return max_score

    @staticmethod
    def _get_max_cvss_score(component: Component) -> Optional[float]:
        max_cvss_score: float = 0.0
        for v in component.get_vulnerabilities():
            max_cvss_score = OssCommand._get_max_cvss_score_for_vulnerability(vulnerability=v)
        return max_cvss_score

    @staticmethod
    def _print_vulnerability(tree: Tree, v: Vulnerability) -> None:
        b = tree.add(
            f':warning: [bright_red] ID: {v.id}'
        )

        severity_color = OssCommand._get_color_for_cvss_score(
            OssCommand._get_max_cvss_score_for_vulnerability(vulnerability=v)
        )

        content = f"""
[bright_white]{v.description}
{v.detail}

Ratings:
{os.linesep.join([f'   -  [{severity_color}]{rating.score:.1f} {rating.severity.name} - '
                  f'Vector: {rating.vector if rating.vector else "Unknown"}, '
                  f'CWEs: {",".join(list(map(lambda cwe: str(cwe), v.cwes))) if v.cwes else "None Recorded"}'
                  f'[bright_white]' for rating in v.ratings])}

References:
{os.linesep.join([f'  - {reference.source.name if reference.source.name else ""} [Ref: {reference.id}]{os.linesep}'
                  f'    URL: {reference.source.url if reference.source.url else "None"}'
                  for reference in v.references])}
        """

        b.add(Panel(content, title=f'[bright_white]{v.id}', title_align="left"))

    @staticmethod
    def _get_color_for_cvss_score(cvss_score: float = 0.0) -> str:
        if cvss_score >= 9.0:
            return 'bright_red'
        elif cvss_score >= 7.0:
            return 'bright_yellow'
        elif cvss_score >= 4.0:
            return 'yellow3'
        elif cvss_score > 0.0:
            return 'bright_cyan'
        else:
            return 'bright_green'

    @staticmethod
    def _get_severity_for_cvss_score(cvss_score: float = None) -> str:
        if cvss_score >= 9.0:
            return 'Critical'
        elif cvss_score >= 7.0:
            return 'High'
        elif cvss_score >= 4.0:
            return 'Medium'
        elif cvss_score > 0.0:
            return 'Low'
        else:
            return 'None'
