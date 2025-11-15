import pytest

from src.product import Product


def test_product_init(product) -> None:
    assert product.name == "Xiaomi Redmi Note 11"
    assert product.description == "1024GB, Синий"
    assert product.price == 31000.0
    assert product.quantity == 14


def test_new_product(product_dict: dict, product_dict1: dict) -> None:
    product1 = Product.new_product(product_dict)
    product2 = Product.new_product(product_dict1)

    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product2.name == "Poko"


def test_new_product_invalid() -> None:
    product1 = Product.new_product({})
    with pytest.raises(AttributeError):
        assert product1.name
