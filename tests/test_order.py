from src.order import Order


def test_product_init(order: object) -> None:
    assert order.name == "Xiaomi Redmi Note 11"
    assert order.price == 31000.0
    assert order.quantity == 14


def test_get_info() -> None:
    order = Order(name="Xiaomi Redmi Note 11", price=31000.0, quantity=14)
    assert order.get_info() == "Заказ: Xiaomi Redmi Note 11 x 14, Итоговая стоимость: 434000.0"


def test_zero_quantity_error(capsys) -> None:
    Order(name="Xiaomi Redmi Note 11", price=31000.0, quantity=0)
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Нельзя заказать товаров не положительном количестве"
    assert message.out.strip().split("\n")[-1] == "Обработка добавления товара завершена."
