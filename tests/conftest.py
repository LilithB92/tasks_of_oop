from unittest.mock import patch

import pytest

from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator


@pytest.fixture
def first_category() -> Category:
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
        products=[
            Product(
                name="Samsung Galaxy S23 Ultra",
                description="256GB, Серый цвет, 200MP камера",
                price=180000.0,
                quantity=5,
            ),
            Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8),
            Product(name="Xiaomi Redmi Note 11", description="1024GB, Синий", price=31000.0, quantity=14),
        ],
    )


@pytest.fixture
def second_category():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром,"
        " станет вашим другом и помощником",
        products=[Product(name='55" QLED 4K', description="Фоновая подсветка", price=123000.0, quantity=7)],
    )


@pytest.fixture
def product():
    return Product(name="Xiaomi Redmi Note 11", description="1024GB, Синий", price=31000.0, quantity=14)


@pytest.fixture
def other_product_for_add():
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)


@pytest.fixture
def product_dict() -> dict:
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 120000.0,
        "quantity": 5,
    }


@pytest.fixture
def product_dict1() -> dict:
    return {
        "name": "Poko",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }


@pytest.fixture
def mock_input_data():
    with patch("builtins.input", return_value="y"):
        yield


@pytest.fixture
def product_iterator(first_category):
    return ProductIterator(first_category)
