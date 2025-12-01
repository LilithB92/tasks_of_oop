from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def add_product(cls, *args, **kwargs):
        pass
