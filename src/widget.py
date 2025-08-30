import re
from masks import get_mask_card_number
from masks import get_mask_account

s = "Visa Gold 5999414228426355"
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

print(mask_account_card(s))

def get_date(data: str) -> str:
    data_1 = data[:10]
    data_2 = data_1.split('-')
    return f"{data_2[2]}.{data_2[1]}.{data_2[0]}"
print(get_date("2024-03-11T02:26:18.671407"))