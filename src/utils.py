import json
import os
from pathlib import Path

directory_name = Path(__file__).resolve().parent.parent



def read_json(filename: str):
    """
    Функция читает JSON файл
    :param filename: имя файла
    :return: содержание файла в виде списка
    """
    file_path = os.path.join(directory_name, 'data', filename+'.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return  data



if __name__ == "__main__":
    print(read_json('products'))