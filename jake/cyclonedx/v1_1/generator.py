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

"""generator.py will craft a CycloneDX 1.1 SBOM"""
import pathlib
import logging

from lxml import etree

XMLNS = "http://cyclonedx.org/schema/bom/1.1"
XMLNSV = "http://cyclonedx.org/schema/ext/vulnerability/1.0"

NSMAP = {"v" : XMLNSV}

class CycloneDx11Generator():
  """CycloneDx11Generator is responsible for taking identifiers
  and vulnerabilities and turning them into a CycloneDX 1.1 SBOM"""
  def __init__(self):
    self._log = logging.getLogger('jake')
    self.__xml = []

  def create_xml_from_purls(self, coords: list) -> (etree.Element):
    """parses a list of purls to generate an xml w/ only component nodes

    Arguments:
        coords -- list of purls (strings)

    Returns:
        xml -- list of etree.Element objects, component only nodes with no vulns
    """
    self.__create_root()
    components = etree.Element('components')
    for component in coords:
      node = etree.Element('component', {"type": "library", "bom-ref": component})
      nombre, versace = self.__get_name_version_from_purl(component)
      name = etree.SubElement(node, 'name')
      name.text = nombre
      version = etree.SubElement(node, 'version')
      version.text = versace
      purl = etree.SubElement(node, 'purl')
      purl.text = component
      components.append(node)
    self.__xml.append(components)
    return self.__xml

  def create_xml_from_oss_index_results(self, results: list) -> (etree.Element):
    """Takes the CoordinateResults list and creates an sbom in XML form"""
    self.__create_root()
    self.__create_component_nodes(results)
    return self.__xml

  @staticmethod
  def validate_xml_vulnerabilities(xml_vulnerabilities):
    """Validates the given xml against the xsd for vulnerability"""
    file = pathlib.Path(__file__).parent / "vuln.xsd"
    with open(file, "r") as stdin:
      xml_schema_d = etree.parse(stdin)
      xml_schema = etree.XMLSchema(xml_schema_d)
      return xml_schema.assertValid(xml_vulnerabilities)

  def validate_xml(self, xml=None):
    """Takes the XML generated and validates it against the xsd
    for the vulnerability"""
    file = pathlib.Path(__file__).parent / "vuln.xsd"
    with open(file, "r") as stdin:
      xml_schema_d = etree.parse(stdin)
      xml_schema = etree.XMLSchema(xml_schema_d)
      self._log.debug(etree.tostring(self.__xml))
      return xml_schema.assertValid(self.__xml) if xml is None else xml_schema.assertValid(xml)

  def __create_root(self):
    self.__xml = etree.Element('bom', {"xmlns": XMLNS, "version": "1"}, nsmap=NSMAP)

  def __create_component_nodes(self, component_list: list) -> (list):
    components = etree.Element('components')
    for component in component_list:
      node = etree.Element('component', {"type": "library", "bom-ref": component.get_coordinates()})
      nombre, versace = self.__get_name_version_from_purl(component.get_coordinates())
      name = etree.SubElement(node, 'name')
      name.text = nombre
      version = etree.SubElement(node, 'version')
      version.text = versace
      purl = etree.SubElement(node, 'purl')
      purl.text = component.get_coordinates()
      components.append(node)
      if len(component.get_vulnerabilities()) > 0:
        vulnerabilities = etree.Element("{%s}vulnerabilities" % XMLNSV, nsmap=NSMAP)
        self.__create_vulnerability_node(
            component.get_vulnerabilities(),
            component.get_coordinates(),
            vulnerabilities,
            node)
        self.validate_xml_vulnerabilities(vulnerabilities)
    self.__xml.append(components)

  @staticmethod
  def __get_name_version_from_purl(purl):
    split_list = purl.split("/")
    second_split = split_list[1].split("@")
    version_split = second_split[1].split("?")
    return (second_split[0], version_split[0])

  @staticmethod
  def __create_vulnerability_node(vulnerability_list, purl, vulnerabilities, node):
    for vuln in vulnerability_list:
      vulnerability = etree.Element("{%s}vulnerability" % XMLNSV, {"ref": purl})
      _id = etree.SubElement(vulnerability, "{%s}id" % XMLNSV)
      if vuln.get_cve() is None:
        _id.text = "ossindex"
      else:
        _id.text = vuln.get_cve()
      source = etree.Element("{%s}source" % XMLNSV, {"name": "ossindex"})
      url = etree.SubElement(source, "{%s}url" % XMLNSV)
      url.text = vuln.reference
      vulnerability.append(source)
      ratings = etree.Element("{%s}ratings" % XMLNSV)
      rating = etree.SubElement(ratings, "{%s}rating" % XMLNSV)
      score = etree.SubElement(rating, "{%s}score" % XMLNSV)
      base = etree.SubElement(score, "{%s}base" % XMLNSV)
      base.text = str(vuln.get_cvss_score())
      vector = etree.SubElement(rating, "{%s}vector" % XMLNSV)
      vector.text = vuln.get_cvss_vector()
      vulnerability.append(ratings)
      description = etree.SubElement(vulnerability, "{%s}description" % XMLNSV)
      description.text = vuln.description
      vulnerabilities.append(vulnerability)
    node.append(vulnerabilities)
