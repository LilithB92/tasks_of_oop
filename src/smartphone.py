from src.product import Product


class Smartphone(Product):
    """
    Класс для представления Смартфонов
    """

    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """
          Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра.
        :param name: Имя смартфона
        :param description: описание смартфона
        :param price: цена смартфона
        :param quantity: количество смартфона
        :param efficiency: производительность смартфона
        :param model: модель смартфона
        :param memory: объем встроенной памяти смартфона
        :param color: цвет смартфона
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """
         Метод возвращает сумму произведений цены на количество у двух объектов класса Smartphone
         или TypeError(если объекты не Smartphone класса).

        :param other:Объект класса Smartphone
        :return: возвращает сумму произведений цены на количество у двух объектов или(TypeError)
        """
        if type(other) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError
