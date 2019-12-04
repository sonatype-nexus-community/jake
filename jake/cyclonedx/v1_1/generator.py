"""generator.py will craft a CycloneDX 1.1 SBOM"""
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
from lxml import etree

XMLNS = "http://cyclonedx.org/schema/bom/1.1"
XMLNSV = "http://cyclonedx.org/schema/ext/vulnerability/1.0"

NSMAP = {"v" : XMLNSV}

class CycloneDx11Generator():
  """CycloneDx11Generator is responsible for taking identifiers
  and vulnerabilities and turning them into a CycloneDX 1.1 SBOM"""
  def create_xml_from_oss_index_results(self, results):
    xml = self.__create_root()
    xml = self.__create_component_nodes(xml, results)
    return xml

  def __create_root(self):
    xml = etree.Element('bom', {"xmlns": XMLNS, "version": "1"}, nsmap=NSMAP)
    return xml

  def __create_component_nodes(self, xml, component_list):
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
        vulnerabilities = self.__create_vulnerability_node(vulnerabilities, component.get_vulnerabilities(), component.get_coordinates())
        node.append(vulnerabilities)
    xml.append(components)
    return xml

  def __get_name_version_from_purl(self, purl):
    split_list = purl.split("/")
    second_split = split_list[1].split("@")
    return (second_split[0], second_split[1])

  def __create_vulnerability_node(self, xml, vulnerability_list, purl):
    for vuln in vulnerability_list:
      vulnerability = etree.Element("{%s}vulnerability" % XMLNSV, {"ref": purl})
      _id = etree.SubElement(vulnerability, "{%s}id" % XMLNSV)
      _id.text = vuln.cve
      source = etree.Element("{%s}source" % XMLNSV, {"name": "ossindex"})
      url = etree.SubElement(source, "{%s}url" % XMLNSV)
      url.text = vuln.reference
      vulnerability.append(source)
      ratings = etree.Element("{%s}ratings" % XMLNSV)
      rating = etree.SubElement(ratings, "{%s}rating" % XMLNSV)
      score = etree.SubElement(rating, "{%s}score" % XMLNSV)
      base = etree.SubElement(score, "{%s}base" % XMLNSV)
      base.text = str(vuln.cvss_score)
      vector = etree.SubElement(rating, "{%s}vector" % XMLNSV)
      vector.text = vuln.cvss_vector
      vulnerability.append(ratings)
      description = etree.SubElement(vulnerability, "{%s}description" % XMLNSV)
      description.text = vuln.description
      xml.append(vulnerability)
    return xml
