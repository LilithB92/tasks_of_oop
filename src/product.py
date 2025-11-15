class Product:
    """
    Класс для представления продукты электротоваров
    """

    name: str
    description: str
    __price: float
    quantity: int
    products_list: list = []
    products_name_list: list = []

    def __init__(self, name, description, price, quantity) -> None:
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.products_list.append(self)
        Product.products_name_list.append(name)

    @classmethod
    def new_product(cls, product_dict: dict):
        """
        Метод принимает на вход cls, продукт для создания в виде словаря и
        возвращает экземпляра класса Product на основе данных словаря.
        Если товар уже существует метод сложить количество в наличии старого товара и нового.
        При конфликте цен выбрать ту, которая является более высокой.
        :param product_dict: Продукт в виде словаря
        :return: экземпляра класса Product на основе данных словаря
        """
        try:
            name = product_dict["name"]
            description = product_dict["description"]
            price = product_dict["price"]
            quantity = product_dict["quantity"]
            if name not in cls.products_name_list:
                new_product = cls(name, description, price, quantity)
                Product.products_list.append(new_product)
                Product.products_name_list.append(name)
            else:
                new_product = cls.update_duplicated_product(name, price, quantity)
            return new_product

        except (AssertionError, AttributeError, KeyError, ValueError):
            return None

    @classmethod
    def update_duplicated_product(cls, name, price, quantity):
        """
        Если товар уже существует метод сложить количество в наличии старого товара и нового.
        При конфликте цен выбрать ту, которая является более высокой.
        Метод вернет товар обнавленнимы даннимы или None если товар не существует

        :param name: Название товара
        :param price: Цена товара
        :param quantity: Количество товара
        :return: Товар с обнавленнимы даннимы
        """
        for product in cls.products_list:
            if product.name == name:
                product.quantity += quantity
                product.price = max(product.price, price)
                return product
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

        :param price: Новое значение цены
        :return: или выводится сообщение, или ничего не возвращает
        """
        if price > 0:
            self.__price = price
        else:
            print("«Цена не должна быть нулевая или отрицательная»")


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 280000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 32000.0, 14)
    product4 = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    print(product4.price)
