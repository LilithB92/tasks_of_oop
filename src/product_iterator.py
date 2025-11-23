from src.category import Category


class ProductIterator:
    """
    Класс перебирает товары одной категории
    """

    category_obj: Category
    index_obj: int = 0

    def __init__(self, category_obj):
        """
        Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра.

        :param category_obj: Объект класса Category
        """
        self.category_obj = category_obj
