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

import pytest as pytest
from unittest.mock import patch

from jake import app


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.cmd = app._create_cmd()

    def tearDown(self):
        self.cmd = None

    def test_app_noargs(self):
        self.cmd.execute()

    def test_app_bad_arg(self):
        test_args = ["prog", "bad-arg-name"]
        with patch.object(sys, 'argv', test_args):
            with pytest.raises(SystemExit) as pytest_wrapped_e:
                # force re-read of args
                self.cmd.__init__()
                self.cmd.execute()

        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == 2


if __name__ == '__main__':
    unittest.main()
