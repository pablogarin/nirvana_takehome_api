import os
import sys
from coalesce_api import create_flask_app
from coalesce_api.strategies.context_handler import ContextHandler
from coalesce_api.utils.config import get_config


def main(*args, **kwargs):
  try:
    strategy = get_config("STRATEGY")
    ctx = ContextHandler(strategy)
    app = create_flask_app(ctx=ctx)
    app.run()
  except Exception as e:
    print(e.to_json())


if __name__ == "__main__":
  try:
    main()
  except ValueError as e:
    print(e)
    sys.exit(1)
  except Exception as e:
    print(e)
    sys.exit(1)
  sys.exit(0)