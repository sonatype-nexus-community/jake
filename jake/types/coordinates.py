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


class Coordinates(object):
    def __init__(self):
        self._coordinates = []

    def add_coordinate(self, coordinate):
        self._coordinates.append(coordinate)

    def get_coordinates(self):
        return self._coordinates

    def get_coordinates_as_json(self):
        coordinates = {}
        coordinates['coordinates'] = self._coordinates
        return json.dumps(coordinates)
