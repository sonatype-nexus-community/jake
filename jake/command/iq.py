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
import logging
from typing import Union
from urllib.parse import urlparse

import requests
from cyclonedx.model.bom import Bom
from cyclonedx.output import get_instance
from cyclonedx_py.parser.environment import EnvironmentParser
from polling2 import poll_decorator
from requests.auth import HTTPBasicAuth
from rich.progress import Progress

from . import BaseCommand, _jake_version


class IqCommand(BaseCommand):
    class IqServerApi:
        """
        Internal Nexus Lifecycle API class

        @todo In the future this and other API accessor classes may be moved to their won PyPi package to enable
                wider reuse.
        """

        _logger: logging.Logger = logging.getLogger('jake.iq')

        _server_url: str
        _username: str
        _password: str
        _auth: HTTPBasicAuth

        _default_headers = {
            'User-Agent': 'jake/{}'.format(_jake_version)
        }

        _max_wait_in_seconds: int = 300
        _check_interval_seconds: int = 10

        def __init__(self, server_url: str, username: str, password: str):
            self._server_url = urlparse(server_url).geturl()
            self._username = username
            self._password = password

            if self._validate_server():
                self._auth = HTTPBasicAuth(username, password)
            else:
                self._logger.error(
                    'IQ server at {} does not appear accessible or in a ready-state to receive requests'.format(
                        self._server_url
                    )
                )

        def scan_application_with_bom(self, bom: Bom, iq_public_application_id: str, iq_scan_stage: str):
            """
            This method is intentionally blocking.

            We submit a CycloneDX BOM to Nexus IQ for evaluation and then continuously poll IQ to determine
            when the results are available. Once available, we grab the results and then this method will return.

            """
            iq_bom_submit_response = self._submit_bom(
                bom=bom,
                iq_internal_application_id=self._get_internal_application_id_from_public_application_id(
                    iq_public_application_id=iq_public_application_id
                ),
                iq_scan_stage=iq_scan_stage
            )

            iq_status_url = iq_bom_submit_response['statusUrl']
            self._logger.debug('Status URL to check is {}'.format(iq_status_url))
            self._logger.debug('Starting to poll IQ for results')
            iq_report_response = self._get_scan_report_results(status_uri=iq_status_url)
            self._logger.debug('Polling for IQ results has stopped')
            return iq_report_response

        def _get_internal_application_id_from_public_application_id(self, iq_public_application_id: str) -> str:
            """
            Attempts to obtain the internal ID of the Application from Nexus IQ

            """
            iq_response = self.__make_request(
                uri='/api/v2/applications?publicId={}'.format(iq_public_application_id)
            )

            if 'applications' not in iq_response.keys():
                raise ValueError('Response from IQ is missing the \'applications\' key. Cannot parse')

            if len(iq_response['applications']) == 1:
                return iq_response['applications'][0]['id']
            else:
                message = 'There were {} matching Applications found in IQ for {}'.format(
                    len(iq_response['applications']), iq_public_application_id
                )
                self._logger.warning(message)
                raise ValueError(message)

        @poll_decorator(step=10, timeout=300, log_error=logging.DEBUG)
        def _get_scan_report_results(self, status_uri: str):
            try:
                response = self.__make_request(
                    uri='/{}'.format(status_uri)
                )
                if 'isError' in response.keys() and not response['isError']:
                    return response
                else:
                    return False
            except ValueError:
                return False

        def _submit_bom(self, bom: Bom, iq_internal_application_id: str, iq_scan_stage: str):
            self._logger.debug(
                'Submitting BOM to IQ for Application {} at stage {}'.format(iq_internal_application_id, iq_scan_stage)
            )
            return self.__make_request(
                uri='/api/v2/scan/applications/{}/sources/jake?stageId={}'.format(
                    iq_internal_application_id, iq_scan_stage
                ),
                method='POST',
                body_data=get_instance(bom=bom).output_as_string(),
                additional_headers={'Content-Type': 'application/xml'}
            )

        def _validate_server(self) -> bool:
            response = requests.get(url='{}/ping'.format(self._server_url), timeout=5)
            if response.status_code == 200 and response.text.strip() == 'pong':
                return True
            else:
                self._logger.error('IQ Server at {} is not available: {} - {}'.format(
                    self._server_url, response.status_code, response.text
                ))
                return False

        def __make_request(self, uri: str, body_data: object = None, additional_headers=None,
                           method: str = 'GET'):
            if additional_headers is None:
                additional_headers = {}
            self._logger.debug('Beginning request to IQ {}'.format(uri))
            response = requests.request(
                method=method,
                url='{}{}'.format(self._server_url, uri),
                data=(body_data.encode('UTF-8') if body_data else None),
                auth=self._auth,
                headers={**self._default_headers, **additional_headers}
            )

            if response.ok:
                self._logger.debug('   OK response {}'.format(response.status_code))
                # We always expect JSON response from IQ at this time
                return response.json()
            else:
                raise ValueError(response.text)

    _iq_server: Union[IqServerApi, None] = None

    def __init__(self):
        super().__init__()
        self._iq_server = None

    def handle_args(self) -> int:
        exit_code: int = 0

        with Progress() as progress:
            task_validate_iq = progress.add_task(
                description="[yellow]Checking out your Nexus IQ Server", start=True, total=10
            )
            task_parser = progress.add_task(
                description="[yellow]Collecting packages in your Python Environment", start=True, total=10
            )
            task_query_iq = progress.add_task(
                description="[yellow]Submitting to Nexus Lifecycle for Policy Evaluation", start=True, total=10
            )

            # task_validate_iq
            self._iq_server = self.IqServerApi(
                server_url=self._arguments.iq_server_url,
                username=self._arguments.iq_username,
                password=self._arguments.iq_password
            )
            progress.update(
                task_validate_iq, completed=10,
                description=f"🐍 [green]IQ Server at {self._arguments.iq_server_url} is up and accessible"
            )

            # task_parser
            parser = EnvironmentParser()
            total_packages_collected = len(parser.get_components())
            progress.update(
                task_parser, completed=10,
                description=f'🐍 [green]Collected {total_packages_collected} packages from your environment'
            )

            # task_query_iq
            progress.start_task(task_query_iq)
            iq_response = self._iq_server.scan_application_with_bom(
                bom=Bom.from_parser(parser=parser),
                iq_public_application_id=self._arguments.iq_application_id,
                iq_scan_stage=self._arguments.iq_scan_stage
            )

            if iq_response['policyAction'] == 'Failure':
                progress.update(
                    task_query_iq, completed=10,
                    description='💥 [red]Snakes on the plane! There are policy failures from Sonatype Nexus IQ.'
                )
                exit_code = 1
            elif iq_response['policyAction'] == 'Warning':
                progress.update(
                    task_query_iq, completed=10,
                    description='🧨 [orange]Something slithers around your ankle! '
                                'There are policy warnings from Sonatype Nexus IQ.'
                )
            else:
                progress.update(
                    task_query_iq, completed=10,
                    description='🐍 [green]Sonatype Nexus IQ Policy Evaluation complete with ZERO snakes.'
                )

        print('')
        print('Your Sonatype Nexus IQ Lifecycle Report is available here:')
        print('  HTML: {}/{}'.format(self._arguments.iq_server_url, iq_response['reportHtmlUrl']))
        print('  PDF:  {}/{}'.format(self._arguments.iq_server_url, iq_response['reportPdfUrl']))
        print('')

        return exit_code

    def setup_argument_parser(self, subparsers: argparse._SubParsersAction):
        parser: argparse.ArgumentParser = subparsers.add_parser('iq', help='perform a scan backed by Nexus Lifecycle')

        parser.add_argument('-s', '--server-url', help='Full http(s):// URL to your Nexus Lifecycle server',
                            metavar='https://localhost:8070', required=True, dest='iq_server_url')

        parser.add_argument('-i', '--application-id', help='Public Application ID in Nexus Lifecycle',
                            metavar='APP_ID', required=True, dest='iq_application_id')

        parser.add_argument('-u', '--username', help='Username for authentication to Nexus Lifecycle',
                            metavar='USER_ID', required=True, dest='iq_username')

        parser.add_argument('-p', '--password', help='Password for authentication to Nexus Lifecycle',
                            metavar='PASSWORD', required=True, dest='iq_password')

        parser.add_argument('-t', '--stage', help='The stage for the report',
                            metavar='STAGE', required=False, dest='iq_scan_stage', default='source')
