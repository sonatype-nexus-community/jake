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
import json

class CoordinateResults(object):
  def __init__(self):
    self._coordinates = ""
    self._reference = ""
    self._vulnerabilities = []
  
  def setCoordinates(self, coordinate):
    self._coordinates = coordinate

  def getCoordinates(self):
    return self._coordinates
  
  def setReference(self, reference):
    self._reference = reference

  def getReference(self):
    return self._reference

  def addVulnerability(self, vulnerability):
    self._vulnerabilities = vulnerability

  def getVulnerabilities(self):
    return self._vulnerabilities

  def toJSON(self):
    return json.dumps(self, default=lambda o: CoordinateJsonResult(o.getCoordinates(), o.getReference(), o.getVulnerabilities()).__dict__)

class CoordinateJsonResult(object):
  def __init__(self, coordinate, reference, vulnerabilities):
    self.coordinates = coordinate
    self.reference = reference
    self.vulnerabilities = vulnerabilities
