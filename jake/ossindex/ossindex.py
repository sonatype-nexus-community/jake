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
import json

class OssIndex(object):
    def __init__(self, url='https://ossindex.sonatype.org/api/v3/component-report', headers={'Content-type': 'application/json', 'User-Agent': 'jake'}):
        self._url = url
        self._headers = headers
        self._log = logging.getLogger('jake')
        self._maxcoords = 128

    def get_url(self):
        return self._url

    def get_headers(self):
        return self._headers

    def chunk(self, purls):
        chunks = []
        divided = []
        length = len(purls.get_coordinates())
        num_chunks = length // self._maxcoords
        if length % self._maxcoords > 0:
            num_chunks += 1
        start_index = 0
        end_index = self._maxcoords
        for i in range(0, num_chunks):
            if i == (num_chunks - 1):
                divided = purls.get_coordinates()[start_index:length]
            else:    
                divided = purls.get_coordinates()[start_index:end_index]
                start_index = end_index
                end_index += end_index
            chunks.append(divided)
        return chunks

    def callOSSIndex(self, purls):
        self._log.debug(purls)

        chunk_purls = self.chunk(purls)
        results = []
        for purls in chunk_purls:
            data = {}
            data["coordinates"] = purls
            response = requests.post(self.get_url(), data=json.dumps(data), headers=self.get_headers())
            if response.status_code == 200:
                first_results = json.loads(response.text)
            else:
                return None
            results.extend(first_results)
        return results
