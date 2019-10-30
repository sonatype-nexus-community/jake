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

class ResultsDecoder(json.JSONDecoder):
  def __init__(self):
    json.JSONDecoder.__init__(self, object_hook=self.dict_to_object)

  def dict_to_object(self, dictionary):
    item = CoordinateResults()
    item.setCoordinates(dictionary["coordinates"])
    item.setReference(dictionary["reference"])
    item.setVulnerabilities(dictionary["vulnerabilities"])

    return item
