import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card_number, expected", [
    ("1234567890123456", "1234******3456"),
    ("1111222233334444", "1111******4444"),
    ("", ""),
    ("1234", "1234"),
])
def test_get_mask_card_number(card_number, expected):
    """Тест маскирования номера карты"""
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("account, expected", [
    ("12345678901234567890", "**7890"),
    ("11112222333344445555", "**5555"),
    ("", ""),
    ("123", "123"),
])
def test_get_mask_account(account, expected):
    """Тест маскирования номера счёта"""
    assert get_mask_account(account) == expected

