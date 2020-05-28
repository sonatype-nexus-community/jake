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

"""test_results_decoder.py audits the ResultsDecoder class"""
import unittest
import pathlib
import json

from ..types.results_decoder import ResultsDecoder
from ..types.coordinateresults import CoordinateResults


class TestResultsDecoder(unittest.TestCase):
  """TestResultsDecoder audits the ResultsDecoder class"""
  def test_results_decoder_can_transform_ossindex_response(self):
    """test_results_decoder_can_transform_ossindex_response ensures calls
    to ResultsDecorder will return a CoordinateResults typed object"""
    file = pathlib.Path(__file__).parent / "ossindexresponse.txt"
    with open(file, "r") as stdin:
      result = json.loads(stdin.read(), cls=ResultsDecoder)
    self.assertEqual(len(result), 32)
    self.assertEqual(isinstance(result, list), True)
    self.assertEqual(isinstance(result[0], CoordinateResults), True)
    self.assertEqual(result[0].get_coordinates(),
                     "pkg:conda/pycrypto@2.6.1")
    self.assertEqual(result[0].get_reference(
    ), "https://ossindex.sonatype.org/component/pkg:conda/pycrypto@2.6.1")
    self.assertEqual(isinstance(
        result[0].get_vulnerabilities(),
        list), True)
    self.assertEqual(len(result[0].get_vulnerabilities()), 0)
