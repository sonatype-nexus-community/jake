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

"""test_sbom_generator.py audits the cyclonedx/1.1/CycloneDx11Generator class"""
import unittest
import pathlib
import json

from lxml import etree

from ..types.coordinateresults import CoordinateResults
from ..types.results_decoder import ResultsDecoder
from ..cyclonedx.generator import CycloneDxSbomGenerator

class TestSbomGenerator(unittest.TestCase):
  """TestSbomGenerator audits the cyclonedx/CycloneDxSbomGenerator class"""
  def setUp(self):
    self.func = CycloneDxSbomGenerator()

  def test_invalid_bom_version(self):
    """test_invalid_bom_version verifies using a non-implemented bom version fails"""
    self.assertRaises(NotImplementedError, CycloneDxSbomGenerator, "1.0")

  def test_can_create_valid_root_element(self):
    """test_can_create_valid_root_element tests if an sbom can be created
    using the cyclonedx/CycloneDxSbomGenerator class"""
    file = pathlib.Path(__file__).parent / "ossindexvulnerablesnipresponse.txt"
    with open(file, "r") as stdin:
      result = json.loads(stdin.read(), cls=ResultsDecoder)
    results = self.func.create_and_return_sbom(result)
    # Assert that it has a <bom>
    self.assertIsNotNone(results)
    self.assertEqual(etree.iselement(results), True)
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
    self.assertEqual(vulnerable_component.__getitem__(0).text, "ncurses")
    self.assertEqual(vulnerable_component.__getitem__(1).text, "6.1")
    self.assertEqual(vulnerable_component.__getitem__(2).text, "pkg:conda/ncurses@6.1")
    self.assertIsNotNone(vulnerable_component)
    self.assertEqual(vulnerable_component.__len__(), 4)
    vulnerabilities = vulnerable_component.__getitem__(3)
    self.assertEqual(vulnerabilities.__len__(), 5)

  def test__get_name_version_from_purl(self):
    """test__get_name_version_from_purl tests if a parameter suffix is removed from the
    sbom version field"""
    coord_result = CoordinateResults()
    coord_result.set_coordinates("pkg:pypi/yaspin@0.16.0?extension=tar.gz")
    coord_result_normal = CoordinateResults()
    coord_result_normal.set_coordinates("pkg:pypi/normalpurl@0.17.0")
    coord_results = [coord_result, coord_result_normal]
    sbom = self.func.create_and_return_sbom(coord_results)
    # Assert that it has a <bom>
    self.assertIsNotNone(sbom)
    self.assertEqual(etree.iselement(sbom), True)
    self.assertEqual(sbom.tag, 'bom')
    # Assert that it has a <components>
    self.assertIs(sbom.__len__(), 1, sbom.__len__())
    item = sbom.__getitem__(0)
    self.assertIsNotNone(item)
    self.assertEqual(item.tag, "components")
    self.assertIs(item.__len__(), 2)

    component = item.__getitem__(0)
    self.assertIsNotNone(component)
    self.assertEqual(component.tag, "component")
    self.assertEqual(component.__getitem__(0).text, "yaspin")
    self.assertEqual(component.__getitem__(1).text, "0.16.0")
    self.assertEqual(component.__getitem__(2).text, "pkg:pypi/yaspin@0.16.0?extension=tar.gz")
    self.assertIsNotNone(component)

    component_normal = item.__getitem__(1)
    self.assertIsNotNone(component_normal)
    self.assertEqual(component_normal.tag, "component")
    self.assertEqual(component_normal.__getitem__(0).text, "normalpurl")
    self.assertEqual(component_normal.__getitem__(1).text, "0.17.0")
    self.assertEqual(component_normal.__getitem__(2).text, "pkg:pypi/normalpurl@0.17.0")
    self.assertIsNotNone(component_normal)
