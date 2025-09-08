from datetime import datetime
from typing import Dict


def filter_by_state(my_list_dict: list, state: str = 'EXECUTED') -> list:
    '''возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению.'''
    filter_my_list_dict = []
    for dict in my_list_dict:
        if dict['state'] == state:
            filter_my_list_dict.append(dict)
    return filter_my_list_dict


def sort_by_date(my_list_dict: list, descending: bool = True) -> list:
    '''принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате (date)'''

    def get_date(transaction: Dict[str, str]) -> datetime:
        '''Извлекаем дату из словаря и приводим её к типу datetime'''
        return datetime.fromisoformat(transaction['date'])
    sort_my_list_dict = sorted(my_list_dict, key=get_date, reverse=descending)
    return sort_my_list_dict
