from src.product import Product


def test_print_mixin(capsys)->None:
    Product(name="Xiaomi Redmi Note 11", description="1024GB, Синий", price=31000.0, quantity=14)
    message = capsys.readouterr()
    assert message.out.strip() == "Product('Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, 14)"

