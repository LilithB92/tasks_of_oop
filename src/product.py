class Product:
    """
    Класс для представления продукты электротоваров
    """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity) -> None:
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
