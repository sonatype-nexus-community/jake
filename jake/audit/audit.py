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


class Audit(object):
    def __init__(self):
        self._log = logging.getLogger('jake')

    def auditResults(self, results: List[CoordinateResults]):
        self._log.debug("Results recieved, %s total results", len(results))

        totalVulns = 0
        pkgNum = 0

        for coordinate in results:
            pkgNum += 1
            totalVulns += self.printResult(coordinate, pkgNum, len(results))

        return totalVulns

    def printResult(self, coordinate: CoordinateResults, number, length):
        if len(coordinate.get_vulnerabilities()) == 0:
            print("[{}/{}] - {} - no known vulnerabilities for this version"
                  .format(
                    number,
                    length,
                    coordinate.get_coordinates()))
            return len(coordinate.get_vulnerabilities())
        else:
            print(("[{}/{}] - {} [VULNERABLE] {} known vulnerabilities for"
                  "this version").format(
                    number,
                    length,
                    coordinate.get_coordinates(),
                    len(coordinate.get_vulnerabilities())))
            for vulnerability in coordinate.get_vulnerabilities():
                self.printVulnerability(vulnerability)
            return len(coordinate.get_vulnerabilities())

    def printVulnerability(self, vulnerability: Vulnerabilities):
        print("ID: {}".format(vulnerability.get_id()))
        print("Title: {}".format(vulnerability.get_title()))
        print("Description: {}".format(vulnerability.get_description()))
        print("CVSS Score: {}".format(vulnerability.get_cvssScore()))
        if vulnerability.get_cvssVector() is not None:
            print("CVSS Vector: {}".format(vulnerability.get_cvssVector()))
        print("CVE: {}".format(vulnerability.get_cve()))
        print("Reference: {}".format(vulnerability.get_reference()))
        print("----------------------------------------------------")
