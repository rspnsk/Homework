import math
from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(s: str) -> str:
    """
    обрабатывает информацию о картах И счетах
    возвращает строку с замаскированным номером карты или счета
    """
    # Проверяем, не является ли s значением NaN
    if isinstance(s, float) and math.isnan(s):
        return "Ошибка: Некорректный номер счета или карты"

    # Преобразуем s в строку, если это число
    if isinstance(s, float):
        s = str(int(s))  # Преобразуем float в целое число и затем в строку

    letters = ''.join(c for c in s if c.isalpha())
    numbers = ''.join(c for c in s if c.isdigit())
    if len(numbers) == 16:
        return letters + ' ' + get_mask_card_number(numbers)
    elif len(numbers) == 20:
        return letters + ' ' + get_mask_account(numbers)
    else:
        return "Ошибка: Некорректный номер счета или карты"


def get_date(date_string: any) -> str:
    """
    Преобразует дату из формата "YYYY-MM-DDTHH:MM:SS.ssssss" в формат "DD.MM.YYYY".
   """
    try:
        # Проверяем, что переданная дата является строкой
        if not isinstance(date_string, str):
            return "некорректный формат даты"

        # Пробуем преобразовать дату
        dt = datetime.fromisoformat(date_string)
        return dt.strftime("%d.%m.%Y")
    except TypeError:
        # Если произошел TypeError (например, дата не строка)
        return "некорректный формат даты"
    except ValueError:
        # Если формат даты некорректен
        return "некорректный формат даты"
    except Exception:
        # Ловим любые другие исключения и выводим свое сообщение
        return "некорректный формат даты"
