import pytest
from src.process_bank import process_bank_search, process_bank_operations


# Тест для функции process_bank_search
@pytest.fixture
def sample_operations():
    return [
        {'date': '08.12.2019', 'amount': '40542 руб.', 'state': 'EXECUTED', 'description': 'Открытие вклада'},
        {'date': '22.07.2023', 'amount': '30368 руб.', 'state': 'CANCELED', 'description': 'Перевод с карты на карту'},
        {'date': '05.09.2023', 'amount': '16210 руб.', 'state': 'EXECUTED', 'description': 'Перевод организации'}
    ]


@pytest.mark.parametrize("keyword, expected_result", [
    ("Открытие вклада", [{'date': '08.12.2019', 'amount': '40542 руб.', 'state': 'EXECUTED', 'description': 'Открытие вклада'}]),
    ("Перевод организации",
     [{'date': '05.09.2023', 'amount': '16210 руб.', 'state': 'EXECUTED', 'description': 'Перевод организации'}]),
    ("Перевод с карты на карту",
     [{'date': '22.07.2023', 'amount': '30368 руб.', 'state': 'CANCELED', 'description': 'Перевод с карты на карту'}]),
    ("ненужный", []),  # Проверка отсутствия совпадений
    ("любое", [])  # Проверка отсутствия ключа 'description'
])
def test_process_bank_search(sample_operations, keyword, expected_result):
    # Выполняем функцию с параметрами
    result = process_bank_search(sample_operations, keyword)

    # Проверяем, что результат соответствует ожидаемому
    assert result == expected_result


#  Тесты для функции process_bank_operations
@pytest.fixture
def sample_transactions():
    return [
        {'date': '08.12.2019', 'amount': '40542 руб.', 'state': 'EXECUTED', 'description': 'Открытие вклада'},
        {'date': '22.07.2023', 'amount': '30368 руб.', 'state': 'CANCELED', 'description': 'Перевод с карты на карту'},
        {'date': '05.09.2023', 'amount': '16210 руб.', 'state': 'EXECUTED', 'description': 'Перевод организации'}
    ]


@pytest.mark.parametrize("categories, expected_result", [
    # Тест 1: Пустой список операций
    ([], {}),

    # Тест 2: Корректный список операций
    (['Открытие вклада', 'Перевод организации'], {'Открытие вклада': 1, 'Перевод организации': 1}),

    # Тест 3: Операций больше, чем категорий
    (['Перевод с карты на карту'], {'Перевод с карты на карту': 1}),

    # Тест 4: Классифицируем по категориям, которых нет в операциях
    (['Страховка', 'Коммунальные'], {}),

    # Тест 5: Смешанный случай (частичное совпадение категорий)
    (['Перевод с карты на карту', 'Открытие вклада'], {'Открытие вклада': 1, 'Перевод с карты на карту': 1}),
])
def test_process_bank_operations(sample_transactions, categories, expected_result):
    # Выполняем функцию с параметрами
    result = process_bank_operations(sample_transactions, categories)

    # Проверяем, что результат соответствует ожидаемому
    assert result == expected_result
