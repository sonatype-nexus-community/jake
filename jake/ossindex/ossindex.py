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

"""ossindex.py makes a request to OSSIndex"""
import logging
import json
import datetime as DT

from typing import List
from datetime import datetime, timedelta
from pathlib import Path
from tinydb import TinyDB, Query

import requests

from ..types.coordinates import Coordinates
from ..types.results_decoder import ResultsDecoder
from ..types.coordinateresults import CoordinateResults
from ..config.config import Config

DEFAULT_HEADERS = {
    'Content-type': 'application/vnd.ossindex.component-report-request.v1+json',
    'User-Agent': 'jake'}

class OssIndex():
  """ossindex.py makes a request to OSSIndex"""
  def __init__(self,
               url='https://ossindex.sonatype.org/api/v3/component-report',
               cache_location=''):
    self._url = url
    self._headers = DEFAULT_HEADERS
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
    """gets url to use for OSSIndex request"""
    return self._url

  def get_headers(self):
    """gets headers to use for OSSIndex request"""
    return self._headers

  def chunk(self, coords: Coordinates):
    """chunks up purls array into 128-purl subarrays"""
    chunks = []
    divided = []
    length = len(coords.get_coordinates())
    num_chunks = length // self._maxcoords
    if length % self._maxcoords > 0:
      num_chunks += 1
    start_index = 0
    end_index = self._maxcoords
    for i in range(0, num_chunks):
      if i == (num_chunks - 1):
        divided = coords.get_purls()[start_index:length]
      else:
        divided = coords.get_purls()[start_index:end_index]
        start_index = end_index
        end_index += end_index
      chunks.append(divided)
    return chunks

  def call_ossindex(self, coords: Coordinates) -> (list):
    """makes a request to OSSIndex"""
    self._log.debug("Purls received, total purls before chunk: %s",
                    len(coords.get_coordinates()))

    (coords, results) = self.get_purls_and_results_from_cache(coords)

    self._log.debug("Purls checked against cache, total purls remaining to "
                    "call OSS Index: %s",
                    len(coords.get_coordinates()))

    chunk_purls = self.chunk(coords)
    for purls_chunk in chunk_purls:
      data = {}
      data["coordinates"] = purls_chunk
      config_file = Config()
      if config_file.check_if_config_exists() is False:
        response = requests.post(self.get_url(), data=json.dumps(
            data), headers=self.get_headers())
      else:
        auth = config_file.get_config_from_file(
            ".oss-index-config")

        response = requests.post(self.get_url(),
                                 data=json.dumps(data),
                                 headers=self.get_headers(),
                                 auth=(auth["Username"], auth["Token"]))
      if response.status_code == 200:
        self._log.debug(response.headers)
        first_results = json.loads(response.text, cls=ResultsDecoder)
      else:
        self._log.debug("Response failed, status: %s",
                        response.status_code)
        self._log.debug("Failure reason if any: %s", response.reason)
        self._log.debug("Failure text if any: %s", response.text)
        return None
      results.extend(first_results)

    (cached, num_cached) = self.maybe_insert_into_cache(results)
    self._log.debug("Cached: <%s> num_cached: <%s>", cached, num_cached)
    return results

  def maybe_insert_into_cache(self, results: List[CoordinateResults]):
    """checks to see if result is in cache and if not, stores it"""
    coordinate_query = Query()
    num_cached = 0
    cached = False
    for coordinate in results:
      mydatetime = datetime.now()
      twelvelater = mydatetime + timedelta(hours=12)
      result = self._db.search(
          coordinate_query.purl == coordinate.get_coordinates())
      if len(result) == 0:
        self._db.insert({'purl': coordinate.get_coordinates(),
                         'response': coordinate.to_json(),
                         'ttl': twelvelater.isoformat()})
        self._log.debug(
            "Coordinate inserted into cache: <%s>",
            coordinate.get_coordinates())
        num_cached += 1
        cached = True
      else:
        timetolive = DT.datetime.strptime(
          result[0]['ttl'],
          '%Y-%m-%dT%H:%M:%S.%f'
          )
        if mydatetime > timetolive:
          self._db.update({'response': coordinate.to_json(),
                           'ttl': twelvelater.isoformat()},
                          doc_ids=[result[0].doc_id])
          self._log.debug(
              "Coordinate: <%s> updated in cache because TTL"
              " expired",
              coordinate.get_coordinates())
          num_cached += 1
          cached = True

    return (cached, num_cached)

  def get_purls_and_results_from_cache(self, purls: Coordinates) -> (Coordinates, list):
    """get cached purls and results from cache"""
    valid = isinstance(purls, Coordinates)
    if not valid:
      return (None, None)
    new_purls = Coordinates()
    results = []
    coordinate_query = Query()
    for coordinate, purl in purls.get_coordinates().items():
      mydatetime = datetime.now()
      result = self._db.search(coordinate_query.purl == purl)
      if len(result) == 0 or DT.datetime.strptime(
        result[0]['ttl'],
        '%Y-%m-%dT%H:%M:%S.%f'
        ) < mydatetime:
        new_purls.add_coordinate(coordinate[0], coordinate[1], coordinate[2])
      else:
        results.append(json.loads(
            result[0]['response'], cls=ResultsDecoder))
    return (new_purls, results)

  def clean_cache(self):
    """removes all documents from the table"""
    self._db.purge()
    return True

  def close_db(self):
    """closes connection to TinyDB"""
    self._db.close()
