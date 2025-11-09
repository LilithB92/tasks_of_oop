import json
import os
from pathlib import Path
from typing import Any

from src.category import Category
from src.product import Product

directory_name = Path(__file__).resolve().parent.parent


def read_json(filename: str) -> Any:
    """
    Функция читает JSON файл
    :param filename: имя файла
    :return: содержание файла в виде списка
    """
    file_path = os.path.join(directory_name, "data", filename + ".json")
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def json_data_to_object(data: list[dict]) -> list:
    """
    Функция создавать объекты классов из списков словорей
    :param data: список словорей
    :return: список с обектомы класса Category и Products
    """
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories


if __name__ == "__main__":
    json_data = read_json("products")
    print(json_data_to_object(json_data)[0].products[0].name)
