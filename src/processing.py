from typing import List, Dict, Any


def filter_by_state(spisok: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """Функция, которая принимает список словарей и возвращает отфильтрованный список"""
    result = []
    for voc in spisok:
        if voc.get('state') == state:
            result.append(voc)
    return result


def sort_by_date(data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Функция, принимающая список словарей и возвращает отсортированный по дате список"""
    return sorted(data, key=lambda x: x['date'], reverse=reverse)

