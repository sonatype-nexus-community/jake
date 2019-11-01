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

from jake.config.config import Config


class TestConfig(unittest.TestCase):
    def setUp(self):
        self.func = Config(save_location='/tmp/')

    def test_configObjectSavesConfigFile(self):
        self.func.setPassword("password")
        self.func.setUsername("test@me.com")
        result = self.func.saveConfigToFile()
        self.assertEqual(result, True)

    def test_getConfigFromFile(self):
        self.func.setPassword("password")
        self.func.setUsername("test@me.com")
        self.func.saveConfigToFile()

        (username, password) = self.func.getConfigFromFile()
        self.assertEqual(username, "test@me.com")
        self.assertEqual(password, "password")

    def test_returnTrueWhenConfigExists(self):
        self.func.setPassword("password")
        self.func.setUsername("test@me.com")
        self.func.saveConfigToFile()
        self.assertEqual(self.func.checkIfConfigExists(), True)
