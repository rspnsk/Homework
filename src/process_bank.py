import re
from collections import Counter

import numpy


def process_bank_search(operations_list: list[dict], keyword: str) -> list[dict]:
    """
    Функция принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка.
    """
    if not operations_list:
        return []
    chosen_operations = []
    for operation in operations_list:
        description = operation.get('description', '')
        if isinstance(description, str) and re.search(keyword, description, flags=re.IGNORECASE):
            chosen_operations.append(operation)
    return chosen_operations


def process_bank_operations(transactions: list[dict], categories: list) -> dict:
    """
    Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий, а значения — это количество
    операций в каждой категории.
    """
    category_counts = Counter(
        operation.get('description') for operation in transactions if operation.get('description') in categories
    )
    return dict(category_counts)


def extract_values_transactions(data, key):
    """
    Функция принимает список словарей с данными о банковских операциях и значение ключа,
    а возвращает список категорий операций (Категории операций из поля 'description')
    """
    # Собираем все значения в список
    transactions = [item['description'] for item in data if 'description' in item]

    # Удаляем пустые значения из списка
    cleaned_category_operations = [transaction for transaction in transactions if transaction is not numpy.nan]

    # возращаем уникальные значения с помощью множества
    return list(set(cleaned_category_operations))
