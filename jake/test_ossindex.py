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
from pathlib import Path
from tinydb import TinyDB, Query
import json

from jake.ossindex.ossindex import OssIndex
from jake.parse.parse import Parse
from jake.parse.coordinates import Coordinates

class TestOssIndex(unittest.TestCase):
    def setUp(self):
        self.func = OssIndex(url="http://blahblah", headers={"thing": "thing", "anotherthing": "anotherthing"}, cache_location="/tmp")
        self.parse = Parse()
    
    def tearDown(self):
        if Path('/tmp/.ossindex/jake.json').exists():
            Path('/tmp/.ossindex/jake.json').unlink()
    
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
        fn = Path(__file__).parent / "condalistoutput.txt"
        sys.stdin = open(fn, "r")
        
        purls = self.parse.getDependenciesFromStdin(sys.stdin)
        actual_result = self.func.chunk(purls)
        self.assertEqual(len(actual_result), 3)
        self.assertEqual(len(actual_result[0]), 128)
        self.assertEqual(actual_result[0][0], "pkg:conda/_ipyw_jlab_nb_ext_conf@0.1.0")
        self.assertEqual(actual_result[1][0], "pkg:conda/mistune@0.8.4")
        self.assertEqual(actual_result[2][0], "pkg:conda/yaml@0.1.7")

    def test_insertIntoCache(self):
        fn = Path(__file__).parent / "ossindexresponse.txt"
        sys.stdin = open(fn, "r")
        (cached, num_cached) = self.func.maybeInsertIntoCache(sys.stdin.read())
        self.assertEqual(num_cached, 46)
        self.assertEqual(cached, True)

    def test_getPurlsFromCache(self):
        self.func.maybeInsertIntoCache("[{'coordinates': 'pkg:conda/_ipyw_jlab_nb_ext_conf@0.1.0', 'reference': 'https://ossindex.sonatype.org/component/pkg:conda/_ipyw_jlab_nb_ext_conf@0.1.0', 'vulnerabilities': []}, {'coordinates': 'pkg:conda/alabaster@0.7.12', 'reference': 'https://ossindex.sonatype.org/component/pkg:conda/alabaster@0.7.12', 'vulnerabilities': []}, {'coordinates': 'pkg:conda/anaconda@2019.07', 'reference': 'https://ossindex.sonatype.org/component/pkg:conda/anaconda@2019.07', 'vulnerabilities': []}]")
        (new_purls, results) = self.func.getPurlsAndResultsFromCache("[{'coordinates': 'pkg:conda/_ipyw_jlab_nb_ext_conf@0.1.0', 'reference': 'https://ossindex.sonatype.org/component/pkg:conda/_ipyw_jlab_nb_ext_conf@0.1.0', 'vulnerabilities': []}]")
        self.assertEqual(results[0], "[{'coordinates': 'pkg:conda/_ipyw_jlab_nb_ext_conf@0.1.0', 'reference': 'https://ossindex.sonatype.org/component/pkg:conda/_ipyw_jlab_nb_ext_conf@0.1.0', 'vulnerabilities': []}]")