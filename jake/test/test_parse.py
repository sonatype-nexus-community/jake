"""test_parse.py adits the Parse class"""
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
import pathlib

from jake.parse.parse import Parse


class TestParse(unittest.TestCase):
  """TestParse audits the Parse class"""
  def setUp(self):
    self.func = Parse()

  def test_call_get_dependencies_returns_purls(self):
    """test_call_get_dependencies_returns_purls ensures that calls to
    Parse.get_coordinates() returns a list of purls"""
    file = pathlib.Path(__file__).parent / "condalistoutput.txt"
    with open(file, "r") as stdin:
      actual = self.func.get_dependencies_from_stdin(stdin)
      output = actual.get_coordinates()
    self.assertEqual(len(output), 262)
    self.assertEqual(output[0], "pkg:conda/_ipyw_jlab_nb_ext_conf@0.1.0")
    self.assertEqual(output[131], "pkg:conda/mkl_fft@1.0.12")
    self.assertEqual(output[261], "pkg:conda/zstd@1.3.7")
