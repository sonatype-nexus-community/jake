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

"""coordinateresults.py creates a CoordinateResults type object"""
import json

class CoordinateResults():
  """CoordinateResults creates a CoordinateResults type object"""
  def __init__(self):
    self.coordinates = ""
    self.reference = ""
    self.vulnerabilities = []

  def set_coordinates(self, coordinate):
    """sets coordinates for CoordinateResults obj"""
    self.coordinates = coordinate

  def get_coordinates(self):
    """gets coordinates for CoordinateResults obj"""
    return self.coordinates

  def set_reference(self, reference):
    """sets reference for CoordinateResults obj"""
    self.reference = reference

  def get_reference(self):
    """get reference for CoordinateResults obj"""
    return self.reference

  def set_vulnerabilities(self, vulnerabilities):
    """sets vulnerabilities for CoordinateResults obj"""
    self.vulnerabilities = vulnerabilities

  def get_vulnerabilities(self):
    """sets vulnerabilities for CoordinateResults obj"""
    return self.vulnerabilities

  def get_max_cvss_score(self):
    """gets the max cvss_score for vulnerabilities list"""
    # if not self.vulnerabilities:
    #   return None
    return max(vulnerability.get_cvss_score() for vulnerability in self.vulnerabilities)

  def to_json(self):
    """converts CoordinateResults obj to JSON"""
    return json.dumps(self.__dict__, default=lambda o: o.__dict__)
