import json

def load_rating(rating_path):
    """Загрузка данных рекордов из файла."""
    with open(rating_path, "r") as f:
        return json.load(f)
