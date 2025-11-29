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
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
