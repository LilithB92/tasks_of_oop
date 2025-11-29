import pytest


def test_lawn_grass_init(grass1: object) -> None:
    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"


def test_lawn_grass_add(grass1: object, grass2: object) -> None:
    assert grass2 + grass1 == 16750.0


def test_lawn_grass_add_error(grass1: object, smartphone1: object) -> None:
    with pytest.raises(TypeError):
        assert grass1 + smartphone1
