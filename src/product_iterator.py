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

    def __iter__(self):
        """
        Возвращает итератор.
        :return: Итератор
        """
        self.index_obj = 0
        return self

    def __next__(self):
        """
        Возвращает следующее товар категории.
        Raises:
            StopIteration: Если достигнута верхняя граница диапазона.
        :return: Строку: Название продукта, X руб. Остаток: X шт
        """
        if self.index_obj < len(self.category_obj.product):
            product = self.category_obj.product[self.index_obj]
            self.index_obj += 1
            return product
        else:
            raise StopIteration
