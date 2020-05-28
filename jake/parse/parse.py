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

"""parse.py parses dependencies and converts them to purls"""
import logging
from shutil import which

from ..types.coordinates import Coordinates

class Parse():
  """parse.py parses dependencies and converts them to purls"""
  def __init__(self):
    self._log = logging.getLogger('jake')
    self._format = "conda"

  def get_dependencies(self, run_command_list):
    """checks if conda exists and then gets a list of conda dependencies from stdout"""
    if self.check_if_conda_exists():
      return self.really_get_conda_dependencies(run_command_list)
    return None

  def get_deps_stdin(self, stdin):
    """gets depdencies from stdin"""
    return self.parse_conda_dependencies_into_purls(stdin)

  def check_if_conda_exists(self):
    """checks to see if user installed conda"""
    self._log.debug(which("python"))
    conda_exists = which("conda")

    self._log.debug(conda_exists)

    if conda_exists is not None:
      return True

    return False

  def really_get_conda_dependencies(self, run_command_list):
    """gets a list of installed conda dependencies"""
    results = self.run_conda_list_command(run_command_list)

    length = len(results)

    if results[length-1] == 0:
      return self.parse_conda_dependencies_into_purls(results)

    return None

  @classmethod
  def run_conda_list_command(cls, run_command_list):
    """checks stdout to see if user installed conda"""
    return run_command_list

  def parse_conda_dependencies_into_purls(self, stdin):
    """converts list of dependencies from stdin into purl coordinates"""
    coords = Coordinates()
    self._log.debug("Starting to parse results")
    for line in stdin:
      if "#" in line:
        self._log.debug("Skipping line")
      else:
        line_array = line.split()
        if len(line_array) != 0:
          coords.add_coordinate(line_array[0], line_array[1], self._format)

    if len(coords.get_coordinates()) == 0:
      return None

    return coords
