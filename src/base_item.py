from abc import ABC, abstractmethod


class BaseItem(ABC):
    """
    Абстрактный класс представляющий универсальный элемент
    """

    @abstractmethod
    def get_info(self) -> str:
        pass
