import unittest
import requests
from unittest.mock import patch
from unittest.mock import Mock
from requests import Response

from coalesce_api.insurance_apis.invalid_method_error import InvalidMethodError
from coalesce_api.insurance_apis.invalid_response_error import InvalidResponseError
from coalesce_api.insurance_apis.rest_api import RestAPIClient


def create_success_call():
  dummy_response = Response()
  dummy_response.status_code = 200
  dummy_response.json = lambda: {"success": True}
  return dummy_response


def create_failed_call():
  dummy_response = Response()
  dummy_response.status_code = 500
  return dummy_response


class TestRestAPIClient(unittest.TestCase):
  @patch("requests.request", return_value=create_success_call())
  def test_should_fetch_from_api(self, *args):
    mocked_request = args[0]
    client = RestAPIClient("dummy_url")
    response = client.fetch_from_api()
    mocked_request.assert_called_with("GET", "dummy_url")
    self.assertTrue(response["success"])
  
  @patch("requests.request", return_value=create_failed_call())
  def test_should_fail_call_to_api(self, *args):
    client = RestAPIClient("dummy_url")
    with self.assertRaises(InvalidResponseError):
      client.fetch_from_api()
  
  def test_should_fail_with_invalid_method(self):
    client = RestAPIClient("dummy_url")
    with self.assertRaises(InvalidMethodError):
      client.fetch_from_api(method="N/A")
  
  @patch("requests.request", return_value=create_success_call())
  def test_should_fetch_insurance_data(self, *args):
    mocked_request = args[0]
    client = RestAPIClient("dummy_url")
    mock_id = 1
    response = client.get_insurance_data(mock_id)
    mocked_request.assert_called_with("GET", f"dummy_url?member_id={mock_id}")
    self.assertTrue(response["success"])

  def test_should_fail_to_fetch_insurance_data_without_id(self, *args):
    client = RestAPIClient("dummy_url")
    with self.assertRaises(ValueError):
      response = client.get_insurance_data(None)
