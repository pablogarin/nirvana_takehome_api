from dotenv import load_dotenv
from coalesce_api import create_flask_app
from coalesce_api.strategies.context_handler import ContextHandler
from coalesce_api.utils.config import get_config

load_dotenv()


strategy = get_config("STRATEGY")
ctx = ContextHandler(strategy)
app = create_flask_app(ctx=ctx)
