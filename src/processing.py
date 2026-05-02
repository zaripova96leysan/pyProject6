def filter_by_state(spisok, state='EXECUTED'):
    """Функция, которая принимает список словарей и возвращает отфильтрованный список"""
    result = []

    for voc in spisok:
        if voc.get('state') == state:
            result.append(voc)

    return result


def sort_by_date(data, reverse=True):
    """Функция, принимающая список словарей и возвращает отсортированный по дате"""
    return sorted(data, key=lambda x: x['date'], reverse=reverse)


