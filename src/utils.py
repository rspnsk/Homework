import json
import logging

logger = logging.getLogger('utils')
file_handler = logging.FileHandler('C:/Users/Юрий/PycharmProjects/Homework/logs/utils.log', mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def read_transactions(path: str) -> list:
    """возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            logger.debug('Читаем данные из файла')

            # Проверяем, что прочитанное значение — это список
            if isinstance(data, list):
                logger.info('значение data успешно считаны')
                return data
            else:
                logger.warning('значение data это не список!!!')
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error('файл не найден или не удалось прочитать JSON')
        print('файл не найден или не удалось прочитать JSON')
        return []


print(read_transactions('../data/operations.json'))
