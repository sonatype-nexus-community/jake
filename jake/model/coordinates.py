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

"""coordinates.py creates a Coordinates type object"""
import json

class Coordinates():
  """
  An object that contains a dict with name/version/source keys and purl values
  It also generates the purl as a string from the coordinate values passed in
  Allows for joins with other Coordinate dicts, adding coordinates, and retrieving
  as a dict or list of purl strings
  """

  def __init__(self):
    self._coordinates = dict()
    # extension needed for IQ ingestion of pypi components
    self._pypi_extension = "?extension=tar.gz"

  def add_coordinate(self, name: str, version: str, source: str):
    """
    adds a coordinate to the object dict based on coordinate values
    """
    purl = self.parse_to_purl(name, version, source)
    self._coordinates[(name, version, source)] = purl

  def get_coordinates(self) -> (dict):
    """gets the coordinates set"""
    return self._coordinates

  def get_purls(self) -> (list):
    """
    gets a list of purls from the objects dict values

    Returns:
        list -- purls as strings
    """
    return list(self._coordinates.values())

  def get_coordinates_as_json(self) -> (str):
    """turns the coordinates array to JSON"""
    coordinates = {}
    coordinates['coordinates'] = self._coordinates
    return json.dumps(coordinates)

  def parse_to_purl(self, name: str, version: str, source: str) -> (str):
    """
    parses a single name, version, source set into a purl

    Returns:
        string -- purl
    """

    template = "pkg:{}/{}@{}"
    purl = template.format(source, name, version)

    # adds the pypi extension for IQ (does not affect oss index results)
    if source == "pypi":
      purl += self._pypi_extension
    return purl

  def join_coords(self, coords: dict):
    """
    Takes in a dict generated from another Coordinates object and joins them,
    then sets the current objects dict to the result

    Returns:
        Coordinates object -- updated object with the joined dict
    """

    self._coordinates.update(coords)
    return self
