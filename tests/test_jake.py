# encoding: utf-8

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
import sys
import unittest
from jake import app


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.cmd = app._create_cmd()
        self.orig_args = sys.argv
        sys.argv = [sys.argv[0]]

    def tearDown(self):
        self.cmd = None
        sys.argv = self.orig_args

    def test_app_noargs(self):
        assert self.cmd is not None
        self.cmd.execute()


if __name__ == '__main__':
    unittest.main()
