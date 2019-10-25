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
from shutil import which

from .coordinates import Coordinates

class Parse(object):
    def __init__(self):
        self._log = logging.getLogger('jake')

    def getDependencies(self, run_command_list):
        if self.checkIfCondaExists():
            return self.reallyGetCondaDependencies(run_command_list)
        else:
            return None

    def getDependenciesFromStdin(self, stdin):
        return self.parseCondaDependenciesIntoPurls(stdin)

    def checkIfCondaExists(self):
        self._log.debug(which("python"))
        condaExists = which("conda")

        self._log.debug(condaExists)

        if condaExists is not None:
            return True
        else:
            return False

    def reallyGetCondaDependencies(self, run_command_list):
        results = self.runCondaListCommand(run_command_list)

        #self._log.debug("results: " + results)
        length = len(results)

        if results[length-1] == 0:
            return self.parseCondaDependenciesIntoPurls(results)
        else:
            return None

    def runCondaListCommand(self, run_command_list):
        return run_command_list

    def parseCondaDependenciesIntoPurls(self, stdin):
        purls = Coordinates()
        self._log.debug("Starting to parse results")
        for line in stdin:
            if "#" in line:
                self._log.debug("Skipping line")
            else:
                purl = self.parseLineIntoPurl(line)
                if purl is not None:
                    purls.add_coordinate(self.parseLineIntoPurl(line))
        if len(purls.get_coordinates()) == 0:
            return None
        else:
            return purls.get_coordinates_as_json()

    def parseLineIntoPurl(self, line):
        lineArray = line.split()
        template = "pkg:conda/{}@{}"
        if len(lineArray) is not 0:
            return template.format(lineArray[0], lineArray[1])
        else:
            return None
