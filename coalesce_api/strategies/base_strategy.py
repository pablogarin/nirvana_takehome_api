from abc import ABC
from abc import abstractmethod


class BaseStrategy(ABC):
  @abstractmethod
  def run(self, *args, **kwargs):
    pass
  
  @classmethod
  @abstractmethod
  def get_type(cls):
    pass