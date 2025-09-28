import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "some_data, expected",
    [
        ("1234567843218765", "1234 56** **** 8765"),
        ("123456784321", "Некорректный ввод"),
        ("12345678432187650000", "Некорректный ввод"),
        ("", "Некорректный ввод"),
        ("12345678432буква", "Некорректный ввод"),
    ],
)
def test_get_mask_card_number(some_data: str, expected: str) -> None:
    assert get_mask_card_number(some_data) == expected


@pytest.mark.parametrize(
    "some_data, expected",
    [
        ("73654108430135874305", "**4305"),
        ("736541084301358", "Некорректный ввод"),
        ("7365410843013587430500000", "Некорректный ввод"),
        ("", "Некорректный ввод"),
        ("736541084301358буква", "Некорректный ввод"),
    ],
)
def test_get_mask_account(some_data: str, expected: str) -> None:
    assert get_mask_account(some_data) == expected
