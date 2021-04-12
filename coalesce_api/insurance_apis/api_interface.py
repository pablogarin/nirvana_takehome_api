from abc import ABC
from abc import abstractmethod


class APIInterface(ABC):
    @abstractmethod
    def fetch_from_api(self, path):
        pass

    @classmethod
    @abstractmethod
    def get_type(cls):
        pass
