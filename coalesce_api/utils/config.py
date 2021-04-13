import os
from dotenv import load_dotenv

load_dotenv()


def get_config(name: str, default: any = None) -> str:
  config_value = os.getenv(name)
  if not config_value:
    raise ValueError("Variable not found in environment.")
  return config_value
