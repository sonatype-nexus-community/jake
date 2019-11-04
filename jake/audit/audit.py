""" audit.py for all your audit py needs """
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
import logging

from typing import List

from jake.types.coordinateresults import CoordinateResults
from jake.types.vulnerabilities import Vulnerabilities

class Audit():
  """ Audit does the business, it prints results from OSS Index to the standard out """
  def __init__(self):
    self._log = logging.getLogger('jake')

  def audit_results(self, results: List[CoordinateResults]):
    """
    audit_results is the ingest point for the results from OSS Index,
    and handles control flow
    """
    self._log.debug("Results recieved, %s total results", len(results))

    total_vulns = 0
    pkg_num = 0

    for coordinate in results:
      pkg_num += 1
      total_vulns += self.print_result(coordinate, pkg_num, len(results))

    return total_vulns

  def print_result(self, coordinate: CoordinateResults, number, length):
    """
    print_results takes a coordinate, the index of the coordinate in a list,
    and the length, and handles printing it in different formats if a
    vulnerability exists
    """
    if len(coordinate.get_vulnerabilities()) == 0:
      print("[{}/{}] - {} - no known vulnerabilities for this version"
            .format(
                number,
                length,
                coordinate.get_coordinates()))
      return len(coordinate.get_vulnerabilities())

    print(("[{}/{}] - {} [VULNERABLE] {} known vulnerabilities for"
           "this version")
          .format(
              number,
              length,
              coordinate.get_coordinates(),
              len(coordinate.get_vulnerabilities())))
    for vulnerability in coordinate.get_vulnerabilities():
      self.print_vulnerability(vulnerability)
    return len(coordinate.get_vulnerabilities())

  @classmethod
  def print_vulnerability(cls, vulnerability: Vulnerabilities):
    """
    print_vulnerability takes a vulnerability, and well, it prints it
    """
    print("ID: {}".format(vulnerability.get_id()))
    print("Title: {}".format(vulnerability.get_title()))
    print("Description: {}".format(vulnerability.get_description()))
    print("CVSS Score: {}".format(vulnerability.get_cvss_score()))
    if vulnerability.get_cvss_vector() is not None:
      print("CVSS Vector: {}".format(vulnerability.get_cvss_vector()))
    print("CVE: {}".format(vulnerability.get_cve()))
    print("Reference: {}".format(vulnerability.get_reference()))
    print("----------------------------------------------------")
