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

"""test_pip.py audits the Pip class"""
import unittest

from ..pip.pip import Pip
from ..types.coordinates import Coordinates

class TestPip(unittest.TestCase):
  """TestPip audits the Pip class"""
  def setUp(self):
    self.func = Pip()

  def test_call_get_dependencies_returns_purls(self):
    """test_call_get_dependencies_returns_purls ensures that calls to
    Pip.get_dependencies() returns a Coordinates object"""
    actual = self.func.get_dependencies()

    self.assertIsNotNone(actual)
    self.assertEqual(actual.__class__, Coordinates)
