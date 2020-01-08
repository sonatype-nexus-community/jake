"""iq.py handles requests to IQ Server"""
# Copyright 2019 Sonatype Inc.
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
import json
import logging

from json import JSONDecodeError

import requests
import polling

from jake.config.iq_config import IQConfig

DEFAULT_HEADERS = {
    'User-Agent': 'jake'}

LOG = logging.getLogger('jake')

class IQ():
  """IQ handles requests to IQ Server"""
  def __init__(self, public_application_id, iq_server_base_url='http://localhost:8070/'):
    self._iq_server_base_url = iq_server_base_url.rstrip('/')
    self._public_application_id = public_application_id
    self._headers = DEFAULT_HEADERS
    self._report_url = ''
    self._policy_action = None
    config = IQConfig()
    results = config.get_config_from_file(".iq-server-config")

    self._user = results['Username']
    self._password = results['Token']
    self._iq_server_base_url = results['Server']

  def get_url(self):
    """gets url to use for IQ Server request"""
    return self._iq_server_base_url

  def get_policy_action(self):
    """gets policy action from IQ Server result"""
    return self._policy_action

  def get_report_url(self):
    """gets report url from IQ Server result"""
    return self._report_url

  def get_headers(self):
    """gets headers to use for IQ Server request"""
    return self._headers

  def get_public_application_id(self):
    """gets public application id to use for IQ Server request"""
    return self._public_application_id

  def get_internal_application_id_from_iq_server(self):
    """gets internal application id from IQ Server using the public
    application id"""
    response = requests.get(
        '{0}/api/v2/applications?publicId={1}'.format(
            self.get_url(),
            self.get_public_application_id()),
        self.get_headers(),
        auth=(self._user, self._password))
    if response.ok:
      res = json.loads(response.text)
      LOG.debug(res['applications'][0]['id'])
      return res['applications'][0]['id']
    raise ValueError(response.text)

  def submit_sbom_to_third_party_api(self, sbom: str, internal_id: str):
    """submits sbom (in str form) to IQ server, valid sbom should get
    202 response. On valid response, sets status url for later polling"""
    LOG.debug(sbom)
    headers = self.get_headers()
    headers['Content-Type'] = 'application/xml'
    response = requests.post(
        '{0}/api/v2/scan/applications/{1}/sources/jake'.format(
            self.get_url(),
            internal_id),
        data=sbom,
        headers=headers,
        auth=(self._user, self._password))
    if response.ok:
      res = json.loads(response.text)
      LOG.debug(res['statusUrl'])
      return res['statusUrl']
    raise ValueError(response.text)

  def poll_for_results(self, status_url: str):
    """polls status url once a second until it gets a 200 response
    , and times out after one minute"""
    polling.poll(
        lambda: requests.get(
            '{0}/{1}'.format(self._iq_server_base_url, status_url),
            auth=(self._user, self._password)).text,
        check_success=self.__handle_response,
        step=1,
        timeout=60)

  def __handle_response(self, response):
    try:
      res = json.loads(response)
      LOG.debug(res)
      if res['policyAction'] == 'None':
        LOG.debug("No policy issues, whew!")
      else:
        self._policy_action = res['policyAction']
      self._report_url = res['reportHtmlUrl']
      return True
    except JSONDecodeError as json_decode_error:
      LOG.debug(json_decode_error.msg)
      return False
