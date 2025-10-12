from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(s: str) -> str:
    """обрабатывает информацию о картах И счетах
    возвращает строку с замаскированным номером карты или счета"""
    letters = ''.join(c for c in s if c.isalpha())
    numbers = ''.join(c for c in s if c.isdigit())
    if len(numbers) == 16:
        return letters + ' ' + get_mask_card_number(numbers)
    elif len(numbers) == 20:
        return letters + ' ' + get_mask_account(numbers)
    else:
        return "Некорректный ввод"


def get_date(date_string: str) -> str:
    """Преобразует дату из формата "2024-03-11T02:26:18.671407" в формат "11.03.2024"."""
    try:
        dt = datetime.fromisoformat(date_string)
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        return "Некорректный формат даты"
