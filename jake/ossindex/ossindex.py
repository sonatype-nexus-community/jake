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
import ast

from typing import List
from datetime import datetime, timedelta
from dateutil.parser import parse
from tinydb import TinyDB, Query
from pathlib import Path
from jake.parse.parse import Coordinates
from jake.types.results_decoder import ResultsDecoder
from jake.types.coordinateresults import CoordinateResults

class OssIndex(object):
    def __init__(self, url='https://ossindex.sonatype.org/api/v3/component-report', headers={'Content-type': 'application/json', 'User-Agent': 'jake'}, cache_location=''):
        self._url = url
        self._headers = headers
        self._log = logging.getLogger('jake')
        self._maxcoords = 128
        if cache_location == '':
            home = str(Path.home())
            dir_oss = home + "/.ossindex/"
        else:
            dir_oss = cache_location + "/.ossindex/"
        if not Path(dir_oss).exists():
            Path(dir_oss).mkdir(parents=True, exist_ok=True)
        self._db = TinyDB(dir_oss + "jake.json")

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

    def callOSSIndex(self, purls: Coordinates):
        self._log.debug(purls)

        results = []

        (purls, results) = self.getPurlsAndResultsFromCache(purls)

        chunk_purls = self.chunk(purls)
        for purls in chunk_purls:
            data = {}
            data["coordinates"] = purls
            response = requests.post(self.get_url(), data=json.dumps(data), headers=self.get_headers())
            if response.status_code == 200:
                first_results = json.loads(response.text, cls=ResultsDecoder)
            else:
                return None
            results.extend(first_results)

        (cached, num_cached) = self.maybeInsertIntoCache(results)
        self._log.debug("Cached: " + str(cached) + " num_cached: " + str(num_cached))
        return results

    def maybeInsertIntoCache(self, results: List[CoordinateResults]):
        Coordinate = Query()
        num_cached = 0
        cached = False
        for coordinate in results:
            mydatetime = datetime.now()
            twelvelater = mydatetime + timedelta(hours=12)
            result = self._db.search(Coordinate.purl == coordinate.getCoordinates())
            if len(result) is 0:
                self._db.insert({'purl': coordinate.getCoordinates(), 'response': coordinate.toJSON(), 'ttl': twelvelater.isoformat()})
                self._log.debug("Coordinate inserted into cache")
                num_cached += 1
                cached = True
            else:
                timetolive = parse(result[0]['ttl'])
                if mydatetime > timetolive:
                    self._db.update({'response': coordinate.toJSON(), 'ttl': twelvelater.isoformat()}, doc_ids=[result[0].doc_id])
                    self._log.debug("Coordinate updated in cache because TTL expired")
                    num_cached += 1
                    cached = True

        return (cached, num_cached)

    def getPurlsAndResultsFromCache(self, purls: Coordinates):
        valid = isinstance(purls, Coordinates)
        if not valid:
            return (None, None)
        new_purls = Coordinates()
        results = []
        Coordinate = Query()
        for purl in purls.get_coordinates():
            mydatetime = datetime.now()
            result = self._db.search(Coordinate.purl == purl)
            if len(result) is 0 or parse(result[0]['ttl']) < mydatetime:
                new_purls.add_coordinate(purl)
            else:
                results.append(json.loads(result[0]['response'], cls=ResultsDecoder))
        return (new_purls, results)

    def cleanCache(self):
        self._db.purge()
        return self._db.all()