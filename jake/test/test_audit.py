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
import unittest
import json

from jake.audit.audit import Audit
from jake.types.results_decoder import ResultsDecoder
from pathlib import Path


class TestAudit(unittest.TestCase):
    def setUp(self):
        self.func = Audit()

    def test_callauditResultsPrintsOutput(self):
        fn = Path(__file__).parent / "ossindexresponse.txt"
        with open(fn, "r") as stdin:
            response = json.loads(
              stdin.read(),
              cls=ResultsDecoder)
        self.assertEqual(self.func.auditResults(response),
                         self.expectedResults())

    def expectedResults(self):
        return 3
