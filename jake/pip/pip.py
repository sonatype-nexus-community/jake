"""pip.py gets installed pip dependencies"""
# Copyright 2020 Sonatype Inc.
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
import pkg_resources

from jake.types.coordinates import Coordinates

class Pip():
  """pip.py gets installed pip dependencies"""
  def __init__(self):
    self._log = logging.getLogger('jake')

  def get_dependencies(self):
    """converts list of pkg_resource.working_set into purl coordinates"""
    purls = Coordinates()

    # pkg_resources.working_set will show as None at compile time
    # it is populated at runtime
    for i in iter(pkg_resources.working_set):
      purls.add_coordinate(self.parse_line_into_purl(i))

    return purls

  @classmethod
  def parse_line_into_purl(cls, line):
    """formats an object from pkg_resources.working_set into a purl"""
    template = "pkg:pypi/{}@{}?extension=tar.gz"
    return template.format(line.project_name, line._version)
