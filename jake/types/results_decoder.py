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

"""results_decoder.py takes the JSON results from a call to OSSIndex and
 turns them into CoordinateResults or Vulnerabilities type objects"""
import json

from ..types.coordinateresults import CoordinateResults
from ..types.vulnerabilities import Vulnerabilities


class ResultsDecoder(json.JSONDecoder):
  """ResultsDecoder takes the JSON results from a call to OSSIndex and
 turns them into CoordinateResults or Vulnerabilities type objects"""
  def __init__(self):
    json.JSONDecoder.__init__(self, object_hook=self.dict_to_object)

  @classmethod
  def dict_to_object(cls, dictionary):
    """checks to see if dictionary item has coordinates key then if it does
 converts item into CoordinateResults, if it doesnt converts it to
 Vulnerabilities """
    if dictionary.get('coordinates') is not None:
      item = CoordinateResults()
      item.set_coordinates(dictionary.get("coordinates"))
      item.set_reference(dictionary.get("reference"))
      item.set_vulnerabilities(dictionary.get("vulnerabilities"))

      return item

    vulnerability = Vulnerabilities()
    vulnerability.set_id(dictionary.get("id"))
    vulnerability.set_title(dictionary.get("title"))
    vulnerability.set_description(dictionary.get("description"))
    vulnerability.set_cvss_score(dictionary.get("cvssScore"))
    vulnerability.set_cvss_vector(dictionary.get('cvssVector'))
    vulnerability.set_cve(dictionary.get("cve"))
    vulnerability.set_reference(dictionary.get("reference"))

    return vulnerability
