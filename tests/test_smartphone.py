import pytest


def test_smartphone_init(smartphone1: object) -> None:
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_smartphone_add(smartphone1: object, smartphone2: object) -> None:
    assert smartphone2 + smartphone1 == 2580000.0


def test_smartphone_add_invalid(smartphone1: object, product: object) -> None:
    with pytest.raises(TypeError):
        assert smartphone1 + product
