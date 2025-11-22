from src.product import Product


class Category:
    """
    Класс для представления категории электротоваров
    """

    name: str
    description: str
    __products: list
    product_count: int = 0
    category_count: int = 0

    def __init__(self, name, description, products=None) -> None:
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = products if products else []
        self.product_count += len(self.__products) if products else 0
        Category.category_count += 1

    def __str__(self):
        """
        Метод рассчитывает общее количество товаров на складе (quantity) для каждого продукта
        в приватном атрибуте products и возвращает строку: Название категории, количество продуктов: X шт.
        :return: Строку: Название категории, количество продуктов: X шт.
        """
        products_count = sum([product.quantity for product in self.__products])
        return f"{self.name}, количество продуктов: {products_count} шт.\n"

    def add_product(self, product: Product) -> None:
        """
        Метод добавляет продукт в атрибут products
        и увеличивает «счетчик продуктов» (атрибут product_count) на 1
        :param product: экземпляра класса Product
        :return: не возвращает значения
        """
        self.__products.append(product)
        self.product_count += 1

    @property
    def products(self):
        """
        Метод возвращает строку со всеми продуктами в приватном атрибуте products
        :return: строку со всеми продуктами
        """
        products_str = ""
        for product in self.__products:
            products_str += product.__str__()
        return products_str
