"""test_sbom_generator.py audits the cyclonedx/1.1/CycloneDx11Generator class"""
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
import json

from lxml import etree

from jake.types.results_decoder import ResultsDecoder
from jake.cyclonedx.v1_1.generator import CycloneDx11Generator

class TestSbomGenerator(unittest.TestCase):
  """TestSbomGenerator audits the cyclonedx/1_1/CycloneDx11Generator class"""
  def setUp(self):
    self.func = CycloneDx11Generator()

  def test_can_create_valid_root_element(self):
    """test_can_create_valid_root_element tests if an sbom can be created
    using the cyclonedx/1_1/CycloneDx11Generator class"""
    file = pathlib.Path(__file__).parent / "ossindexvulnerableresponse.txt"
    with open(file, "r") as stdin:
      result = json.loads(stdin.read(), cls=ResultsDecoder)
    results = self.func.create_xml_from_oss_index_results(result)
    print(etree.tostring(results, pretty_print=True))
