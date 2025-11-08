import logging
import os

print(os.getcwd())

# Создание и получение именованного логера
logger = logging.getLogger('masks')
# Создаем хендлер для вывода в файл
file_handler = logging.FileHandler('C:/Users/Юрий/PycharmProjects/Homework/logs/masks.log', mode='w', encoding='utf-8')
# Создаем форматер для форматирования вывода используемого хендлера.
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# устанавливаем созданный форматер для хендлера
file_handler.setFormatter(file_formatter)
# добавляем хендлер в логер
logger.addHandler(file_handler)
# Устанавливаем уровень логирования
logger.setLevel(logging.DEBUG)


def get_mask_card_number(number_card: str) -> str:
    """Функция  принимает на вход номер карты и
    возвращает ее маску по правилу XXXX XX** **** XXXX"""
    if not number_card.isdigit():
        logger.error('не цифры!')
        return "Некорректный ввод"
    if len(number_card) != 16:
        logger.error('не 16 цифр')
        return "Некорректный ввод"
    mask_number_card = ""
    for i in range(len(number_card)):
        if 0 <= i <= 5 or 12 <= i <= 15:
            mask_number_card += number_card[i]
        else:
            mask_number_card += "*"

    logger.info("Успешно создана маска карты")
    return " ".join([mask_number_card[i : i + 4] for i in range(0, len(mask_number_card), 4)])


# print(get_mask_card_number('1234567891231236'))


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета в виде числа и
    возвращает маску номера по правилу **XXXX."""
    if not account_number.isdigit():
        logger.error('не цифры!')
        return "Некорректный ввод"
    if len(account_number) != 20:
        logger.error('не 20 цифр!')
        return "Некорректный ввод"
    logger.info("Успешно создана маска карты")
    mask_account = f"**{account_number[-4:]}"
    return mask_account
