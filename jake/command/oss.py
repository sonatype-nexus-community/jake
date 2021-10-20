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
from textwrap import wrap
from typing import List

from colorama import Fore
from cyclonedx.model.bom import Bom
from cyclonedx.model.component import Component
from cyclonedx.model.vulnerability import Vulnerability as CycloneDxVulnerability, VulnerabilityRating, \
    VulnerabilitySourceType
from cyclonedx.output import get_instance, OutputFormat, SchemaVersion
from cyclonedx.parser.environment import EnvironmentParser
from ossindex.model import OssIndexComponent, Vulnerability
from ossindex.ossindex import OssIndex
from packageurl import PackageURL
from terminaltables import DoubleTable
from yaspin import yaspin

from . import BaseCommand


class OssCommand(BaseCommand):

    def handle_args(self) -> int:
        exit_code: int = 0

        with yaspin(text='Collecting packages in your Python Environment', color='yellow', timer=True) as spinner:
            parser = EnvironmentParser()
            spinner.text = 'Collected {} packages from your environment'.format(len(parser.get_components()))
            spinner.ok('🐍')

        oss_index_results: List[OssIndexComponent] = None
        with yaspin(text='Querying OSS Index for details on your packages', color='yellow', timer=True) as spinner:
            oss = OssIndex()
            if self._arguments.oss_clear_cache:
                spinner.text = 'Clearing OSS Index local cache'
                oss.purge_local_cache()
                spinner.text = 'Querying OSS Index for details on your packages'

            oss_index_results = oss.get_component_report(
                packages=list(map(lambda c: c.to_package_url(), parser.get_components())))
            spinner.text = 'Successfully queried OSS Index for package and vulnerability info'
            spinner.ok('🐍')

        with yaspin(text='Sanity checking...', color='yellow') as spinner:
            if len(parser.get_components()) > len(oss_index_results):
                spinner.text = 'Some components not identified by OSS Index - perhaps these are InnerSource?'
                spinner.ok('🐍 !!! ')
            else:
                spinner.text = 'Sane number of results from OSS Index'
                spinner.ok('🐍')

        print('')
        self._print_oss_index_report(oss_index_results=oss_index_results)

        if self._arguments.oss_output_file:
            cyclonedx_output = get_instance(
                bom=self._build_bom(oss_index_results=oss_index_results),
                output_format=OutputFormat[str(self._arguments.oss_output_format).upper()],
                schema_version=SchemaVersion['V{}'.format(
                    str(self._arguments.oss_schema_version).replace('.', '_')
                )]
            )
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

        oic: OssIndexComponent = None
        v: Vulnerability = None
        i: int = 1
        for oic in oss_index_results:
            if oic.has_known_vulnerabilities():
                print(
                    f"{self._get_color_for_cvss_score(cvss_score=oic.get_max_cvss_score())}[{i}/{total_packages}] - "
                    f"{oic.get_coordinates()} [VULNERABLE]{Fore.RESET}"
                )
                print(f"{len(oic.get_vulnerabilities())} known vulnerabilities for this package version")
                total_vulnerabilities += len(oic.get_vulnerabilities())
                for v in oic.get_vulnerabilities():
                    OssCommand._print_vulnerability_as_table(v=v)
                else:
                    print(f"{self._get_color_for_cvss_score(cvss_score=oic.get_max_cvss_score())}[{i}/{total_packages}]"
                          f" - {oic.get_coordinates()}{Fore.RESET}")

            i += 1

        print('')
        table_data = [
            ["Audited Dependencies", len(oss_index_results)],
            ["Vulnerablities Found", total_vulnerabilities],

        ]

        table_instance = DoubleTable(table_data, "Summary")
        print(table_instance.table)

    @staticmethod
    def _print_vulnerability_as_table(v: Vulnerability) -> None:
        table_data = [
            ["ID", v.get_id()],
            ["Title", v.get_title()],
            ["Description", '\n'.join(wrap(v.get_description(), 100))],
            ["CVSS Score", f"{v.get_cvss_score()} - {OssCommand._get_severity_for_cvss_score(v.get_cvss_score())}"],
        ]
        if v.get_cvss_vector():
            table_data.append(
                ["CVSS Vector", v.get_cvss_vector()]
            )

        table_data.extend(
            [
                ["CWE", v.get_cwe()],
                ["Reference", v.get_oss_index_reference_url()]
            ]
        )
        table_instance = DoubleTable(table_data)
        table_instance.inner_heading_row_border = False
        table_instance.inner_row_border = True
        print(OssCommand._get_color_for_cvss_score(cvss_score=v.get_cvss_score()) + table_instance.table + Fore.RESET)

    @staticmethod
    def _get_color_for_cvss_score(cvss_score: float = 0.0):
        if cvss_score >= 9.0:
            return Fore.RED
        elif cvss_score >= 7.0:
            return Fore.YELLOW
        elif cvss_score >= 4.0:
            return Fore.LIGHTYELLOW_EX
        elif cvss_score > 0.0:
            return Fore.CYAN
        else:
            return Fore.GREEN

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
