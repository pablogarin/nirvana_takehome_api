from coalesce_api.strategies.base_strategy import BaseStrategy


strategies = {}

def register_strategy(strategy: BaseStrategy) -> BaseStrategy:
  type_, cl = strategy.get_type()
  if type_ in strategies:
    if strategies[type_] != cl:
      raise ValueError('Strategy name must be unique')
    return
  strategies[type_] = cl
  return cl


class ContextHandler(object):
  def __init__(self, strategy: str):
    if strategy in strategies:
      self.strategy = strategies[strategy]()
  
  def execute(self, **kwargs) -> None:
    return self.strategy.run(**kwargs)
