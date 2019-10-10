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

class Audit(object):
    def __init__(self):
        self._log = logging.getLogger('jake')

    def auditResults(self, results):
        self._log.debug(results)

        totalVulns = 0
        pkgNum = 0

        for coordinate in results:
            pkgNum += 1
            totalVulns += self.printResult(coordinate, pkgNum, len(results))

        return totalVulns

    def printResult(self, coordinate, number, length):
        if len(coordinate['vulnerabilities']) == 0:
            print("[{}/{}] - {} - no known vulnerabilities for this version".format(number, length, coordinate['coordinates']))
            return len(coordinate['vulnerabilities'])
        else:
            print("[{}/{}] - {} [VULNERABLE] {} known vulnerabilities for this version".format(number, length, coordinate['coordinates'], len(coordinate['vulnerabilities'])))
            for vulnerability in coordinate['vulnerabilities']:
                self.printVulnerability(vulnerability)
            return len(coordinate['vulnerabilities'])

    def printVulnerability(self, vulnerability):
        print(vulnerability)
