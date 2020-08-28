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

"""test_ossindex.py audits the call to OSSIndex"""
import unittest
import json
import datetime as DT

from unittest.mock import patch
from pathlib import Path
from datetime import timedelta
from tinydb import TinyDB, Query

from ..ossindex.ossindex import OssIndex
from ..parse.parse import Parse
from ..types.coordinates import Coordinates
from ..types.coordinateresults import CoordinateResults
from ..types.results_decoder import ResultsDecoder
from ..types.vulnerabilities import Vulnerabilities


class TestOssIndex(unittest.TestCase):
  """TestOssIndex audits the call to OSSIndex"""
  def setUp(self):
    self.func = OssIndex(url="http://blahblah",
                         cache_location="/tmp")
    self.parse = Parse()

  def tearDown(self):
    self.func.close_db()
    if Path('/tmp/.ossindex/jake.json').exists():
      Path('/tmp/.ossindex/jake.json').unlink()

  def test_get_headers(self):
    """test_get_headers ensures headers are being retrieved correctly"""
    self.assertEqual(self.func.get_headers(), {
        "Content-type":
        "application/vnd.ossindex.component-report-request.v1+json",
        "User-Agent":
        "jake"})

  def test_get_url(self):
    """test_get_url ensures url is being retrieved correctly"""
    self.assertEqual(self.func.get_url(), "http://blahblah")

  @staticmethod
  def get_fake_purls():
    """get_fake_purls is a helper function that creates a fake Coordinate"""
    fake_purls = Coordinates()
    fake_purls.add_coordinate('thing', '1.1', 'conda')
    fake_purls.add_coordinate('thing', '1.2', 'conda')
    fake_purls.add_coordinate('thing', '1.3', 'conda')
    return fake_purls

  @staticmethod
  def get_fake_actual_purls():
    """get_fake_actual_purls is a helper function that creates a
    fake Coordinate with realistic data"""
    fake_actual_purls = Coordinates()
    fake_actual_purls.add_coordinate('pycrypto', '2.6.1', 'conda')
    return fake_actual_purls

  @patch('jake.ossindex.ossindex.requests.post')
  def test_call_get_dependencies_returns_purls(self, mock_post):
    """test_call_get_dependencies_returns_purls mocks a call to OSSIndex
    and ensures that that calls to OSSIndex return properly formated purls
    as Coordinates or Vulnerabilities type objects"""
    file = Path(__file__).parent / "ossindexresponse.txt"
    with open(file, "r") as stdin:
      mock_result = stdin.read()
      mock_post.return_value.status_code = 200
      mock_post.return_value.text = mock_result
      response = self.func.call_ossindex(self.get_fake_purls())
    self.assertEqual(len(response), 32)
    self.assertEqual(response[0].get_coordinates(),
                     "pkg:conda/pycrypto@2.6.1")
    self.assertEqual(response[18].get_coordinates(),
                     "pkg:conda/python@3.7.3")
    self.assertEqual(isinstance(
        response[18].get_vulnerabilities()[0], Vulnerabilities), True)
    self.assertEqual(response[18].get_vulnerabilities()[
        0].get_id(), "156d71e4-6ed5-4d5f-ae47-7d57be01d387")

  @patch('jake.ossindex.ossindex.requests.post')
  def test_call_ossindex_post_returns_error(self, mock_post):
    """test_call_ossindex_post_returns_error mocks a failed call to OSSIndex
    and ensures the error is handled"""
    mock_post.return_value.status_code = 404
    mock_post.return_value.text = "yadda"
    response = self.func.call_ossindex(self.get_fake_purls())
    self.assertEqual(response, None)

  def test_chunk(self):
    """test_chunk ensures the chunk method is splitting responses with more
    than 128 purl results into 128-purl chunks"""
    file = Path(__file__).parent / "condalistoutput.txt"
    with open(file, "r") as stdin:
      purls = self.parse.get_deps_stdin(stdin)
      actual_result = self.func.chunk(purls)
    self.assertEqual(len(actual_result), 3)
    self.assertEqual(len(actual_result[0]), 128)
    self.assertEqual(actual_result[0][0],
                     "pkg:conda/_ipyw_jlab_nb_ext_conf@0.1.0")
    self.assertEqual(actual_result[1][0], "pkg:conda/mistune@0.8.4")
    self.assertEqual(actual_result[2][0], "pkg:conda/yaml@0.1.7")

  def test_insert_into_cache(self):
    """test_insert_into_cache ensures the results from an OSSIndex call
    are inserted into cache if they do not yet exist in cache"""
    file = Path(__file__).parent / "ossindexresponse.txt"
    with open(file, "r") as stdin:
      response = json.loads(stdin.read(), cls=ResultsDecoder)
      (cached, num_cached) = self.func.maybe_insert_into_cache(response)
    self.assertEqual(num_cached, 32)
    self.assertEqual(cached, True)

  def test_insert_into_cache_does_not_duplicate(self):
    """test_insert_into_cache_does_not_duplicate ensures that maybe_insert_into_cache
    does not insert results into cache if they exist in cache"""
    file = Path(__file__).parent / "ossindexresponse.txt"
    with open(file, "r") as stdin:
      response = json.loads(stdin.read(), cls=ResultsDecoder)
      self.func.maybe_insert_into_cache(response)
      (cached, num_cached) = self.func.maybe_insert_into_cache(response)
    self.assertEqual(num_cached, 0)
    self.assertEqual(cached, False)

  def test_insert_into_cache_expired_ttl(self):
    """test_insert_into_cache_expired_ttl ensures that maybe_insert_into_cache
    inserts results into cache if the time to live is expired"""
    database = TinyDB('/tmp/.ossindex/jake.json')
    coordinate_query = Query()
    response = self.string_to_coordinatesresult(
        """[{"coordinates":"pkg:conda/pycrypto@2.6.1",
        "reference":"https://ossindex.sonatype.org/component/pkg:conda/pycrypto@2.6.1",
        "vulnerabilities":[]}]""")
    self.func.maybe_insert_into_cache(response)
    result_expired = database.search(
        coordinate_query.purl == "pkg:conda/pycrypto@2.6.1")
    time_unwind = DT.datetime.strptime(
      result_expired[0]['ttl'],
      '%Y-%m-%dT%H:%M:%S.%f') - timedelta(hours=13)
    database.update({'ttl': time_unwind.isoformat()},
                    coordinate_query.purl == "pkg:conda/pycrypto@2.6.1")

    next_response = self.string_to_coordinatesresult(
        """[{"coordinates":"pkg:conda/pycrypto@2.6.1",
        "reference":"https://ossindex.sonatype.org/component/pkg:conda/pycrypto@2.6.1",
        "vulnerabilities":[]}]""")
    (cached, num_cached) = self.func.maybe_insert_into_cache(next_response)
    self.assertEqual(cached, True)
    self.assertEqual(num_cached, 1)
    database.close()

  def test_get_purls_from_cache(self):
    """test_get_purls_from_cache ensures that get_purls_and_results_from_cache
    properly retireves purl objs and results from the cache"""
    self.func.maybe_insert_into_cache(self.string_to_coordinatesresult(
        """[{"coordinates":"pkg:conda/pycrypto@2.6.1",
        "reference":"https://ossindex.sonatype.org/component/pkg:conda/pycrypto@2.6.1",
        "vulnerabilities":[{"id":"156d71e4-6ed5-4d5f-ae47-7d57be01d387",
        "title":"[CVE-2019-16056] jake the snake",
        "cvssScore":0.0,"cve":"CVE-2019-16056",
        "reference":"http://www.wrestling.com"}]}]"""))
    (new_purls, results) = self.func.get_purls_and_results_from_cache(
        self.get_fake_actual_purls())
    self.assertEqual(isinstance(results, list), True)
    self.assertEqual(isinstance(results[0], CoordinateResults), True)
    self.assertEqual(results[0].get_coordinates(),
                     "pkg:conda/pycrypto@2.6.1")
    self.assertEqual(results[0].get_reference(
    ), "https://ossindex.sonatype.org/component/pkg:conda/pycrypto@2.6.1")
    self.assertEqual(isinstance(
        results[0].get_vulnerabilities(), list), True)
    self.assertEqual(isinstance(
        results[0].get_vulnerabilities()[0], Vulnerabilities), True)
    self.assertEqual(results[0].get_vulnerabilities()[
        0].get_id(), "156d71e4-6ed5-4d5f-ae47-7d57be01d387")
    self.assertEqual(results[0].get_vulnerabilities()[
        0].get_cve(), "CVE-2019-16056")
    self.assertEqual(len(new_purls.get_coordinates()), 0)
    self.assertEqual(isinstance(new_purls, Coordinates), True)

  def test_get_purls_from_cache_with_cache_miss(self):
    """ This test ensures that a) results can be added to the cache
    and b) if a purl is not in the cache, that purl is still in the new purls
    that are returned """
    self.func.maybe_insert_into_cache(self.string_to_coordinatesresult(
        """[{"coordinates":"pkg:conda/pycrypto@2.6.1",
        "reference":"https://ossindex.sonatype.org/component/pkg:conda/pycrypto@2.6.1",
        "vulnerabilities":[{"id":"156d71e4-6ed5-4d5f-ae47-7d57be01d387",
        "title":"[CVE-2019-16056] jake the snake",
        "cvssScore":0.0,"cve":"CVE-2019-16056",
        "reference":"http://www.wrestling.com"}]}]"""))
    fake_purls = self.get_fake_actual_purls()
    fake_purls.add_coordinate('alabaster', '0.7.12', 'conda')
    (new_purls, results) = self.func.get_purls_and_results_from_cache(
        fake_purls)
    self.assertEqual(len(new_purls.get_coordinates()), 1)
    self.assertEqual(isinstance(new_purls, Coordinates), True)
    self.assertEqual(isinstance(results, list), True)
    self.assertEqual(isinstance(results[0], CoordinateResults), True)
    self.assertEqual(isinstance(
        results[0].get_vulnerabilities()[0],
        Vulnerabilities), True)
    self.assertEqual(results[0].get_vulnerabilities()[
        0].get_id(), "156d71e4-6ed5-4d5f-ae47-7d57be01d387")
    self.assertEqual(results[0].get_vulnerabilities()[
        0].get_cve(), "CVE-2019-16056")
    self.assertEqual(results[0].get_coordinates(),
                     "pkg:conda/pycrypto@2.6.1")
    self.assertEqual(results[0].get_reference(
    ), "https://ossindex.sonatype.org/component/pkg:conda/pycrypto@2.6.1")
    self.assertEqual(new_purls.get_coordinates()
                     [('alabaster', '0.7.12', 'conda')], "pkg:conda/alabaster@0.7.12")

  def test_get_purls_from_cache_with_non_valid_object(self):
    """test_get_purls_from_cache_with_non_valid_object ensures calls to
    get_purls_and_results_from_cache with improper objects returns None for
    new_purls and results"""
    (new_purls, results) = self.func.get_purls_and_results_from_cache(
        "bad data")
    self.assertEqual(new_purls, None)
    self.assertEqual(results, None)

  def test_clean_cache_wipes_database(self):
    """test_clean_cache_wipes_database ensures calls to clean_cache will
    clear out documents from the database"""
    self.func.maybe_insert_into_cache(self.string_to_coordinatesresult(
        """[{"coordinates":"pkg:conda/pycrypto@2.6.1",
        "reference":"https://ossindex.sonatype.org/component/pkg:conda/pycrypto@2.6.1",
        "vulnerabilities":[]}]"""))
    self.assertEqual(self.func.clean_cache(), True)

  @staticmethod
  def string_to_coordinatesresult(string):
    """string_to_coordinatesresult is a helper function that turns a string
    into a CoordinateResult typed object"""
    return json.loads(string, cls=ResultsDecoder)
