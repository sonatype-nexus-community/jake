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

from jake.types.coordinateresults import CoordinateResults
from jake.types.vulnerabilities import Vulnerabilities


class ResultsDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.dict_to_object)

    def dict_to_object(self, dictionary):
        if dictionary.get('coordinates') is not None:
            item = CoordinateResults()
            item.set_coordinates(dictionary.get("coordinates"))
            item.set_reference(dictionary.get("reference"))
            item.set_vulnerabilities(dictionary.get("vulnerabilities"))

            return item
        else:
            vulnerability = Vulnerabilities()
            vulnerability.add_id(dictionary.get("id"))
            vulnerability.add_title(dictionary.get("title"))
            vulnerability.add_description(dictionary.get("description"))
            vulnerability.add_cvssScore(dictionary.get("cvssScore"))
            vulnerability.add_cvssVector(dictionary.get('cvssVector'))
            vulnerability.add_cve(dictionary.get("cve"))
            vulnerability.add_reference(dictionary.get("reference"))

            return vulnerability
