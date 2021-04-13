import requests

from coalesce_api.insurance_apis.api_interface import APIInterface
from coalesce_api.insurance_apis.api_factory import register_type
from coalesce_api.insurance_apis.invalid_method_error import InvalidMethodError
from coalesce_api.insurance_apis.invalid_response_error import InvalidResponseError


@register_type
class RestAPIClient(APIInterface):
    allowed_methods = { 'GET', 'POST', 'PUT', 'DELETE' }
    def __init__(self, url):
        self.url = url

    def fetch_from_api(self, url: str = None, method: str = 'GET', **kwargs):
        if method not in self.allowed_methods:
            raise InvalidMethodError(url, method)
        if not url:
          url = self.url
        response = requests.request(method, url, **kwargs)
        if response.status_code >= 400:
            raise InvalidResponseError(url, response.status_code)
        response_data = response.json()
        return response_data
    
    def get_insurance_data(self, id_: int):
      if not id_:
        raise ValueError('You must provide a valid member id')
      url = f'{self.url}?member_id={id_}'
      data = self.fetch_from_api(url=url)
      return data
    
    @classmethod
    def get_type(cls):
      return 'REST', cls
