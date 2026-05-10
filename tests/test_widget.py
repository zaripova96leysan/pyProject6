import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.widget import get_date, mask_account_card


@pytest.fixture
def card_data():
    return {
        "visa": "Visa 1234567890123456",
        "mastercard": "MasterCard 5555666677778888",
        "maestro": "Maestro 1234567890123456",
        "счет": "Счет 12345678901234567890",
    }


@pytest.mark.parametrize("input_data, expected", [
    ("Visa 1234567890123456", "Visa 1234******3456"),
    ("MasterCard 5555666677778888", "MasterCard 5555******8888"),
    ("Maestro 1234567890123456", "Maestro 1234******3456"),
    ("МИР 9876543210987654", "МИР 9876******7654"),
    ("Счет 12345678901234567890", "Счет **7890"),
    ("Счет 11112222333344445555", "Счет **5555"),
    ("", ""),
    ("Карта", "Карта"),
])
def test_mask_account_card(input_data, expected):
    assert mask_account_card(input_data) == expected


def test_mask_account_card_with_fixture(card_data):
    assert mask_account_card(card_data["visa"]) == "Visa 1234******3456"
    assert mask_account_card(card_data["счет"]) == "Счет **7890"


@pytest.mark.parametrize("input_date, expected", [
    ("2024-03-15T12:30:45.123456", "15.03.2024"),
    ("2023-12-25T10:00:00", "25.12.2023"),
    ("2025-01-01T00:00:00", "01.01.2025"),
    ("", ""),
    ("2024-03-15", "15.03.2024"),
])
def test_get_date(input_date, expected):
    assert get_date(input_date) == expected