import unittest
import json

from coalesce_api.insurance_apis.invalid_method_error import InvalidMethodError
from coalesce_api.insurance_apis.invalid_response_error import InvalidResponseError


class TestErrors(unittest.TestCase):
  def test_should_print_method_error_as_json(self):
    mock_error_dict = {
      "success": False,
      "message": 'mock_message',
      "method": 'mock_method',
      "url": 'mock_url'
    }
    err = InvalidMethodError(
      mock_error_dict["url"],
      mock_error_dict["method"],
      message=mock_error_dict["message"])
    self.assertEqual(err.to_json(), json.dumps(mock_error_dict))

  def test_should_print_response_error_as_json(self):
    mock_error_dict = {
      "success": False,
      "message": 'mock_message',
      "code": 500,
      "url": 'mock_url'
    }
    err = InvalidResponseError(
      mock_error_dict["url"],
      mock_error_dict["code"],
      message=mock_error_dict["message"])
    self.assertEqual(err.to_json(), json.dumps(mock_error_dict))

