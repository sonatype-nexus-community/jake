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
import requests
import logging

class OssIndex(object):
    def __init__(self, url='https://ossindex.sonatype.org/api/v3/component-report', headers={'Content-type': 'application/json', 'User-Agent': 'jake'}):
        self._url = url
        self._headers = headers
        self._log = logging.getLogger('jake')

    def get_url(self):
        return self._url

    def get_headers(self):
        return self._headers

    def callOSSIndex(self, purls):
        self._log.debug(purls)

        response = requests.post(self.get_url(), data=purls, headers=self.get_headers())

        self._log.debug(response.status_code)

        return response 
