from abc import ABC
from abc import abstractmethod


class BaseStrategy(ABC):
    @abstractmethod
    def coalesce_values(self, *args, **kwargs):
        pass