import json
import os
from pathlib import Path

from src.utils import read_json


def test_json_read():
    directory_name = Path(__file__).resolve().parent.parent
    file_path = os.path.join(directory_name, "data", "test.json")
    data = {"key": "expected_value"}
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)
    assert read_json("test")["key"] == "expected_value"
