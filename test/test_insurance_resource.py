import unittest
import json
from unittest.mock import patch
from unittest.mock import MagicMock
from unittest.mock import PropertyMock
from requests import Response

from coalesce_api.strategies.context_handler import ContextHandler
from coalesce_api.resources.insurance_info import InsuranceInfo


def get_current_result():
  responses = [
    {
      "deductible": 1000,
      "stop_loss": 1000,
      "oop_max": 1000
    },
    {
      "deductible": 2000,
      "stop_loss": 2000,
      "oop_max": 2000
    },
    {
      "deductible": 6000,
      "stop_loss": 6000,
      "oop_max": 6000
    }
  ]
  i = 0
  while True:
    yield responses[i]
    i += 1
    if i >= len(responses):
      i = 0


results_generator = get_current_result()


def create_success_response(method, url):
  result = next(results_generator)
  dummy_response = Response()
  dummy_response.status_code = 200
  dummy_response.json = lambda: result
  return dummy_response


def create_failed_response():
  dummy_response = Response()
  dummy_response.status_code = 500
  return dummy_response


class DummyResponse(object):
  def __init__(self, data):
    self.data = data
    self.headers = {}


query_params = {"member_id": 1}


class TestInsuranceInfo(unittest.TestCase):
  @patch("requests.request", new=create_success_response)
  @patch("flask_restful.reqparse.RequestParser.add_argument")
  @patch("flask_restful.reqparse.RequestParser.parse_args", return_value=query_params)
  def test_should_return_averaged_fields(self, *args):
    mocked_parse_args = args[0]
    mocked_add_argument = args[1]
    ctx = ContextHandler("average")
    resource = InsuranceInfo(ctx)
    avg = resource.get()
    mocked_add_argument.assert_called_once_with("member_id", type=int, required=True)
    mocked_parse_args.assert_called_once()
    self.assertIn("deductible", avg)
    self.assertIn("stop_loss", avg)
    self.assertIn("oop_max", avg)
    self.assertEqual(avg["deductible"], 3000.0) # asumes 3 api calls
    self.assertEqual(avg["stop_loss"], 3000.0) # asumes 3 api calls
    self.assertEqual(avg["oop_max"], 3000.0) # asumes 3 api calls

  @patch("requests.request", return_value=create_failed_response())
  @patch("flask.make_response", new=lambda data: DummyResponse(data))
  @patch("flask_restful.reqparse.RequestParser.add_argument")
  @patch("flask_restful.reqparse.RequestParser.parse_args", return_value=query_params)
  def test_should_fail_with_server_error(self, *args):
    ctx = ContextHandler("average")
    resource = InsuranceInfo(ctx)
    failure = resource.get()
    self.assertEqual(failure.status_code, 500)
    self.assertEqual(failure.headers["content-type"], "application/json")
    parsed_data = json.loads(failure.data)
    self.assertIn("success", parsed_data)
    self.assertFalse(parsed_data["success"])
