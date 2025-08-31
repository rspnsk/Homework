import re
from datetime import datetime

from masks import get_mask_account, get_mask_card_number


def mask_account_card(s: str) -> str:
    "обрабатывает информацию о картах И счетах"
    "возвращает строку с замаскированным номером карты или счета"
    account_number = re.split(r'(\d+)', s)
    if len(account_number[1]) == 16:
        return account_number[0] + " " + get_mask_card_number(account_number[1])
    elif len(account_number[1]) == 20:
        return account_number[0] + " " + get_mask_account(account_number[1])
    else:
        return "Некорректный ввод"


# iso_date это исходная дата в формате ISO 8601
def get_date(iso_date: str) -> str:
    "функция get_date возвращает строку с датой в формате ДД.ММ.ГГГГ"
    # парсим строку в объект datetime
    parsed_date = datetime.strptime(iso_date, "%Y-%m-%dT%H:%M:%S.%f")
    # Преобразуем дату в нужный формат
    formatted_date = parsed_date.strftime("%d.%m.%Y")
    return (formatted_date)  # Вывод: "ДД.ММ.ГГГГ"
