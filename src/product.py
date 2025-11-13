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

    @classmethod
    def new_product(cls, product_dict: dict):
        """
        Метод принимает на вход cls, продукт для создания в виде словаря и
        возвращает экземпляра класса Product на основе данных словаря
        :param product_dict: продукт  виде словаря
        :return: экземпляра класса Product на основе данных словаря
        """
        try:
            name = product_dict["name"]
            description = product_dict["description"]
            price = product_dict["price"]
            quantity = product_dict["quantity"]
            return cls(name, description, price, quantity)
        except (AssertionError, AttributeError, KeyError, ValueError):
            return None
