def filter_by_state(my_list, state='EXECUTED'):
    """Функция, которая принимает список словарей и возвращает отфильтрованный список"""
    result = []

    for list in my_list:
        if list.get('state') == state:
            result.append(list)

    return result


def sort_by_date(data, reverse=True):
    """Функция, принимающая список словарей и возвращает отсортированный по дате"""
        return sorted(data, key=lambda x: x['date'], reverse=reverse)



