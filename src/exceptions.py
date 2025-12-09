class ZeroQuantityError(Exception):
    """
    Пользовательское исключение для демонстрации ошибок, где количество 0
    """

    def __init__(self, message=None):
        self.message = message
        super().__init__(self.message)
