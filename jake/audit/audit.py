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
        if len(coordinate.getVulnerabilities()) == 0:
            print("[{}/{}] - {} - no known vulnerabilities for this version".format(number, length, coordinate.getCoordinates()))
            return len(coordinate.getVulnerabilities())
        else:
            print("[{}/{}] - {} [VULNERABLE] {} known vulnerabilities for this version".format(number, length, coordinate.getCoordinates(), len(coordinate.getVulnerabilities())))
            for vulnerability in coordinate.getVulnerabilities():
                self.printVulnerability(vulnerability)
            return len(coordinate.getVulnerabilities())

    def printVulnerability(self, vulnerability):
        print(vulnerability)
