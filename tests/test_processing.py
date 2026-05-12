import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.processing import filter_by_state, sort_by_date


# ==================== ФИКСТУРЫ ====================

@pytest.fixture
def sample_transactions():
    """Фикстура с тестовыми транзакциями"""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-03-15T10:00:00"},
        {"id": 2, "state": "PENDING", "date": "2024-03-14T10:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2024-03-16T10:00:00"},
        {"id": 4, "state": "CANCELED", "date": "2024-03-13T10:00:00"},
        {"id": 5, "state": "EXECUTED", "date": "2024-03-12T10:00:00"},
    ]


@pytest.fixture
def transactions_same_date():
    """Фикстура с одинаковыми датами"""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-03-15T10:00:00"},
        {"id": 2, "state": "PENDING", "date": "2024-03-15T10:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2024-03-15T10:00:00"},
    ]


# ==================== ТЕСТЫ ДЛЯ filter_by_state ====================

@pytest.mark.parametrize("state, expected_ids", [
    ("EXECUTED", [1, 3, 5]),
    ("PENDING", [2]),
    ("CANCELED", [4]),
    ("UNKNOWN", []),
])
def test_filter_by_state(sample_transactions, state, expected_ids):
    """Тест фильтрации по статусу"""
    filtered = filter_by_state(sample_transactions, state)
    filtered_ids = [item["id"] for item in filtered]
    assert filtered_ids == expected_ids


def test_filter_by_state_no_key(sample_transactions):
    """Тест: если нет ключа state - функция не падает"""
    wrong_data = sample_transactions + [{"id": 6, "date": "2024-03-15"}]
    result = filter_by_state(wrong_data, "EXECUTED")
    assert len(result) == 3


# ==================== ТЕСТЫ ДЛЯ sort_by_date ====================

def test_sort_by_date_descending(sample_transactions):
    """Тест сортировки по убыванию (новые сначала)"""
    sorted_list = sort_by_date(sample_transactions, reverse=True)  # ← reverse=True
    dates = [item["date"] for item in sorted_list]
    assert dates[0] == "2024-03-16T10:00:00"
    assert dates[-1] == "2024-03-12T10:00:00"


def test_sort_by_date_ascending(sample_transactions):
    """Тест сортировки по возрастанию (старые сначала)"""
    sorted_list = sort_by_date(sample_transactions, reverse=False)  # ← reverse=False
    dates = [item["date"] for item in sorted_list]
    assert dates[0] == "2024-03-12T10:00:00"
    assert dates[-1] == "2024-03-16T10:00:00"


def test_sort_by_date_same_dates(transactions_same_date):
    """Тест: при одинаковых датах порядок не меняется"""
    sorted_list = sort_by_date(transactions_same_date, reverse=True)  # ← reverse=True
    assert sorted_list[0]["id"] == 1
    assert sorted_list[1]["id"] == 2
    assert sorted_list[2]["id"] == 3


def test_sort_by_date_empty_list():
    """Тест: пустой список"""
    result = sort_by_date([], reverse=True)  # ← reverse=True
    assert result == []



def test_sort_by_date_invalid_format():
    """Тест: некорректный формат даты"""
    data = [
        {"id": 1, "date": "not-a-date"},
        {"id": 2, "date": "2024-03-15T10:00:00"},
    ]
    result = sort_by_date(data)
    assert len(result) == 2
