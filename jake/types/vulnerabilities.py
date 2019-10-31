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

class Vulnerabilities(object):
  def __init__(self):
    self._id = ""
    self._title = ""
    self._description = ""
    self._cvssScore = ""
    self._cvssVector = ""
    self._cve = ""
    self._reference = ""
    
  def add_id(self, id):
    self._id = id

  def get_id(self):
    return self._id

  def add_title(self, title):
    self._title = title

  def get_title(self):
    return self._title

  def add_description(self, description):
    self._description = description

  def get_description(self):
    return self._description

  def add_cvssScore(self, cvssScore):
    self._cvssScore = cvssScore

  def get_cvssScore(self):
    return self._cvssScore
