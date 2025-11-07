from typing import Dict, Iterator, List


def filter_by_currency(transactions: List[Dict], currency_code: str) -> Iterator[Dict]:
    """
    Возвращает итератор транзакций с указанной валютой.
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Генератор, возвращающий описание каждой транзакции.
    """
    if not transactions:
        return iter([])
    for transaction in transactions:
        yield transaction.get("description", "описание отсутствует")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генератор номеров карт в диапазоне [start, end].
    """
    for number in range(start, stop + 1):
        # Форматируем число в 16-значное с ведущими нулями
        card_num = f"{number:016d}"
        # Разбиваем на группы по 4 цифры
        formatted = " ".join([card_num[i:i + 4] for i in range(0, 16, 4)])
        yield formatted


def filter_by_currency_json(transactions, currency_code="RUB"):
    """
    Возвращает список транзакций с указанной валютой, по умолчанию RUB, для json файлов
    """
    transaction_data_currency = []
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == "RUB":
            transaction_data_currency.append(transaction)
    return transaction_data_currency


def filter_by_currency_csv(transactions, currency_code="RUB"):
    """
    Возвращает список транзакций с указанной валютой для json и excel файлов
    """
    transaction_data_currency = []
    for transaction in transactions:
        if transaction.get("currency_code", {}) == "RUB":
            transaction_data_currency.append(transaction)
    return transaction_data_currency
