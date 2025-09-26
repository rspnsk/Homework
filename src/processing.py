from datetime import datetime
from typing import Any, Dict


def filter_by_state(my_list_dict: list, state: str = 'EXECUTED') -> list:
    '''возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению.'''
    filter_my_list_dict = []
    for dict in my_list_dict:
        if dict['state'] == state:
            filter_my_list_dict.append(dict)
    return filter_my_list_dict


def get_date(transaction: Dict[str, str]) -> datetime:
    '''Извлекаем дату из словаря и приводим её к типу datetime'''
    return datetime.fromisoformat(transaction['date'])


def sort_by_date(my_list_dict: list[dict[Any, Any]], descending: bool = True) -> list[dict[Any, Any]]:
    '''Функция сортирует список словарей по дате, по умолчанию — по убыванию'''

    # Проверяем, что даты корректны
    try:
        # Сортируем список по дате
        sorted_list = sorted(my_list_dict, key=get_date, reverse=descending)
        return sorted_list
    except ValueError:
        return [{"error": "Некорректная дата"}]
