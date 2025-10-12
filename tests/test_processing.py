from typing import Any

from src.processing import filter_by_state, sort_by_date

# Тесты для функции filter_by_state


def test_filter_by_state(
    list_of_dicts: list[dict[Any, Any]],
    list_of_dicts_state_executed: list[dict[Any, Any]]
) -> None:
    # по умолчанию фильтруем по EXECUTED
    assert filter_by_state(list_of_dicts) == list_of_dicts_state_executed


def test_filter_canceled_state(
    list_of_dicts: list[dict[Any, Any]],
    list_of_dicts_state_canceled: list[dict[Any, Any]]
) -> None:
    # фильтруем по CANCELED
    assert filter_by_state(list_of_dicts, "CANCELED") == list_of_dicts_state_canceled


def test_filter_unknown_state(list_of_dicts: list[dict[Any, Any]]) -> None:
    # фильтр по состоянию, которого нет
    assert filter_by_state(list_of_dicts, "UNKNOWN_STATE") == []


def test_filter_empty_list() -> None:
    # передаем пустой список
    assert filter_by_state([]) == []

    # Тесты для функции sort_by_date


def test_sort_by_date_descending(
    list_of_dicts: list[dict[Any, Any]],
    list_of_dicts_sorting_by_descending_date: list[dict[Any, Any]]
) -> None:
    # сортировка по умолчанию (по убыванию)
    assert sort_by_date(list_of_dicts) == list_of_dicts_sorting_by_descending_date


def test_sort_by_date_increasing(
    list_of_dicts: list[dict[Any, Any]],
    list_of_dicts_sorting_by_increasing_date: list[dict[Any, Any]]
) -> None:
    # сортировка по возрастанию
    assert sort_by_date(list_of_dicts, False) == list_of_dicts_sorting_by_increasing_date


def test_sort_by_date_same(
    list_of_dicts_same: list[dict[Any, Any]],
    list_of_dicts_sorting_by_same_date: list[dict[Any, Any]]
) -> None:
    # сортировка при одинаковых датах
    assert sort_by_date(list_of_dicts_same) == list_of_dicts_sorting_by_same_date


def test_sort_by_unusual_date(list_of_dicts_unexpected_date: list[dict[Any, Any]]) -> None:
    # сортировка при некорректном формате даты
    assert sort_by_date(list_of_dicts_unexpected_date) == [{"error": "Некорректная дата"}]
