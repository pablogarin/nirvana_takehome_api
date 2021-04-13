import unittest

from coalesce_api.strategies.average_strategy import AverageStrategy


class TestAverageStrategy(unittest.TestCase):
  def test_should_run_strategy_successfully(self):
    strategy = AverageStrategy()
    result = strategy.run(
      fields=["test"],
      payload=[{"test": 1}, {"test": 3}])
    self.assertEqual(result, {"test": 2.0})

  def test_should_fail_run_without_fields_param(self):
    strategy = AverageStrategy()
    with self.assertRaises(ValueError):
      result = strategy.run(
        payload=[{"test": 1}, {"test": 3}])
