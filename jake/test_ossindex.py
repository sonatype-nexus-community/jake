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
import unittest
import json
from unittest.mock import patch
from pathlib import Path
from tinydb import TinyDB, Query
from dateutil.parser import parse
from datetime import timedelta
from typing import List

from jake.ossindex.ossindex import OssIndex
from jake.parse.parse import Parse
from jake.parse.coordinates import Coordinates
from jake.types.coordinateresults import CoordinateResults
from jake.types.results_decoder import ResultsDecoder

class TestOssIndex(unittest.TestCase):
    def setUp(self):
        self.func = OssIndex(url="http://blahblah", headers={"thing": "thing", "anotherthing": "anotherthing"}, cache_location="/tmp")
        self.parse = Parse()
    
    def tearDown(self):
        self.func.closeDB()
        if Path('/tmp/.ossindex/jake.json').exists():
            Path('/tmp/.ossindex/jake.json').unlink()
    
    def test_getHeaders(self):
        self.assertEqual(self.func.get_headers(), {"thing": "thing", "anotherthing": "anotherthing"})

    def test_getUrl(self):
        self.assertEqual(self.func.get_url(), "http://blahblah")

    def get_fakePurls(self):
        fakePurls = Coordinates()
        fakePurls.add_coordinate("pkg:conda/thing1")
        fakePurls.add_coordinate("pkg:conda/thing2")
        fakePurls.add_coordinate("pkg:conda/thing3")
        return fakePurls
    
    def get_fakeActualPurls(self):
        fakeActualPurls = Coordinates()
        fakeActualPurls.add_coordinate("pkg:conda/_ipyw_jlab_nb_ext_conf@0.1.0")
        return fakeActualPurls
    
    @patch('jake.ossindex.ossindex.requests.post')
    def test_callGetDependenciesReturnsPurls(self, mock_post):
        fn = Path(__file__).parent / "ossindexresponse.txt"
        with open(fn, "r") as stdin:
            mock_result = stdin.read().replace("'", '"')
            mock_post.return_value.status_code = 200
            mock_post.return_value.text = mock_result
            response = self.func.callOSSIndex(self.get_fakePurls())
        self.assertEqual(len(response), 46)
        self.assertEqual(response[0].getCoordinates(), "pkg:conda/astroid@2.3.1")

    @patch('jake.ossindex.ossindex.requests.post')
    def test_callOSSIndex_PostReturnsError(self, mock_post):
        mock_post.return_value.status_code = 404
        mock_post.return_value.text = "yadda"
        response = self.func.callOSSIndex(self.get_fakePurls())
        self.assertEqual(response, None)

    def test_chunk(self):
        fn = Path(__file__).parent / "condalistoutput.txt"
        with open(fn, "r") as stdin:
            purls = self.parse.getDependenciesFromStdin(stdin)
            actual_result = self.func.chunk(purls)
        self.assertEqual(len(actual_result), 3)
        self.assertEqual(len(actual_result[0]), 128)
        self.assertEqual(actual_result[0][0], "pkg:conda/_ipyw_jlab_nb_ext_conf@0.1.0")
        self.assertEqual(actual_result[1][0], "pkg:conda/mistune@0.8.4")
        self.assertEqual(actual_result[2][0], "pkg:conda/yaml@0.1.7")

    def test_insertIntoCache(self):
        fn = Path(__file__).parent / "ossindexresponse.txt"
        with open(fn, "r") as stdin:
            response = json.loads(stdin.read().replace("'", '"'), cls=ResultsDecoder)
            (cached, num_cached) = self.func.maybeInsertIntoCache(response)
        self.assertEqual(num_cached, 46)
        self.assertEqual(cached, True)

    def test_insertIntoCacheDoesNotDuplicate(self):
        fn = Path(__file__).parent / "ossindexresponse.txt"
        with open(fn, "r") as stdin:
            response = json.loads(stdin.read().replace("'", '"'), cls=ResultsDecoder)
            self.func.maybeInsertIntoCache(response)
            (cached, num_cached) = self.func.maybeInsertIntoCache(response)
        self.assertEqual(num_cached, 0)
        self.assertEqual(cached, False)

    def test_insertIntoCacheExpiredTTL(self):
        db = TinyDB('/tmp/.ossindex/jake.json')
        Coordinates = Query()
        response = self.stringToCoordinatesResult("[{'coordinates': 'pkg:conda/astroid@2.3.1', 'reference': 'https://ossindex.sonatype.org/component/pkg:conda/astroid@2.3.1', 'vulnerabilities': []}]")
        self.func.maybeInsertIntoCache(response)
        resultExpired = db.search(Coordinates.purl == "pkg:conda/astroid@2.3.1")
        timeUnwind = parse(resultExpired[0]['ttl']) - timedelta(hours=13)
        db.update({'ttl': timeUnwind.isoformat()}, Coordinates.purl == "pkg:conda/astroid@2.3.1")
        
        nextResponse = self.stringToCoordinatesResult("[{'coordinates': 'pkg:conda/astroid@2.3.1', 'reference': 'https://ossindex.sonatype.org/component/pkg:conda/astroid@2.3.1', 'vulnerabilities': []}]")
        (cached, num_cached) = self.func.maybeInsertIntoCache(nextResponse)
        self.assertEqual(cached, True)
        self.assertEqual(num_cached, 1)
        db.close()

    def test_getPurlsFromCache(self):
        self.func.maybeInsertIntoCache(self.stringToCoordinatesResult("[{'coordinates': 'pkg:conda/_ipyw_jlab_nb_ext_conf@0.1.0', 'reference': 'https://ossindex.sonatype.org/component/pkg:conda/_ipyw_jlab_nb_ext_conf@0.1.0', 'vulnerabilities': []}, {'coordinates': 'pkg:conda/alabaster@0.7.12', 'reference': 'https://ossindex.sonatype.org/component/pkg:conda/alabaster@0.7.12', 'vulnerabilities': []}, {'coordinates': 'pkg:conda/anaconda@2019.07', 'reference': 'https://ossindex.sonatype.org/component/pkg:conda/anaconda@2019.07', 'vulnerabilities': []}]"))
        (new_purls, results) = self.func.getPurlsAndResultsFromCache(self.get_fakeActualPurls())
        self.assertEqual(isinstance(results, List), True)
        self.assertEqual(isinstance(results[0], CoordinateResults), True)
        self.assertEqual(results[0].getCoordinates(), "pkg:conda/_ipyw_jlab_nb_ext_conf@0.1.0")
        self.assertEqual(results[0].getReference(), "https://ossindex.sonatype.org/component/pkg:conda/_ipyw_jlab_nb_ext_conf@0.1.0")
        self.assertEqual(isinstance(results[0].getVulnerabilities(), List), True)
        self.assertEqual(len(new_purls.get_coordinates()), 0)
        self.assertEqual(isinstance(new_purls, Coordinates), True)

    def test_getPurlsFromCacheWithCacheMiss(self):
        self.func.maybeInsertIntoCache(self.stringToCoordinatesResult("[{'coordinates': 'pkg:conda/_ipyw_jlab_nb_ext_conf@0.1.0', 'reference': 'https://ossindex.sonatype.org/component/pkg:conda/_ipyw_jlab_nb_ext_conf@0.1.0', 'vulnerabilities': []}]"))
        fake_purls = self.get_fakeActualPurls()
        fake_purls.add_coordinate("pkg:conda/alabaster@0.7.12")
        (new_purls, results) = self.func.getPurlsAndResultsFromCache(fake_purls)
        self.assertEqual(len(new_purls.get_coordinates()), 1)
        self.assertEqual(isinstance(new_purls, Coordinates), True)
        self.assertEqual(isinstance(results, List), True)
        self.assertEqual(isinstance(results[0], CoordinateResults), True)
        self.assertEqual(isinstance(results[0].getVulnerabilities(), List), True)
        self.assertEqual(results[0].getCoordinates(), "pkg:conda/_ipyw_jlab_nb_ext_conf@0.1.0")
        self.assertEqual(results[0].getReference(), "https://ossindex.sonatype.org/component/pkg:conda/_ipyw_jlab_nb_ext_conf@0.1.0")

    def test_getPurlsFromCacheWithNonValidObject(self):
        (new_purls, results) = self.func.getPurlsAndResultsFromCache("bad data")
        self.assertEqual(new_purls, None)
        self.assertEqual(results, None)

    def test_cleanWipesDB(self):
        self.func.maybeInsertIntoCache(self.stringToCoordinatesResult("[{'coordinates': 'pkg:conda/_ipyw_jlab_nb_ext_conf@0.1.0', 'reference': 'https://ossindex.sonatype.org/component/pkg:conda/_ipyw_jlab_nb_ext_conf@0.1.0', 'vulnerabilities': []}]"))
        self.assertEqual(self.func.cleanCache(), True)

    def stringToCoordinatesResult(self, string):
        return json.loads(string.replace("'", '"'), cls=ResultsDecoder)
