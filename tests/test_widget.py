import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.widget import mask_account_card, get_date  # noqa: E402


@pytest.fixture
def card_data():
    """Фикстура с разными типами карт"""
    return {
        "visa": "Visa 1234567890123456",
        "mastercard": "MasterCard 5555666677778888",
        "счет": "Счет 12345678901234567890",
    }


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("Visa 1234567890123456", "Visa 1234******3456"),
        ("MasterCard 5555666677778888", "MasterCard 5555******8888"),
        ("Счет 12345678901234567890", "Счет **7890"),
        ("", ""),
    ],
)
def test_mask_account_card(input_data, expected):
    """Тест маскирования карт и счетов"""
    assert mask_account_card(input_data) == expected


def test_mask_account_card_with_fixture(card_data):
    """Используем фикстуру для тестирования"""
    assert mask_account_card(card_data["visa"]) == "Visa 1234******3456"
    assert mask_account_card(card_data["счет"]) == "Счет **7890"


@pytest.mark.parametrize(
    "input_date, expected",
    [
        ("2024-03-15T12:30:45.123456", "15.03.2024"),
        ("2023-12-25T10:00:00", "25.12.2023"),
        ("", ""),
    ],
)
def test_get_date(input_date, expected):
    """Тест преобразования даты"""
    assert get_date(input_date) == expected


def test_mask_account_card_only_name():
    """Строка 16: только название без номера (len(parts) == 1)"""
    assert mask_account_card("Visa") == "Visa"
    assert mask_account_card("MasterCard") == "MasterCard"
    assert mask_account_card("Счет") == "Счет"


def test_mask_account_card_account_variants():
    assert mask_account_card("Счет 12345678901234567890") == "Счет **7890"
    assert mask_account_card("Счет 123") == "Счет **123"
    assert mask_account_card("Счет 1234") == "Счет **1234"
    assert mask_account_card("Счет 12345") == "Счет **2345"


def test_mask_account_card_card_variants():
    assert mask_account_card("Visa 1234567890123456") == "Visa 1234******3456"
    assert mask_account_card("Visa 1234") == "Visa 1234"
    assert mask_account_card("MasterCard 12345678") == "MasterCard 12345678"
    assert mask_account_card("Мир 9876543210987654") == "Мир 9876******7654"
    assert (
        mask_account_card("American Express 1234567890123456")
        == "American Express 1234******3456"
    )


def test_get_date_complete_coverage():
    assert get_date("2024-03-15T12:30:45.123456") == "15.03.2024"
    assert get_date("2024-03-15 12:30:45") == "15.03.2024"
    assert get_date("2024-03-15") == "15.03.2024"
    assert get_date("") == ""
    assert get_date("15.03.2024") == "15.03.2024"
    assert get_date("2024/03/15") == "2024/03/15"
    assert get_date("not-a-date") == "date.a.not"
    assert get_date("2024-03") == "2024-03"


def test_mask_account_card_empty_string():
    assert mask_account_card("") == ""


def test_mask_account_card_name_with_spaces():
    assert (
        mask_account_card("American Express 1234567890123456")
        == "American Express 1234******3456"
    )
