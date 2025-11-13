class Product:
    """
    Класс для представления продукты электротоваров
    """

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity) -> None:
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
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

    @property
    def price(self) -> float:
        """
        Геттер для атрибута __price возвращает значение приватного атрибута цены

        :return: значение приватного атрибута цены
        """
        return self.__price

    @price.setter
    def price(self, price: int):
        """
        Сеттер принимает два аргумента — self и новое значение цены.
        Если новое значение цены положительное, то в атрибуте обновляется значение цены.
        А если не положительное, то выводится сообщение «Цена не должна быть нулевая или отрицательная» в консоль.

        :param price: новое значение цены
        :return: или выводится сообщение или ничего не возвращает
        """
        if price > 0:
            self.__price = price
        else:
            print("«Цена не должна быть нулевая или отрицательная»")
