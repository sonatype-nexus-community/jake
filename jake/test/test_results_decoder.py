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
            result = json.loads(stdin.read(), cls=ResultsDecoder)
        self.assertEqual(len(result), 32)
        self.assertEqual(isinstance(result, List), True)
        self.assertEqual(isinstance(result[0], CoordinateResults), True)
        self.assertEqual(result[0].get_coordinates(),
                         "pkg:conda/pycrypto@2.6.1")
        self.assertEqual(result[0].get_reference(
        ), "https://ossindex.sonatype.org/component/pkg:conda/pycrypto@2.6.1")
        self.assertEqual(isinstance(
            result[0].get_vulnerabilities(), 
            List), True)
        self.assertEqual(len(result[0].get_vulnerabilities()), 0)
