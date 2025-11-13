from src.product import Product


class Category:
    """
    Класс для представления категории электротоваров
    """

    name: str
    description: str
    products: list
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name, description, products=None) -> None:
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, product: Product):
        """Метод  добавляет продукт  в атрибут products
        и увеличивает «счетчик продуктов» (атрибут product_count) на 1"""
        self.__products.append(product)
        self.product_count += 1

