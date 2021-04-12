import json
import flask
from flask_restful import reqparse
from flask_restful import Resource

from coalesce_api.insurance_apis.api_factory import APIFactory
from coalesce_api.insurance_apis.invalid_response_error import InvalidResponseError
from coalesce_api.strategies.context_handler import ContextHandler


class InsuranceInfo(Resource):
    def __init__(self, ctx: ContextHandler):
        self.ctx = ctx
        api_factory = APIFactory()
        rest_urls = [
          "http://localhost:3001/api1",
          "http://localhost:3001/api2",
          "http://localhost:3001/api3",
        ]
        self.api_clients = [ api_factory.create_api(url, "REST") for url in rest_urls ]
        self.fields = ["deductible", "stop_loss", "oop_max"]

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("member_id", type=int, required=True)
        args = parser.parse_args()
        id_ = args["member_id"]
        print(f"Fetching data for id {id_}.")
        try:
          responses = []
          for api_client in self.api_clients:
            response = api_client.get_insurance_data(id_)
            responses.append(response)
          processed_data = self.ctx.execute(
            payload=responses,
            fields=self.fields)
          return processed_data
        except InvalidResponseError as e:
          response = flask.make_response(e.to_json())
          response.headers['content-type'] = 'application/json'
          response.status_code = e.status_code
          return response
