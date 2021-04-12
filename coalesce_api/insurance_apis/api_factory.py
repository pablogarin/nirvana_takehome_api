from coalesce_api.insurance_apis.api_interface import APIInterface
from coalesce_api.insurance_apis.api_type_error import APITypeError
from coalesce_api.insurance_apis.invalid_url_error import InvalidURLError
from coalesce_api.insurance_apis.duplicate_interface_error import DuplicateInterfaceError


api_types = {}

def register_type(interface: APIInterface):
  type_, cl = interface.get_type()
  if type_ in api_types:
    if api_types[type_] != cl:
      raise DuplicateInterfaceError()
    return
  api_types[type_] = cl

class APIFactory(object):
  def create_api(self, url=None: str, type_:str = 'REST', *args, **kwargs) -> APIInterface:
    if not url:
      raise InvalidURLError()
    if type_ not in api_types:
      raise APITypeError()
    api = api_types[type_](url, *args, **kwargs)
    return api
