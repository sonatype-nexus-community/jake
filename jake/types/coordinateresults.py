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
        self.coordinates = ""
        self.reference = ""
        self.vulnerabilities = []

    def set_coordinates(self, coordinate):
        self.coordinates = coordinate

    def get_coordinates(self):
        return self.coordinates

    def set_reference(self, reference):
        self.reference = reference

    def get_reference(self):
        return self.reference

    def set_vulnerabilities(self, vulnerabilities):
        self.vulnerabilities = vulnerabilities

    def get_vulnerabilities(self):
        return self.vulnerabilities

    def toJSON(self):
        return json.dumps(self.__dict__, default=lambda o: o.__dict__)
