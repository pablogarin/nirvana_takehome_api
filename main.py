import os
import sys
from dotenv import load_dotenv
from coalesce_api import create_flask_app
from coalesce_api.insurance_apis.api_factory import APIFactory
from coalesce_api.insurance_apis.invalid_response_error import InvalidResponseError
from coalesce_api.strategies.context_handler import ContextHandler


load_dotenv()


def main(*args, **kwargs):
  try:
    strategy = get_config("STRATEGY")
    ctx = ContextHandler(strategy)
    app = create_flask_app(ctx=ctx)
    return app
  except Exception as e:
    print(e.to_json())
    

def get_config(name):
  config_value = os.getenv(name)
  if not config_value:
    raise ValueError("Variable not found in environment.")
  return config_value


if __name__ == "__main__":
  try:
    main(strategy=strategy)
  except ValueError as e:
    print(e)
    sys.exit(1)
  except Exception as e:
    print(e)
    sys.exit(1)
  sys.exit(0)