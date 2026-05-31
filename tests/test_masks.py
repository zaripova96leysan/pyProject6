import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.masks import get_mask_card_number, get_mask_account  # noqa: E402


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567890123456", "1234******3456"),
        ("1111222233334444", "1111******4444"),
        ("", ""),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account, expected",
    [
        ("12345678901234567890", "**7890"),
        ("11112222333344445555", "**5555"),
        ("", ""),
    ],
)
def test_get_mask_account(account, expected):
    assert get_mask_account(account) == expected


def test_get_mask_card_number_short():
    assert get_mask_card_number("1234") == "1234"
    assert get_mask_card_number("1234567890") == "1234567890"
    assert get_mask_card_number("123456789012345") == "123456789012345"


def test_get_mask_account_short():
    assert get_mask_account("123") == "123"
    assert get_mask_account("12") == "12"
    assert get_mask_account("1") == "1"


def test_get_mask_card_number_boundary():
    assert get_mask_card_number("1234567890123456") == "1234******3456"
    assert get_mask_card_number("123456789012345") == "123456789012345"
    assert get_mask_card_number("12345678901234567") == "1234******4567"


def test_get_mask_account_boundary():
    assert get_mask_account("1234") == "**1234"
    assert get_mask_account("123") == "123"
    assert get_mask_account("12345") == "**2345"
