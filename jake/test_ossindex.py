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
import ast
import unittest
from unittest.mock import Mock, patch
import sys
import pathlib

import json

from jake.ossindex.ossindex import OssIndex
from jake.parse.parse import Parse
from jake.parse.coordinates import Coordinates

class TestOssIndex(unittest.TestCase):
    def setUp(self):
        self.func = OssIndex(url="http://blahblah", headers={"thing": "thing", "anotherthing": "anotherthing"})
    
    def test_getHeaders(self):
        self.assertEqual(self.func.get_headers(), {"thing": "thing", "anotherthing": "anotherthing"})

    def test_getUrl(self):
        self.assertEqual(self.func.get_url(), "http://blahblah")

    def get_fakePurls(self):
        fakePurls = Coordinates()
        fakePurls.add_coordinate("pkg:conda/thing1")
        fakePurls.add_coordinate("pkg:conda/thing2")
        fakePurls.add_coordinate("pkg:conda/thing3")
        return fakePurls
    
    @patch('jake.ossindex.ossindex.requests.post')
    def test_callGetDependenciesReturnsPurls(self, mock_post):
        mock_result = '[{"coordinates": "pkg:conda/thing1"}, {"coordinates": "pkg:conda/thing2"}, {"coordinates": "pkg:conda/thing3"}]'

        mock_post.return_value.status_code = 200
        mock_post.return_value.text = mock_result
        response = self.func.callOSSIndex(self.get_fakePurls())
        
        self.assertEqual(len(response), 3)
        self.assertEqual(response[0]["coordinates"], "pkg:conda/thing1")

    def test_chunk(self):
        fn = pathlib.Path(__file__).parent / "condalistoutput.txt"
        sys.stdin = open(fn, "r")
        parse = Parse()
        purls = parse.getDependenciesFromStdin(sys.stdin)
        actual_result = self.func.chunk(purls)
        self.assertEqual(len(actual_result), 3)
        self.assertEqual(len(actual_result[0]), 128)
        self.assertEqual(actual_result[0][0], "pkg:conda/_ipyw_jlab_nb_ext_conf@0.1.0")
        self.assertEqual(actual_result[1][0], "pkg:conda/mistune@0.8.4")
        self.assertEqual(actual_result[2][0], "pkg:conda/yaml@0.1.7")
        