def get_mask_card_number(number_card: int) -> str:
    """Функция  принимает на вход номер карты и
    возвращает ее маску по правилу XXXX XX** **** XXXX"""
    number_card_str = str(number_card)
    if not number_card_str.isdigit():
        return "Некорректный ввод"
    if len(number_card_str) != 16:
        return "Некорректный ввод"
    mask_number_card = ""
    for i in range(len(number_card_str)):
        if 0 <= i <= 5 or 12 <= i <= 15:
            mask_number_card += number_card_str[i]
        else:
            mask_number_card += "*"

    return " ".join([mask_number_card[i : i + 4] for i in range(0, len(mask_number_card), 4)])


def get_mask_account(account_number: int) -> str:
    """Функция принимает на вход номер счета в виде числа и
    возвращает маску номера по правилу **XXXX."""
    account_number_str = str(account_number)
    if not account_number_str.isdigit():
        return "Некорректный ввод"
    if len(account_number_str) != 20:
        return "Некорректный ввод"
    mask_account = f"**{account_number_str[-4:]}"
    return mask_account

