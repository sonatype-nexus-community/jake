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
import json
import os
from argparse import ArgumentParser
from decimal import Decimal
from pathlib import Path
from typing import cast, Iterable, List, Set

from cyclonedx.model import XsUri
from cyclonedx.model.bom import Bom
from cyclonedx.model.component import Component
from cyclonedx.model.impact_analysis import ImpactAnalysisAffectedStatus
from cyclonedx.model.vulnerability import BomTarget, BomTargetVersionRange, Vulnerability, VulnerabilityAdvisory, \
    VulnerabilityRating, VulnerabilityReference, VulnerabilityScoreSource, VulnerabilitySeverity, VulnerabilitySource
from cyclonedx.output import get_instance, OutputFormat, SchemaVersion, LATEST_SUPPORTED_SCHEMA_VERSION
from ossindex.model import OssIndexComponent
from ossindex.ossindex import OssIndex
# See https://github.com/package-url/packageurl-python/issues/65
from packageurl import PackageURL  # type: ignore
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress
from rich.table import Table
from rich.tree import Tree

from . import BaseCommand
from . import parser_selector


class OssCommand(BaseCommand):
    _console: Console

    def handle_args(self) -> int:
        self._console = Console()

        exit_code: int = 0
        input_source_msg = "your python environment" if self.arguments.sbom_input_type == "ENV" else "provided specs"

        with Progress() as progress:
            task_parser = progress.add_task(
                description=f"[yellow]Collecting packages in {input_source_msg}", start=True, total=10
            )
            task_query_ossi = progress.add_task(
                description="[yellow]Querying OSS Index for details on your packages", start=True, total=10
            )
            task_sanity_checking = progress.add_task(
                description="[cyan]Sanity checking...", start=True, total=10
            )

            parser = parser_selector.get_parser(
                self.arguments.sbom_input_type, self.arguments.sbom_input_source
            )
            total_packages_collected = len(parser.get_components())
            progress.update(
                task_parser, completed=10,
                description=f'🐍 [green]Collected {total_packages_collected} packages from {input_source_msg}'
            )

            oss_index_results: List[OssIndexComponent]
            oss = OssIndex()
            if self.arguments.oss_clear_cache:
                progress.update(task_query_ossi, completed=1, description='Clearing OSS Index local cache')
                oss.purge_local_cache()
                progress.update(task_query_ossi, completed=2, description='Cleared OSS Index local cache')

            progress.update(task_query_ossi, completed=3, description='Querying OSS Index for details on your packages')

            oss_index_results = oss.get_component_report(
                packages=list(map(lambda c: c.purl, filter(lambda c: c.purl, parser.get_components())))
            )

            if self.arguments.oss_whitelist_json_file:
                with open(self.arguments.oss_whitelist_json_file) as f:
                    json_data = json.load(f)
                whitelisted_entries = json_data.get("ignore", [])
                whitelisted_ids = {entry["id"] for entry in whitelisted_entries}
                if whitelisted_ids:
                    for oic in oss_index_results:
                        oic.vulnerabilities = {v for v in oic.vulnerabilities if v.id not in whitelisted_ids}

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
                if component.purl:
                    oss_index_component: OssIndexComponent = list(filter(
                        lambda oic_: oic_.get_package_url().to_string() == cast(PackageURL, component.purl).to_string(),
                        oss_index_results
                    )).pop()
                else:
                    continue

                if oss_index_component.vulnerabilities:
                    for oic_vulnerability in oss_index_component.vulnerabilities:

                        ratings: List[VulnerabilityRating] = []
                        if oic_vulnerability.cvss_score:
                            ratings.append(
                                VulnerabilityRating(
                                    source=VulnerabilitySource(
                                        name='OSS Index', url=XsUri(oic_vulnerability.reference)
                                    ),
                                    score=Decimal(
                                        oic_vulnerability.cvss_score
                                    ) if oic_vulnerability.cvss_score else None,
                                    severity=VulnerabilitySeverity.get_from_cvss_scores(
                                        (oic_vulnerability.cvss_score,)
                                    ) if oic_vulnerability.cvss_score else None,
                                    method=VulnerabilityScoreSource.get_from_vector(
                                        vector=oic_vulnerability.cvss_vector
                                    ) if oic_vulnerability.cvss_vector else None,
                                    vector=oic_vulnerability.cvss_vector
                                )
                            )

                        vulnerability: Vulnerability = Vulnerability(
                            bom_ref=oic_vulnerability.id,
                            id=oic_vulnerability.id,
                            source=VulnerabilitySource(
                                name='OSS Index', url=XsUri(oic_vulnerability.reference)
                            ),
                            cwes=[int(oic_vulnerability.cwe[4:])] if oic_vulnerability.cwe else None,
                            description=oic_vulnerability.title,
                            detail=oic_vulnerability.description,
                            ratings=ratings,
                            references=[
                                VulnerabilityReference(
                                    id=oic_vulnerability.display_name, source=VulnerabilitySource(
                                        name='OSS Index', url=XsUri(oic_vulnerability.reference)
                                    )
                                )
                            ]
                        )
                        if oic_vulnerability.external_references:
                            advisories: Set[VulnerabilityAdvisory] = set()
                            for ext_ref_url in oic_vulnerability.external_references:
                                advisories.add(VulnerabilityAdvisory(url=XsUri(uri=ext_ref_url)))
                            vulnerability.advisories = advisories

                        vulnerability.affects.add(
                            BomTarget(
                                ref=str(component.bom_ref),
                                versions=[
                                    BomTargetVersionRange(
                                        version=component.version, status=ImpactAnalysisAffectedStatus.AFFECTED
                                    )
                                ]
                            )
                        )

                        component.add_vulnerability(vulnerability=vulnerability)

                components.append(component)
                progress.update(task_munching_data, advance=1)

        print('')
        self._print_oss_index_report(components=components)

        if self.arguments.oss_output_file:
            cyclonedx_output = get_instance(
                bom=OssCommand._build_bom(components=components),
                output_format=OutputFormat[str(self.arguments.oss_output_format).upper()],
                schema_version=SchemaVersion['V{}'.format(
                    str(self.arguments.oss_schema_version).replace('.', '_')
                )])

            output_filename = os.path.realpath(self.arguments.oss_output_file)
            cyclonedx_output.output_to_file(filename=output_filename, allow_overwrite=True)
            print('')
            print('CycloneDX has been written to {}'.format(output_filename))

        # Update exit_code if warn only is not enabled and issues have been detected
        if not self.arguments.warn_only:
            for oic in oss_index_results:
                if oic.vulnerabilities:
                    exit_code = 1
                    break

        return exit_code

    def get_argument_parser_name(self) -> str:
        return 'ddt'

    def get_argument_parser_help(self) -> str:
        return 'perform a scan backed by OSS Index'

    def setup_argument_parser(self, arg_parser: ArgumentParser) -> None:
        parser_selector.add_parser_selector_arguments(arg_parser)
        arg_parser.add_argument('--clear-cache', help='Clears any local cached OSS Index data prior to execution',
                                action='store_true', dest='oss_clear_cache', default=False)

        arg_parser.add_argument('-o', '--output-file',
                                help='Specify a file to output the SBOM to. If not specified the '
                                     'report will be output to the console. '
                                     'STDOUT is not supported.',
                                metavar='PATH/TO/FILE', dest='oss_output_file', default=None)
        arg_parser.add_argument('--output-format', help='SBOM output format (default = xml)', choices={'json', 'xml'},
                                default='xml', dest='oss_output_format')
        arg_parser.add_argument('--schema-version',
                                help=f'CycloneDX schema version to use (default = '
                                     f'{LATEST_SUPPORTED_SCHEMA_VERSION.to_version()})',
                                choices={'1.4', '1.3', '1.2', '1.1', '1.0'},
                                default=f'{LATEST_SUPPORTED_SCHEMA_VERSION.to_version()}',
                                dest='oss_schema_version')
        arg_parser.add_argument('--whitelist', help='Set path to whitelist json file', type=Path,
                                dest='oss_whitelist_json_file')

    @staticmethod
    def _build_bom(components: Iterable[Component]) -> Bom:
        bom = Bom()
        bom.components = set(components)
        return bom

    def _print_oss_index_report(self, components: List[Component]) -> None:
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
            if rating.score and float(rating.score) > max_score:
                max_score = float(rating.score)
        return max_score

    @staticmethod
    def _get_max_cvss_score(component: Component) -> float:
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
{os.linesep.join([f'   -  [{severity_color}]{rating.score:.1f} {rating.severity.name if rating.severity else ""} - '
                  f'Vector: {rating.vector if rating.vector else "Unknown"}, '
                  f'CWEs: {",".join(list(map(lambda cwe: str(cwe), v.cwes))) if v.cwes else "None Recorded"}'
                  f'[bright_white]' for rating in v.ratings])}

References:
{os.linesep.join([f'  - {reference.source.name if reference.source and reference.source.name else ""} '
                  f'[Ref: {reference.id}]{os.linesep}'
                  f'    URL: {reference.source.url if reference.source and reference.source.url else "None"}'
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
    def _get_severity_for_cvss_score(cvss_score: float) -> str:
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
