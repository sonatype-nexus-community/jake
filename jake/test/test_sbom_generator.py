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
from jake.cyclonedx.generator import CycloneDxSbomGenerator

class TestSbomGenerator(unittest.TestCase):
  """TestSbomGenerator audits the cyclonedx/CycloneDxSbomGenerator class"""
  def setUp(self):
    self.func = CycloneDxSbomGenerator()

  def test_can_create_valid_root_element(self):
    """test_can_create_valid_root_element tests if an sbom can be created
    using the cyclonedx/CycloneDxSbomGenerator class"""
    file = pathlib.Path(__file__).parent / "ossindexvulnerablesnipresponse.txt"
    with open(file, "r") as stdin:
      result = json.loads(stdin.read(), cls=ResultsDecoder)
    results = self.func.create_and_return_sbom(result)
    # Assert that it has a <bom>
    self.assertIsNotNone(results)
    self.assertIsInstance(results, etree._Element)
    self.assertEqual(results.tag, 'bom')
    # Assert that it has a <components>
    self.assertIs(results.__len__(), 1, results.__len__())
    item = results.__getitem__(0)
    self.assertIsNotNone(item)
    self.assertEqual(item.tag, "components")
    self.assertIs(item.__len__(), 15)
    component = item.__getitem__(0)
    self.assertIsNotNone(component)
    self.assertEqual(component.tag, "component")
    vulnerable_component = item.__getitem__(14)
    self.assertIsNotNone(vulnerable_component)
