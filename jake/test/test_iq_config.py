"""test_iq_config.py verifies the IQConfig class"""
# Copyright 2020 Sonatype Inc.
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

from jake.config.iq_config import IQConfig

class TestIQConfig(unittest.TestCase):
  """testIQConfig verifies the IQConfig class"""
  def setUp(self):
    self.func = IQConfig(save_location='/tmp/')

  def tearDown(self):
    sys.stdin = sys.__stdin__

  def test_get_config_from_std_in(self):
    """test_get_config_from_std_in verifies the IQConfig class"""
    testinput = """test@me.com
password
http://localhost:8070/"""
    sys.stdin = io.StringIO(testinput)
    result = self.func.get_config_from_std_in()
    self.assertEqual(result, True)
    # reread stored config
    results = self.func.get_config_from_file({"Username",
                                              "Password",
                                              "IQ-Server-Location"},
                                             ".iq-server-config")
    self.assertEqual(results["Username"], "test@me.com")
    self.assertEqual(results["Password"], "password")
    self.assertEqual(results["IQ-Server-Location"], "http://localhost:8070")
