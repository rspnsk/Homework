from typing import List, Tuple

import pytest

from src.widget import get_date, mask_account_card

test_data: List[Tuple[str, str]] = [
    ("Visa 1234567843218765", "Visa 1234 56** **** 8765"),
    ("Счёт 12345678432187651234", "Счёт **1234"),
    ("MasterCard 1234567843буква", "Некорректный ввод"),
    ("MasterCard", "Некорректный ввод"),
    ("Счёт", "Некорректный ввод")
]


@pytest.mark.parametrize("input_data,expected_output", test_data)
def test_mask_account_card(input_data: str, expected_output: str) -> None:
    assert mask_account_card(input_data) == expected_output


test_date: List[Tuple[str, str]] = [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2024/03-11T02:26:18.671407", "Некорректный формат даты"),
    ("", "Некорректный формат даты")
]


@pytest.mark.parametrize("input_date,expected_output", test_date)
def test_get_date(input_date: str, expected_output: str) -> None:
    assert get_date(input_date) == expected_output
