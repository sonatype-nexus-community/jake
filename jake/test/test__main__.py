""" test__main__.py , for all your testing of main py needs """
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
import io

import sys
import unittest

from jake.__main__ import get_config_from_std_in
from jake.config.config import Config
from jake.config.iq_config import IQConfig


class Test__Main__(unittest.TestCase):
  """ Test__Main__ is responsible for testing __Main__ """

  def test__get_config_from_std_in_with_ossindexconfig(self):
    """verify get config works with ossindex config"""
    testinput = """test@me.com
password
http://localhost:8070/"""
    sys.stdin = io.StringIO(testinput)

    config = Config()
    result = get_config_from_std_in(config)
    self.assertEqual(result, True)
    # reread stored config
    results = self.func.get_config_from_file(".iq-server-config")
    self.assertEqual(results["Username"], "test@me.com")
    self.assertEqual(results["Password"], "password")
    self.assertEqual(results["IQ-Server-Location"], "http://localhost:8070")

  def test__get_config_from_std_in_with_iqconfig(self):
    """verify get config works with iq config"""
    testinput = """test@me.com
password
http://localhost:8070/"""
    sys.stdin = io.StringIO(testinput)

    config = Config()
    config = IQConfig()
    result = get_config_from_std_in(config)
    self.assertEqual(result, True)
    # reread stored config
    results = self.func.get_config_from_file(".iq-server-config")
    self.assertEqual(results["Username"], "test@me.com")
    self.assertEqual(results["Password"], "password")
    self.assertEqual(results["IQ-Server-Location"], "http://localhost:8070")

