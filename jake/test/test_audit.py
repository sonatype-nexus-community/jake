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

""" test_audit.py , for all your testing of audit py needs """
import unittest
import json

from pathlib import Path

from ..audit.audit import Audit
from ..types.results_decoder import ResultsDecoder

class TestAudit(unittest.TestCase):
  """ TestAudit is responsible for testing the Audit class """
  def setUp(self):
    self.func = Audit()

  def test_call_audit_results_prints_output(self):
    """ test_call_audit_results_prints_output ensures that when called with
    a valid result, audit_results returns the number of vulnerabilities found """
    filename = Path(__file__).parent / "ossindexresponse.txt"
    with open(filename, "r") as stdin:
      response = json.loads(
          stdin.read(),
          cls=ResultsDecoder)
    self.assertEqual(self.func.audit_results(response),
                     self.expected_results())

  @staticmethod
  def expected_results():
    """ Weeee, I'm helping! """
    return 3
