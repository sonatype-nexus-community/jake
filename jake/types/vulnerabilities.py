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


class Vulnerabilities(object):
    def __init__(self):
        self.id = ""
        self.title = ""
        self.description = ""
        self.cvssScore = ""
        self.cvssVector = None
        self.cve = ""
        self.reference = ""

    def add_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def add_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def add_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def add_cvssScore(self, cvssScore):
        self.cvssScore = cvssScore

    def get_cvssScore(self):
        return self.cvssScore

    def add_cvssVector(self, cvssVector):
        if cvssVector is not None:
            self.cvssVector = cvssVector

    def get_cvssVector(self):
        return self.cvssVector

    def add_cve(self, cve):
        self.cve = cve

    def get_cve(self):
        return self.cve

    def add_reference(self, reference):
        self.reference = reference

    def get_reference(self):
        return self.reference
