import json


def read_transactions(path: str) -> list:
    """возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, 'r', encoding='utf-8') as file:
            # Читаем данные из файла
            data = json.load(file)

            # Проверяем, что прочитанное значение — это список
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        print('файл не найден или не удалось прочитать JSON')
        return []

print(read_transactions('../data/operations.json'))
