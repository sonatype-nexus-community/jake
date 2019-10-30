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
import ast

from jake.types.coordinateresults import CoordinateResults

class TestResultsDecoder(unittest.TestCase):
  def test_toJsonOnCoordinateResultsReturnsProperJson(self):
    undertest = CoordinateResults()
    undertest.setCoordinates("pkg:conda/thing@1.0.0")
    undertest.setReference("http://www.wrestling.com")
    undertest.setVulnerabilities([])

    result = undertest.toJSON()
    dictionary = ast.literal_eval(result)

    self.assertEqual(isinstance(result, str), True)
    self.assertEqual(dictionary['coordinates'], "pkg:conda/thing@1.0.0")
    self.assertEqual(dictionary['reference'], "http://www.wrestling.com")
    self.assertEqual(dictionary['vulnerabilities'], [])
    

