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

import time
from argparse import ArgumentParser

from cyclonedx.model.bom import Bom
from cyclonedx.output import make_outputter
from cyclonedx.schema import OutputFormat, SchemaVersion
from rich.progress import Progress
from sonatype_iq_api_client import ApiClient, ApplicationsApi, Configuration, ThirdPartyAnalysisApi

from . import BaseCommand
from . import parser_selector


class IqCommand(BaseCommand):

    def handle_args(self) -> int:
        exit_code: int = 0
        input_source_msg = "your python environment" if self.arguments.sbom_input_type == "ENV" else "provided specs"

        with Progress() as progress:
            task_validate_iq = progress.add_task(
                description="[yellow]Checking out your Nexus IQ Server", start=True, total=10
            )
            task_parser = progress.add_task(
                description=f"[yellow]Collecting packages in {input_source_msg}", start=True, total=10
            )
            task_query_iq = progress.add_task(
                description="[yellow]Submitting to Nexus Lifecycle for Policy Evaluation", start=True, total=10
            )

            config = Configuration(
                host=self.arguments.iq_server_url,
                username=self.arguments.iq_username,
                password=self.arguments.iq_password
            )

            with ApiClient(config) as api_client:
                apps_api = ApplicationsApi(api_client)
                scan_api = ThirdPartyAnalysisApi(api_client)

                progress.update(
                    task_validate_iq, completed=10,
                    description=f"[green]IQ Server at {self.arguments.iq_server_url} is up and accessible"
                )

                # task_parser
                parser = parser_selector.get_parser(
                    self.arguments.sbom_input_type, self.arguments.sbom_input_source
                )
                total_packages_collected = len(parser.get_components())
                progress.update(
                    task_parser, completed=10,
                    description=f'[green]Collected {total_packages_collected} packages from {input_source_msg}'
                )

                # Look up internal application ID
                app_list = apps_api.get_applications(public_id=[self.arguments.iq_application_id])
                if not app_list.applications or len(app_list.applications) != 1:
                    raise ValueError(
                        'There were {} matching Applications found in IQ for {}'.format(
                            len(app_list.applications) if app_list.applications else 0,
                            self.arguments.iq_application_id
                        )
                    )
                internal_id = app_list.applications[0].id

                # Build BOM and serialise to XML
                bom = Bom(components=set(parser.get_components()))
                bom_xml = make_outputter(bom, OutputFormat.XML, SchemaVersion.V1_4).output_as_string()

                # Submit scan
                progress.start_task(task_query_iq)
                ticket = scan_api.scan_components(
                    internal_id, 'jake', self.arguments.iq_scan_stage, bom_xml
                )

                # Extract scan ID from the last path segment of status_url
                scan_id = ticket.status_url.rstrip('/').split('/')[-1]

                # Poll for results
                result = None
                while True:
                    result = scan_api.get_scan_status(internal_id, scan_id)
                    if result.is_error is not None:
                        break
                    time.sleep(10)

            if result.policy_action == 'Failure':
                progress.update(
                    task_query_iq, completed=10,
                    description='[red]Policy failures detected from Sonatype Nexus IQ.'
                )
                exit_code = 1
            elif result.policy_action == 'Warning':
                progress.update(
                    task_query_iq, completed=10,
                    description='[yellow]Policy warnings detected from Sonatype Nexus IQ.'
                )
            else:
                progress.update(
                    task_query_iq, completed=10,
                    description='[green]Sonatype Nexus IQ Policy Evaluation complete with no policy violations.'
                )

        print('')
        print('Your Sonatype Nexus IQ Lifecycle Report is available here:')
        print('  HTML: {}/{}'.format(self.arguments.iq_server_url, result.report_html_url))
        print('  PDF:  {}/{}'.format(self.arguments.iq_server_url, result.report_pdf_url))
        print('')

        return exit_code

    def get_argument_parser_name(self) -> str:
        return 'iq'

    def get_argument_parser_help(self) -> str:
        return 'perform a scan backed by Sonatype Nexus Lifecycle'

    def setup_argument_parser(self, arg_parser: ArgumentParser) -> None:
        parser_selector.add_parser_selector_arguments(arg_parser)
        arg_parser.add_argument('-s', '--server-url', help='Full http(s):// URL to your Nexus Lifecycle server',
                                metavar='https://localhost:8070', required=True, dest='iq_server_url')

        arg_parser.add_argument('-i', '--application-id', help='Public Application ID in Nexus Lifecycle',
                                metavar='APP_ID', required=True, dest='iq_application_id')

        arg_parser.add_argument('-u', '--username', help='Username for authentication to Nexus Lifecycle',
                                metavar='USER_ID', required=True, dest='iq_username')

        arg_parser.add_argument('-p', '--password', help='Password for authentication to Nexus Lifecycle',
                                metavar='PASSWORD', required=True, dest='iq_password')

        arg_parser.add_argument('-st', '--stage', help='The stage for the report',
                                metavar='STAGE', required=False, dest='iq_scan_stage', default='source')
