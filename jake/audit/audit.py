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

""" audit.py for all your audit py needs """
# pylint: disable=no-else-return
import logging

from typing import List
from textwrap import wrap
from colorama import Fore
from terminaltables import DoubleTable

from ..types.coordinateresults import CoordinateResults
from ..types.vulnerabilities import Vulnerabilities

class Audit:
  """ Audit does the business, it prints results from OSS Index to the standard out """

  def __init__(self, quiet=False):
    self._log = logging.getLogger("jake")
    self._quiet = quiet

  def audit_results(self, results: List[CoordinateResults]):
    """
    audit_results is the ingest point for the results from OSS Index,
    and handles control flow
    """
    self._log.debug("Results received, %s total results", len(results))

    total_vulns = 0
    pkg_num = 0
    good = [x for x in results if len(x.get_vulnerabilities()) == 0]
    bad = [x for x in results if len(x.get_vulnerabilities()) > 0]

    if len(good) != 0:
      print()
      print("Non-Vulnerable Dependencies")
      print()
      for coordinate in good:
        pkg_num += 1
        total_vulns += self.print_result(coordinate, pkg_num, len(results))

    if len(bad) != 0:
      print()
      print("Vulnerable Dependencies")
      print()

      for coordinate in bad:
        pkg_num += 1
        total_vulns += self.print_result(coordinate, pkg_num, len(results))

    table_data = [
        ["Audited Dependencies", len(results)],
        ["Vulnerablities Found", total_vulns],
    ]

    table_instance = DoubleTable(table_data, "Summary")

    print()

    print(table_instance.table)

    return total_vulns

  def print_result(self, coordinate: CoordinateResults, number, length):
    """
    print_results takes a coordinate, the index of the coordinate in a list,
    and the length, and handles printing it in different formats if a
    vulnerability exists
    """
    if len(coordinate.get_vulnerabilities()) == 0:
      if not self._quiet:
        self.do_print(
            f"[{number}/{length}] - {coordinate.get_coordinates()}",
            0
        )
      return len(coordinate.get_vulnerabilities())
    self.do_print(
        f"[{number}/{length}] - {coordinate.get_coordinates()} [VULNERABLE]",
        coordinate.get_max_cvss_score(),
    )
    self.do_print(
        f"{len(coordinate.get_vulnerabilities())} known vulnerabilities for this version",
        coordinate.get_max_cvss_score(),
    )
    for vulnerability in coordinate.get_vulnerabilities():
      self.print_vulnerability(vulnerability)
    return len(coordinate.get_vulnerabilities())

  @classmethod
  def print_vulnerability(cls, vulnerability: Vulnerabilities):
    """
    print_vulnerability takes a vulnerability, and well, it prints it
    """
    cvss_score = vulnerability.get_cvss_score()
    table_data = [
        ["ID", vulnerability.get_id()],
        ["Title", vulnerability.get_title()],
        ["Description", '\n'.join(wrap(vulnerability.get_description(), 100))],
        ["CVSS Score", f"{vulnerability.get_cvss_score()} - {cls.get_cvss_severity(cvss_score)}"],
        ]
    if vulnerability.get_cvss_vector():
      table_data.append(
          ["CVSS Vector", vulnerability.get_cvss_vector()]
          )

    table_data.extend(
        [
            ["CVE", vulnerability.get_cve()],
            ["Reference", vulnerability.get_reference()]
        ]
        )
    table_instance = DoubleTable(table_data)
    table_instance.inner_heading_row_border = False
    table_instance.inner_row_border = True
    cls.do_print(table_instance.table, cvss_score)

    print("----------------------------------------------------")

  @classmethod
  def do_print(cls, text, cvss_score):
    """
    do_print takes text, and a cvss_score and prints it in a different text depending on
    the score
    """
    if cvss_score == 0:
      print(Fore.GREEN + text + Fore.RESET)
    elif 0 < cvss_score < 4:
      print(Fore.CYAN + text + Fore.RESET)
    elif 4 <= cvss_score < 7:
      print(Fore.LIGHTYELLOW_EX + text + Fore.RESET)
    elif 7 <= cvss_score < 9:
      print(Fore.YELLOW + text + Fore.RESET)
    else:
      print(Fore.RED + text + Fore.RESET)

  @classmethod
  def get_cvss_severity(cls, cvss_score):
    """
    get_cvss_severity takes a cvss_score and returns a human readable severity for it
    """
    if cvss_score == 0:
      return "None"
    elif 0 < cvss_score < 4:
      return "Low"
    elif 4 <= cvss_score < 7:
      return "Medium"
    elif 7 <= cvss_score < 9:
      return "High"
    else:
      return "Critical"
