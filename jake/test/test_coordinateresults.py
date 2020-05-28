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

"""test_coordinateresults.py audits the CoordinateResult type"""
import unittest
import ast

from ..types.coordinateresults import CoordinateResults


class TestResultsDecoder(unittest.TestCase):
  """TestResultsDecoder ensures CoordinateResults are probably decoded to JSON"""
  def test_to_json_on_coordinateresults_returns_proper_json(self):
    """ensures that the to_json method for the CoordinateResults type returns
     proper JSON"""
    undertest = CoordinateResults()
    undertest.set_coordinates("pkg:conda/thing@1.0.0")
    undertest.set_reference("http://www.wrestling.com")
    undertest.set_vulnerabilities(
        '[{"id":"156d71e4-6ed5-4d5f-ae47-7d57be01d387",'
        '"title":"[CVE-2019-16056]'
        ' jake the snake","cvssScore":0.0,"cve":"CVE-2019-16056"'
        ',"reference":"http://www.wrestling.com"}]')

    result = undertest.to_json()
    dictionary = ast.literal_eval(result)

    self.assertEqual(isinstance(result, str), True)
    self.assertEqual(dictionary['coordinates'], "pkg:conda/thing@1.0.0")
    self.assertEqual(dictionary['reference'], "http://www.wrestling.com")
    self.assertEqual(dictionary['vulnerabilities'],
                     '[{"id":"156d71e4-6ed5-4d5f-ae47-7d57be01d387",'
                     '"title":"[CVE-2019-16056] jake the snake",'
                     '"cvssScore":0.0,"cve":"CVE-2019-16056",'
                     '"reference":"http://www.wrestling.com"}]')
