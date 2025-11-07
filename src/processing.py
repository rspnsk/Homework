from datetime import datetime
from typing import Dict, List


def filter_by_state(transactions: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    '''
    возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению.
    '''
    return [transaction for transaction in transactions if transaction.get('state') == state]


def get_date(transaction: dict) -> datetime:
    '''Извлекаем дату из словаря и приводим её к типу datetime'''
    date_str = transaction.get('date', '')
    if isinstance(date_str, str) and date_str.strip():  # Проверяем, что это строка и не пустая
        try:
            return datetime.fromisoformat(date_str)
        except ValueError:
            return None  # Если формат даты некорректен, возвращаем None
    else:
        return None  # Если дата пустая или не строка, возвращаем None


def sort_by_date(my_list_dict: list[dict], descending: bool = True) -> list[dict]:
    '''Функция сортирует список словарей по дате, по умолчанию — по убыванию'''

    # Сортируем список, исключая транзакции без даты
    sorted_list = sorted([d for d in my_list_dict if get_date(d)], key=get_date, reverse=descending)
    return sorted_list

# transaction_data = read_transactions("../data/operations.json")
# transaction_data = read_file_csv("../data/transactions.csv")
# print(transaction_data)
# dat = get_date(transaction_data)
# print(dat)
