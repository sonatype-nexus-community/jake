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

import requests
import polling

DEFAULT_HEADERS = {
    'User-Agent': 'jake'}

class IQ():
  def __init__(self, public_application_id, iq_server_base_url='http://localhost:8070/'):
    self._log = logging.getLogger('jake')
    self._iq_server_base_url = iq_server_base_url
    self._public_application_id = public_application_id
    self._headers = DEFAULT_HEADERS
    self._internal_application_id = ''
    self._user = 'admin'
    self._password = 'admin123'
    self._status_url = ''
    self._report_url = ''
    self._policy_action = None

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
    return self._public_application_id

  def set_application_internal_id(self, _id):
    self._internal_application_id = _id
  
  def get_application_internal_id(self):
    return self._internal_application_id

  def get_internal_application_id_from_iq_server(self):
    response = requests.get(
        '{}api/v2/applications?publicId={}'.format(
            self.get_url(),
            self.get_public_application_id()),
        self.get_headers(),
        auth=(self._user, self._password))
    if response.ok:
      res = json.loads(response.text)
      self._log.debug(res['applications'][0]['id'])
      self._internal_application_id = res['applications'][0]['id']
    else:
      raise ValueError(response.text)

  def submit_sbom_to_third_party_api(self, sbom):
    headers = self.get_headers()
    headers['Content-Type'] = 'application/xml'
    response = requests.post(
        '{0}api/v2/scan/applications/{1}/sources/ossindex'.format(
            self.get_url(),
            self.get_application_internal_id()),
        data=sbom,
        headers=headers,
        auth=(self._user, self._password))
    if response.ok:
      res = json.loads(response.text)
      self._status_url = res['statusUrl']
      self._log.debug(self._status_url)
    else:
      raise ValueError(response.text)

  def poll_for_results(self):
    polling.poll(
        lambda: requests.get(
            '{0}{1}'.format(self._iq_server_base_url, self._status_url),
            auth=(self._user, self._password)).text,
        check_success=self.__handle_response,
        step=1,
        timeout=60)

  def __handle_response(self, response):
    try:
      res = json.loads(response)
      self._log.debug(res)
      if res['policyAction'] == 'None':
        self._log.debug("No policy issues, whew!")
      else:
        self._policy_action = res['policyAction']
      self._report_url = res['reportHtmlUrl']
      return True
    except Exception as e:
      self._log.debug(e)
      return False
