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
from typing import List

from cyclonedx.model.bom import Bom
from cyclonedx.model.component import Component
from cyclonedx.model.vulnerability import Vulnerability as CycloneDxVulnerability, VulnerabilityRating, \
    VulnerabilitySourceType
from cyclonedx.output import get_instance, OutputFormat, SchemaVersion
from cyclonedx.parser.environment import EnvironmentParser
from ossindex.model import OssIndexComponent, Vulnerability
from ossindex.ossindex import OssIndex
from packageurl import PackageURL
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
                description="[yellow]Collecting packages in your Python Environment", start=False, total=10
            )
            task_query_ossi = progress.add_task(
                description="[yellow]Querying OSS Index for details on your packages", start=False, total=10
            )
            task_sanity_checking = progress.add_task(
                description="[cyan]Sanity checking...", start=False, total=10
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
                packages=list(map(lambda c: c.to_package_url(), parser.get_components()))
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

        print('')
        self._print_oss_index_report(oss_index_results=oss_index_results)

        if self._arguments.oss_output_file:
            cyclonedx_output = get_instance(
                bom=self._build_bom(oss_index_results=oss_index_results),
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
                            choices={'1.3', '1.2', '1.1', '1.0'}, default='1.3',
                            dest='oss_schema_version')

    def _build_bom(self, oss_index_results: List[OssIndexComponent]) -> Bom:
        bom = Bom()
        oic: OssIndexComponent = None
        for oic in oss_index_results:
            purl: PackageURL = oic.get_package_url()
            component: Component = Component(name=purl.name, version=purl.version, qualifiers=purl.qualifiers)
            if oic.has_known_vulnerabilities():
                for oss_vuln in oic.get_vulnerabilities():
                    component.add_vulnerability(CycloneDxVulnerability(
                        id=oss_vuln.get_display_name(), source_name='OSSINDEX',
                        source_url=oss_vuln.get_oss_index_reference_url(), ratings=[
                            VulnerabilityRating(
                                score_base=oss_vuln.get_cvss_score(), vector=oss_vuln.get_cvss_vector(),
                                method=VulnerabilitySourceType.get_from_vector(vector=oss_vuln.get_cvss_vector())
                            )
                        ],
                        description=oss_vuln.get_description(),
                        cwes=[oss_vuln.get_cwe().replace('CWE-')] if oss_vuln.get_cwe() else [],
                        advisories=oss_vuln.get_external_reference_urls()
                    ))
            bom.add_component(component=component)

        return bom

    def _print_oss_index_report(self, oss_index_results: List[OssIndexComponent]):
        total_vulnerabilities = 0
        total_packages = len(oss_index_results)

        oic: OssIndexComponent
        v: Vulnerability
        i: int = 1
        for oic in oss_index_results:
            if oic.has_known_vulnerabilities():
                self._console.print(
                    f"[{i}/{total_packages}] - {oic.get_coordinates()} [VULNERABLE]",
                    style=self._get_color_for_cvss_score(cvss_score=oic.get_max_cvss_score())
                )

                total_vulnerabilities += len(oic.get_vulnerabilities())
                if oic.get_vulnerabilities():
                    tree = Tree(f'Vulnerability Details for [bright_white]{oic.get_coordinates()}[white]')
                    for v in oic.get_vulnerabilities():
                        self._print_vulnerability(tree=tree, v=v)
                    self._console.print(tree)
                else:
                    self._console.print(
                        f"[{i}/{total_packages}] - {oic.get_coordinates()}",
                        style=self._get_color_for_cvss_score(cvss_score=oic.get_max_cvss_score())
                    )

            i += 1

        self._console.print('')

        table = Table(title='Summary')
        table.add_column("Audited Dependencies", justify="left", no_wrap=True)
        table.add_column("Vulnerabilities Found", justify="left", no_wrap=True)
        table.add_row('{}'.format(len(oss_index_results)), f'{total_vulnerabilities}')

        self._console.print(table)

    @staticmethod
    def _print_vulnerability(tree: Tree, v: Vulnerability) -> None:
        b = tree.add(
            f':warning: [bright_red] ID: {v.get_id()}'
        )

        severity_color = OssCommand._get_color_for_cvss_score(v.get_cvss_score())

        content = f"""
[bright_white]{v.get_description()}

Details:
  - CVSS Score: {v.get_cvss_score()} - [{severity_color}]{OssCommand._get_severity_for_cvss_score(v.get_cvss_score())}
  [bright_white]- CVSS Vector: {v.get_cvss_vector() if v.get_cvss_vector() else 'Unknown'}
  - CWE: {v.get_cwe() if v.get_cwe() else 'Unknown'}

References:
  - {v.get_oss_index_reference_url()}
{os.linesep.join([f'  - {url}' for url in v.get_external_reference_urls()])}
        """

        b.add(Panel(content, title=f'[bright_white]{v.get_cve()}', title_align="left"))

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
