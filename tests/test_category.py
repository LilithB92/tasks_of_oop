def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == (
        "Смартфоны, как средство не только коммуникации, " "но и получения дополнительных функций для удобства жизни"
    )
    assert len(first_category.products) == 146

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 3
    assert second_category.product_count == 1


def test_add_product_in_category(second_category, product):
    second_category.add_product(product)
    assert second_category.product_count == 2
