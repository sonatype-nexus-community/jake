"""vulnerabilities.py creates a Vulnerabilities type object"""
# pylint: disable=C0103
# pylint: disable=W0622
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


class Vulnerabilities():
  """creates a Vulnerabilities type object"""
  def __init__(self):
    self.id = ""
    self.title = ""
    self.description = ""
    self.cvss_score = ""
    self.cvss_vector = None
    self.cve = ""
    self.reference = ""

  def set_id(self, id):
    """sets vuln_id for Vulnerabilities object"""
    self.id = id

  def get_id(self):
    """gets vuln_id for Vulnerabilities object"""
    return self.id

  def set_title(self, title):
    """sets title for Vulnerabilities object"""
    self.title = title

  def get_title(self):
    """gets title for Vulnerabilities object"""
    return self.title

  def set_description(self, description):
    """sets description for Vulnerabilities object"""
    self.description = description

  def get_description(self):
    """gets description for Vulnerabilities object"""
    return self.description

  def set_cvss_score(self, cvss_score):
    """sets cvss_score for Vulnerabilities object"""
    self.cvss_score = cvss_score

  def get_cvss_score(self):
    """gets cvss_score for Vulnerabilities object"""
    return self.cvss_score

  def set_cvss_vector(self, cvss_vector):
    """sets cvss_vector Vulnerabilities object if it exists"""
    if cvss_vector is not None:
      self.cvss_vector = cvss_vector

  def get_cvss_vector(self):
    """gets cvss_vector for Vulnerabilities object"""
    return self.cvss_vector

  def set_cve(self, cve):
    """sets cve for Vulnerabilities object"""
    self.cve = cve

  def get_cve(self):
    """gets cve for Vulnerabilities object"""
    return self.cve

  def set_reference(self, reference):
    """sets reference for Vulnerabilities object"""
    self.reference = reference

  def get_reference(self):
    """gets reference for Vulnerabilities object"""
    return self.reference
