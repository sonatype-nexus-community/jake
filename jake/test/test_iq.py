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

"""test_iq.py audits the call to IQ"""
import unittest
import json

from pathlib import Path

import responses

from ..iq.iq import IQ
# from ..types.coordinates import Coordinates
# from ..types.coordinateresults import CoordinateResults
# from ..types.results_decoder import ResultsDecoder
# from ..types.vulnerabilities import Vulnerabilities

class TestIQ(unittest.TestCase):
  """TestIQ audits the call to IQ"""
  def setUp(self):
    iq_args = {}
    iq_args['application'] = 'testapp'
    iq_args['stage'] = 'develop'
    iq_args['user'] = 'admin'
    iq_args['password'] = 'admin123'
    iq_args['host'] = 'http://afakeurlthatdoesnotexist.com:8081'
    iq_args['conda'] = False
    iq_args['insecure'] = False

    self.internal_id = '4537e6fe68c24dd5ac83efd97d4fc2f4'
    self.status_id = '9cee2b6366fc4d328edc318eae46b2cb'
    self.third_party_url = '{0}/api/v2/scan/applications/{1}/sources/jake?stageId={2}'.format(
      iq_args['host'],
      self.internal_id,
      iq_args['stage']
    )
    self.status_url = 'api/v2/scan/applications/{0}/status/{1}'.format(
      self.internal_id,
      self.status_id
    )
    self.full_status_url = '{0}/{1}'.format(
      iq_args['host'],
      self.status_url
    )

    self.func = IQ(args=iq_args)

  @responses.activate
  def test_call_get_application_id(self):
    """test_call_get_application_id mocks a call to IQ
    and ensures that that calls to IQ for an application ID return
    an internal ID as expected"""
    file = Path(__file__).parent / "iqapplicationresponse.txt"
    with open(file, "r") as stdin:
      responses.add(responses.GET,
                    'http://afakeurlthatdoesnotexist.com:8081/api/v2/applications?publicId=testapp',
                    body=stdin.read(), status=200)
      response = self.func.get_internal_id()
    self.assertEqual(response, self.internal_id)

  @responses.activate
  def test_call_submit_sbom(self):
    """test_call_submit_sbom mocks a call to IQ
    and ensures that that calls to IQ with an sbom return
    a status URL as expected"""
    file = Path(__file__).parent / "iqapplicationresponse.txt"
    with open(file, "r") as stdin:
      responses.add(responses.GET,
                    'http://afakeurlthatdoesnotexist.com:8081/api/v2/applications?publicId=testapp',
                    body=stdin.read(), status=200)
    file = Path(__file__).parent / "iqstatusurlresponse.txt"
    with open(file, "r") as stdin:
      responses.add(responses.POST,
                    self.third_party_url,
                    body=stdin.read(), status=200)
      response = self.func.submit_sbom("sbom")
    self.assertEqual(response, self.status_url)

  @responses.activate
  def test_call_poll_report_none_policy_action(self):
    """test_call_poll_report_none_policy_action mocks a call to IQ
    and ensures that that calls to IQ asking for a poll
    response on a status URL, return as expected, and sets policy action
    to None"""
    file = Path(__file__).parent / "iqpolicynoneresponse.txt"
    with open(file, "r") as stdin:
      mock_json = json.loads(stdin.read())
      responses.add(responses.GET,
                    self.full_status_url,
                    json=mock_json, status=200)

      self.func.poll_report(self.status_url)
    self.assertEqual(self.func.get_policy_action(), 'None')

  @responses.activate
  def test_call_poll_report_failure_policy_action(self):
    """test_call_poll_report_failure_policy_action mocks a call to IQ
    and ensures that that calls to IQ asking for a poll
    response on a status URL, return as expected, and sets policy action
    to Failure"""
    file = Path(__file__).parent / "iqpolicyfailureresponse.txt"
    with open(file, "r") as stdin:
      mock_json = json.loads(stdin.read())
      responses.add(responses.GET,
                    self.full_status_url,
                    json=mock_json, status=200)

      self.func.poll_report(self.status_url)
    self.assertEqual(self.func.get_policy_action(), 'Failure')

  @responses.activate
  def test_call_poll_report_warning_policy_action(self):
    """test_call_poll_report_warning_policy_action mocks a call to IQ
    and ensures that that calls to IQ asking for a poll
    response on a status URL, return as expected, and sets policy action
    to Warning"""
    file = Path(__file__).parent / "iqpolicywarningresponse.txt"
    with open(file, "r") as stdin:
      mock_json = json.loads(stdin.read())
      responses.add(responses.GET,
                    self.full_status_url,
                    json=mock_json, status=200)

      self.func.poll_report(self.status_url)
    self.assertEqual(self.func.get_policy_action(), 'Warning')
