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

"""iq.py handles requests to IQ Server"""
# pylint: disable=too-many-instance-attributes
import json
import logging

from json import JSONDecodeError

import requests
import polling

from ..config.iq_config import IQConfig

DEFAULT_HEADERS = {
    'User-Agent': 'jake'}

LOG = logging.getLogger('jake')

class IQ():
  """IQ handles requests to IQ Server"""
  def __init__(self, args):
    self._iq_url = args.get('host')
    self._user = args.get('user')
    self._password = args.get('password')
    self._public_application_id = args.get('application')
    self._stage = args.get('stage')
    self._insecure = args.get('insecure')
    self._headers = DEFAULT_HEADERS
    self._report_url = ''
    self._policy_action = None
    self._request = requests.Session()
    self._internal_id = ''

    if self._insecure:
      self._request.verify = False

    config = IQConfig()
    if config.check_if_config_exists('.iq-server-config') is False:
      LOG.debug("No IQ server config supplied, using defaults or taking from command-line.")
      if self._user is None:
        self._user = 'admin'
      if self._password is None:
        self._password = 'admin123'
      if self._iq_url is None:
        self._iq_url = 'http://localhost:8070'
    else:
      LOG.debug("Found iq server config.  Using those unless overwritten by command line params.")
      results = config.get_config_from_file(".iq-server-config")
      if self._user is None:
        self._user = results['Username']
      if self._password is None:
        self._password = results['Token']
      if self._iq_url is None:
        self._iq_url = results['Server']

    self._request.auth = requests.auth.HTTPBasicAuth(self._user, self._password)

  def get_policy_action(self):
    """gets policy action from IQ Server result"""
    return self._policy_action

  def get_report_url(self):
    """gets report url from IQ Server result"""
    return self._report_url

  def get_public_application_id(self) -> (str):
    """gets public application id to use for IQ Server request"""
    return self._public_application_id

  def get_internal_id(self) -> (str):
    """gets internal application id from IQ Server using the public
    application id"""
    response = self._request.get(
        '{0}/api/v2/applications?publicId={1}'.format(
            self._iq_url,
            self._public_application_id),
        headers=self._headers)
    if response.ok:
      res = json.loads(response.text)
      if not res['applications']:
        raise ValueError(
            "\nThe public application id \'"
            + self._public_application_id
            + "\' does not exist or is not accessible by the user.")
      LOG.debug(res['applications'][0]['id'])
      return res['applications'][0]['id']
    raise ValueError('\n' + response.text + '\nSet your config with \'jake config iq\'')

  def submit_sbom(self, sbom: str) -> (str):
    """submits sbom (in str form) to IQ server, valid sbom should get
    202 response. On valid response, sets status url for later polling"""
    self._internal_id = self.get_internal_id()

    LOG.debug(sbom)
    headers = self._headers
    headers['Content-Type'] = 'application/xml'
    response = self._request.post(
        '{0}/api/v2/scan/applications/{1}/sources/jake?stageId={2}'.format(
            self._iq_url,
            self._internal_id,
            self._stage),
        data=sbom,
        headers=headers)
    if response.ok:
      res = json.loads(response.text)
      LOG.debug(res['statusUrl'])
      return res['statusUrl']
    raise ValueError(response.text)

  def poll_report(self, status_url: str):
    """polls status url once a second until it gets a 200 response
    , and times out after one minute"""
    polling.poll(
        lambda: self._request.get(
            '{0}/{1}'.format(self._iq_url, status_url)).text,
        check_success=self.__handle_response,
        step=1,
        timeout=60)

  def __handle_response(self, response: str) -> (bool):
    try:
      res = json.loads(response)
      LOG.debug(res)
      self._policy_action = res['policyAction']
      LOG.debug("Policy Action parsed")
      self._report_url = res['reportHtmlUrl']
      return True
    except JSONDecodeError as json_decode_error:
      LOG.debug(json_decode_error.msg)
      return False
