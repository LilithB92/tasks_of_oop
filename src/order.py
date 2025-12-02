class Order:
    """
    Класс для представления купленный товар, количество купленного товара, а также итоговая стоимость.
    """

    name: str
    price: float
    quantity: int

    def __init__(self, name, price, quantity):
        """
         Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра.
        :param name: Имя заказанного товара
        :param price: цена заказанного товара
        :param quantity: количество заказанного товара
        """
        self.name = name
        self.price = price
        self.quantity = quantity
