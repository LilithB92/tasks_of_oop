def test_product_init(order: object) -> None:
    assert order.name == "Xiaomi Redmi Note 11"
    assert order.price == 31000.0
    assert order.quantity == 14
