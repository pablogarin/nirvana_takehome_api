import unittest
from unittest.mock import patch

from coalesce_api.utils.config import get_config

class TestConfig(unittest.TestCase):
  @patch("os.getenv", new=lambda env: f"mock_{env}")
  def test_should_get_config_value(self):
    val = get_config("TEST")
    self.assertEqual(val, "mock_TEST")

  @patch("os.getenv", new=lambda env: None)
  def test_should_fail_with_invalid_key(self):
    with self.assertRaises(ValueError):
      get_config("TEST")
