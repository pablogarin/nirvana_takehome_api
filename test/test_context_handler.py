import unittest

from coalesce_api.strategies.average_strategy import AverageStrategy
from coalesce_api.strategies.base_strategy import BaseStrategy
from coalesce_api.strategies.context_handler import ContextHandler
from coalesce_api.strategies.context_handler import register_strategy
from coalesce_api.strategies.context_handler import strategies


class DummyStrategy(BaseStrategy):
  def run(self):
    pass

  @classmethod
  def get_type(cls):
    return 'average', cls


class TestContextHandler(unittest.TestCase):
  def test_should_return_average_strategy(self):
    ctx = ContextHandler('average')
    self.assertEqual(ctx.strategy.__class__, AverageStrategy)
  
  def test_should_run_strategy(self):
    ctx = ContextHandler('average')
    result = ctx.execute(
      fields=["test"],
      payload=[{"test": 1}, {"test": 3}])
    self.assertEqual(result, {"test": 2.0})
  
  def test_should_fail_to_run_strategy_without_fields(self):
    ctx = ContextHandler('average')
    with self.assertRaises(ValueError):
      result = ctx.execute(
        payload=[{"test": 1}, {"test": 3}])
  
  def test_should_not_register_strategy_twice(self):
    prev_len = len(strategies.items())
    register_strategy(AverageStrategy)
    self.assertEqual(len(strategies.items()), prev_len)
  
  def test_should_fail_registering_strategy(self):
    with self.assertRaises(ValueError):
      register_strategy(DummyStrategy)
