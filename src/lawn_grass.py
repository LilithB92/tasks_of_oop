from src.product import Product


class LawnGrass(Product):
    """Класс для представления Трава газонная"""

    country: str
    germination_period: str
    color: str

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        """
         Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра.

        :param name: Имя газона
        :param description: описание газона
        :param price: цена газона
        :param quantity: количество газона
        :param country:страна-производитель газона
        :param germination_period: срок прорастания газона
        :param color: цвет газона
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """
         Метод возвращает сумму произведений цены на количество у двух объектов класса LawnGrass
         или TypeError(если объекты не LawnGrass класса).

        :param other:Объект класса LawnGrass
        :return: возвращает сумму произведений цены на количество у двух объектов или(TypeError)
        """
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError
