from flask import Flask
from flask_restful import Api, reqparse

from coalesce_api.resources.insurance_info import InsuranceInfo
from coalesce_api.strategies.context_handler import ContextHandler


def create_flask_app(ctx: ContextHandler):
  print("Starting API...")
  app = Flask(__name__)
  api = Api(app)
  api.add_resource(InsuranceInfo, "/insurance-info", resource_class_kwargs={"ctx": ctx})
  print("API started!")
  return app
