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

"""generator.py will craft and validate a CycloneDX SBOM"""
# pylint: disable=protected-access
import logging

from lxml import etree

from ..cyclonedx.v1_1.generator import CycloneDx11Generator

class CycloneDxSbomGenerator():
  """CycloneDxGenerator is responsible for taking identifiers
  and vulnerabilities and turning them into a CycloneDX SBOM.
  By default it will generate a 1.1 version of the SBOM, if sbom_version
  is set to a different version (and an accompanying implementation is
  done) it can create it. Currently only 1.1 is implemented, any other value
  for sbom_version will throw a NotImplementedError"""
  def __init__(self, sbom_version="1.1"):
    self._log = logging.getLogger('jake')
    if sbom_version == "1.1":
      self.__generator = CycloneDx11Generator()
    else:
      raise NotImplementedError

  def purl_sbom(self, purls: list) -> (etree.Element):
    """ get sbom from a list of purls

    Arguments:
        purls -- list of purls (strings)

    Returns:
        sbom as a list of lxml.etree.Element nodes
        coordinate data only
    """
    sbom = self.__generator.create_xml_from_purls(purls)
    return sbom

  def create_and_return_sbom(self, results) -> (list):
    """create_and_return_sbom is responsible for taking results in
    CoordinateResults form and turning them into a valid CycloneDX SBOM"""
    sbom = self.__generator.create_xml_from_oss_index_results(results)
    return sbom

  @staticmethod
  def sbom_to_string(sbom: etree.Element) -> (bytes):
    """sbom_to_string is responsible for turning an sbom into a string"""
    return etree.tostring(sbom, encoding="UTF-8")

  def validate_sbom(self, sbom):
    """validate_sbom is responsible for taking an sbom in etree Element
     form and validating it against an internal CycloneDX XSD"""
    valid = self.__generator.validate_xml(sbom)
    if valid:
      return sbom
    raise ValueError("Something is wrong with the OSS Index results")
