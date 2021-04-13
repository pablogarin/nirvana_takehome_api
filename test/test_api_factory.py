import unittest

from coalesce_api.insurance_apis.api_factory import APIFactory
from coalesce_api.insurance_apis.api_factory import api_types
from coalesce_api.insurance_apis.api_factory import register_type
from coalesce_api.insurance_apis.api_interface import APIInterface
from coalesce_api.insurance_apis.api_type_error import APITypeError
from coalesce_api.insurance_apis.duplicate_interface_error import DuplicateInterfaceError
from coalesce_api.insurance_apis.invalid_url_error import InvalidURLError
from coalesce_api.insurance_apis.rest_api import RestAPIClient


class DummyAPI(APIInterface):
  def fetch_from_api(self, path):
    pass
  
  def get_insurance_data(self, member_id: int):
    pass

  @classmethod
  def get_type(cls):
    return 'REST', cls


class TestAPIFactory(unittest.TestCase):
  def test_should_create_a_rest_instance(self):
    af = APIFactory()
    api_client = af.create_api('dummy_url', 'REST')

  def test_should_fail_when_url_is_not_provided(self):
    af = APIFactory()
    with self.assertRaises(InvalidURLError):
      af.create_api()
  
  def test_should_fail_when_type_doesnt_exists(self):
    af = APIFactory()
    with self.assertRaises(APITypeError):
      af.create_api('dummy_url', 'NON_EXISTENT')
  
  def test_should_register_new_api(self):
    pass

  def test_should_not_allow_duplicate_interfaces(self):
    with self.assertRaises(DuplicateInterfaceError):
      register_type(DummyAPI)

  def test_should_not_add_interface_twice(self):
    prev_len = len(api_types.items())
    register_type(RestAPIClient)
    self.assertEqual(len(api_types.items()), prev_len)