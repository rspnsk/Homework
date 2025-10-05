import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


# Параметризация для теста фильтрации по валюте
@pytest.mark.parametrize("currency_code, expected_ids", [
    ("USD", [939719570, 142264268, 895315941]),  # Должны отобраться транзакции в USD
    ("RUB", [873106923, 594226727]),  # Должны отобраться транзакции в RUB
    ("EUR", []),  # Транзакций в евро нет
    ("", []),  # Пустая валюта — транзакций нет
])
def test_filter_by_currency(sample_transactions, currency_code, expected_ids):
    results = list(filter_by_currency(sample_transactions, currency_code))

    # Получаем id отобранных транзакций
    result_ids = [trans["id"] for trans in results]

    # Проверяем, что вернулись ожидаемые транзакции
    assert result_ids == expected_ids


# Проверка обработки пустого списка транзакций
def test_empty_transaction_list(sample_transactions):
    empty_transactions = []
    result = list(filter_by_currency(empty_transactions, "USD"))
    assert result == [], "Должен вернуть пустой список"


# Проверка обработки транзакций без подходящей валюты
def test_no_matching_currency(sample_transactions):
    no_usd_transactions = [
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "5870.67",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Операция отменена",
            "from": "",
            "to": ""
        }
    ]
    result = list(filter_by_currency(no_usd_transactions, "USD"))
    assert result == [], "Должен вернуть пустой список, так как нет USD-транзакций"

# Параметризация для теста функции "transaction_descriptions"


@pytest.mark.parametrize(
    "expected",
    [
        [
            "Перевод организации",
            "Перевод со счета на счет",
            "Перевод со счета на счет",
            "Перевод с карты на карту",
            "Перевод организации",
        ]
    ],
)
def test_transaction_descriptions(sample_transactions, expected):
    result = list(transaction_descriptions(sample_transactions))
    assert result == expected


# Проверка обработки транзакций без "description"
def test_no_matching_description():
    no_description = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }
    ]
    result = list(transaction_descriptions(no_description))
    assert result == ["описание отсутствует"]


#  Проверка []
def test_empty_transactions():
    # Передача пустого списка транзакций
    empty_transactions = []
    result = list(transaction_descriptions(empty_transactions))
    assert result == []


# Параметризация для Генератора номера карт

@pytest.mark.parametrize("start,stop,expected_cards", [
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    (1000, 1001, ["0000 0000 0000 1000", "0000 0000 0000 1001"]),
    (9999999999999999, 9999999999999999, ["9999 9999 9999 9999"])
])
def test_card_number_generator(start, stop, expected_cards):
    generated_cards = list(card_number_generator(start, stop))
    assert generated_cards == expected_cards
