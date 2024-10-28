import os
import json
from typing import Tuple, List

def validate_json_file(file_path: str, required_fields: List[str]) -> Tuple[bool, List[str]]:
    """Проверяет, существует ли файл и соответствует ли он требованиям."""
    
    if not os.path.isfile(file_path):
        return False, ["Файл не существует."]
    
    if os.path.getsize(file_path) == 0:
        return False, ["Файл пуст."]
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        return validate_data(data, required_fields)
    except json.JSONDecodeError:
        return False, ["Файл не является корректным JSON."]
    except Exception as e:
        return False, [f"Произошла ошибка: {str(e)}"]

def validate_data(data: list, required_fields: List[str]) -> Tuple[bool, List[str]]:
    """Проверяет, соответствует ли содержимое JSON-файла заданным требованиям."""
    
    errors = []
    
    if not isinstance(data, list):
        return False, ["Файл должен содержать массив объектов."]
    
    for index, entry in enumerate(data):
        if not isinstance(entry, dict):
            errors.append(f"Элемент {index + 1} должен быть объектом (словарем).")
            continue
        
        for field in required_fields:
            if field not in entry:
                errors.append(f"В элементе {index + 1} отсутствует необходимое поле: {field}.")
    
    if errors:
        return False, errors
    
    return True, []
