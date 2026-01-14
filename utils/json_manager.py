import json


class JsonManager:
    @staticmethod
    def read(path, encoding="UTF-8"):
        try:
            with open(path, 'r', encoding=encoding) as file:
                return json.load(file)
        except FileNotFoundError as e:
            print(f"ERROR: File not found!\n{e}")
            return None