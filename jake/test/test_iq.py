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

  @responses.activate
  def test_call_poll_report_absolute_result_url(self):
    """test_call_poll_report_relative_result_url mocks a call to IQ
    and ensures an absolute report URL is returned,
    and ensure that same absolute report URL is returned from get_absolute_report_url()"""
    file = Path(__file__).parent / "iqresponse_absolute_report_url.json"
    with open(file, "r") as stdin:
      mock_json = json.loads(stdin.read())
      responses.add(responses.GET,
                    self.full_status_url,
                    json=mock_json, status=200)

      self.func.poll_report(self.status_url)
    # pylint: disable=W0212
    self.assertEqual(self.func._iq_url, 'http://afakeurlthatdoesnotexist.com:8081')
    self.assertEqual(self.func.get_report_url(),
                     'http://localhost:8070/ui/links/application/my-app/report/95c4c14e')
    # ensure we use the IQ provided absolute URL
    self.assertEqual(self.func.get_absolute_report_url(),
                     'http://localhost:8070/ui/links/application/my-app/report/95c4c14e')

  @responses.activate
  def test_call_poll_report_relative_result_url(self):
    """test_call_poll_report_relative_result_url mocks a call to IQ
    and ensures a relative report URL is returned,
    and ensure get_absolute_report_url() returns an absolute URL
    built from the _iq_url and relative report URL"""
    file = Path(__file__).parent / "iqresponse_relative_report_url.json"
    with open(file, "r") as stdin:
      mock_json = json.loads(stdin.read())
      responses.add(responses.GET,
                    self.full_status_url,
                    json=mock_json, status=200)

      self.func.poll_report(self.status_url)
    # pylint: disable=W0212
    self.assertEqual(self.func._iq_url, 'http://afakeurlthatdoesnotexist.com:8081')
    self.assertEqual(self.func.get_report_url(),
                     'ui/links/application/my-app/report/95c4c14e')
    # build the absolute URL from the IQ Server base url
    self.assertEqual(self.func.get_absolute_report_url(),
        'http://afakeurlthatdoesnotexist.com:8081/ui/links/application/my-app/report/95c4c14e')
