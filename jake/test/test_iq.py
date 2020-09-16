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
    self.third_party_url = '{0}/api/v2/scan/applications/{1}/sources/jake?stageId={2}'.format(
      iq_args['host'],
      self.internal_id,
      iq_args['stage']
    )

    self.func = IQ(args=iq_args)

#   @staticmethod
#   def get_fake_purls():
#     """get_fake_purls is a helper function that creates a fake Coordinate"""
#     fake_purls = Coordinates()
#     fake_purls.add_coordinate('thing', '1.1', 'conda')
#     fake_purls.add_coordinate('thing', '1.2', 'conda')
#     fake_purls.add_coordinate('thing', '1.3', 'conda')
#     return fake_purls

#   @staticmethod
#   def get_fake_actual_purls():
#     """get_fake_actual_purls is a helper function that creates a
#     fake Coordinate with realistic data"""
#     fake_actual_purls = Coordinates()
#     fake_actual_purls.add_coordinate('pycrypto', '2.6.1', 'conda')
#     return fake_actual_purls

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
    self.assertEqual(len(response), 32)
    self.assertEqual(response, '4537e6fe68c24dd5ac83efd97d4fc2f4')

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
    self.assertEqual(len(response), 32)
    self.assertEqual(response,
                     'api/v2/scan/applications/4537e6fe68c24dd5ac83efd97d4fc2f4/status/9cee2b6366fc4d328edc318eae46b2cb')
