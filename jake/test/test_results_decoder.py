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
import pathlib
import json

from typing import List

from jake.types.results_decoder import ResultsDecoder
from jake.types.coordinateresults import CoordinateResults

class TestResultsDecoder(unittest.TestCase):
  def test_resultsDecoderCanTransformOssIndexResponseIntoCoordinateResultsList(self):
    fn = pathlib.Path(__file__).parent / "ossindexresponse.txt"
    with open(fn, "r") as stdin:
      result = json.loads(stdin.read().replace("'", '"'), cls=ResultsDecoder)
    self.assertEqual(len(result), 46)
    self.assertEqual(isinstance(result, List), True)
    self.assertEqual(isinstance(result[0], CoordinateResults), True)
    self.assertEqual(result[0].getCoordinates(), "pkg:conda/astroid@2.3.1")
    self.assertEqual(result[0].getReference(), "https://ossindex.sonatype.org/component/pkg:conda/astroid@2.3.1")
    self.assertEqual(isinstance(result[0].getVulnerabilities(), List), True)
    self.assertEqual(len(result[0].getVulnerabilities()), 0)
