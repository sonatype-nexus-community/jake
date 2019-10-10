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

from parse.parse import Parse

class TestParse(unittest.TestCase):
    def setUp(self):
        self.func = Parse()
    
    def test_callGetDependenciesReturnsPurls(self):
        self.assertEqual(self.func.getDependencies(run_command_list=self.mockListCommand), json.dumps({"coordinates": ["pkg:pypi/django@1.11.1", "pkg:pypi/django@1.11.2"]}))

    def mockListCommand(self):
        return json.dumps({"coordinates": ["pkg:pypi/django@1.11.1", "pkg:pypi/django@1.11.2"]})
