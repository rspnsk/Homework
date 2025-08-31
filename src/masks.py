def get_mask_card_number(number_card: str) -> str:
    """Функция  принимает на вход номер карты и
    возвращает ее маску по правилу XXXX XX** **** XXXX"""
    if not number_card.isdigit():
        return "Некорректный ввод"
    if len(number_card) != 16:
        return "Некорректный ввод"
    mask_number_card = ""
    for i in range(len(number_card)):
        if 0 <= i <= 5 or 12 <= i <= 15:
            mask_number_card += number_card[i]
        else:
            mask_number_card += "*"

    return " ".join([mask_number_card[i : i + 4] for i in range(0, len(mask_number_card), 4)])

# print(get_mask_card_number("7000792289606321"))


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета в виде числа и
    возвращает маску номера по правилу **XXXX."""
    if not account_number.isdigit():
        return "Некорректный ввод"
    if len(account_number) != 20:
        return "Некорректный ввод"
    mask_account = f"**{account_number[-4:]}"
    return mask_account

# print(get_mask_account("73654108430135874305"))
