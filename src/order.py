from src.base_item import BaseItem


class Order(BaseItem):
    """
    Класс для представления купленный товар, количество купленного товара, а также итоговая стоимость.
    """

    name: str
    quantity: int
    price: int
    total_price: float

    def __init__(self, name, price, quantity):
        """
         Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра.
        :param name: Имя заказанного товара
        :param price: цена заказанного товара
        :param quantity: количество заказанного товара
        """
        self.name = name
        self.quantity = quantity
        self.price = price
        Order.total_price = price * quantity

    def get_info(self) -> str:
        """
        Метод возвращает строку с информациям о заказе: имя, количество и итоговая сумма.
        :return: Строку с информациям о заказе: имя, количество и итоговая сумма
        """
        return f"Заказ: {self.name} x {self.quantity}, " f"Итоговая стоимость: {Order.total_price}"
