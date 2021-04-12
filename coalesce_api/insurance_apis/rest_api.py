import requests

from coalesce_api.insurance_apis.api_interface import APIInterface
from coalesce_api.insurance_apis.api_factory import register_type
from coalesce_api.insurance_apis.invalid_method_error import InvalidMethodError
from coalesce_api.insurance_apis.invalid_response_error import InvalidResponseError


@register_type
class RestAPI(APIInterface):
    allowed_methods = { 'GET', 'POST', 'PUT', 'DELETE' }
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_from_api(self, path='/', method='GET', **kwargs):
        if method not in self.allowed_methods:
            raise InvalidMethodError(path, method)
        url = f'{self.base_url}{path}'
        print(url)
        response = requests.request(method, url, **kwargs)
        if response.status_code >= 400:
            raise InvalidResponseError(path, response.status_code)
        response_data = response.json()
        return response_data
    
    @classmethod
    def get_type(cls):
        return 'REST', cls
