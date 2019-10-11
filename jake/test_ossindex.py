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

import json

from jake.ossindex.ossindex import OssIndex

class TestOssIndex(unittest.TestCase):
    def setUp(self):
        self.func = OssIndex(url="http://blahblah", headers={"thing": "thing", "anotherthing": "anotherthing"})
    
    def test_getHeaders(self):
        self.assertEqual(self.func.get_headers(), {"thing": "thing", "anotherthing": "anotherthing"})

    def test_getUrl(self):
        self.assertEqual(self.func.get_url(), "http://blahblah")
    
    @patch('jake.ossindex.ossindex.requests.post')
    def test_callGetDependenciesReturnsPurls(self, mock_post):
        #expected_result = json.dumps(ast.literal_eval('{ "coordinates": [ "pkg:conda/thing"]}'))
        expected_result = '{ "coordinates": [ "pkg:conda/thing"]}'

        mock_post.return_value.status_code = 200
        mock_post.return_value.text = expected_result
        response = self.func.callOSSIndex("purls")
        
        self.assertEqual(len(response["coordinates"]), 1)
        self.assertEqual(response["coordinates"][0], "pkg:conda/thing")
