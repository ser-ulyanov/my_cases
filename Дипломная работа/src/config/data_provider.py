import json


class DataProvider:
    def __init__(self) -> None:
        with open("test_data.json", encoding="utf-8") as file:
            self.data = json.load(file)

    def get(self, key: str) -> str:
        return self.data[key]
