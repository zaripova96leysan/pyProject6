from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_info: str) -> str:
    """ Принимает строку с типом и номером карты/счета, возвращает замаскированный номер"""
    # Разделяем строку на слова
    parts = card_or_account_info.split()

    # Последний элемент — это номер
    number = parts[-1]

    # Всё остальное — название (могут быть несколько слов: "Visa Platinum")
    name_parts = parts[:-1]
    name = " ".join(name_parts)

    # Определяем, карта это или счёт
    if name.lower().startswith("счет"):
        # Для счёта используем функцию из masks.py
        masked_number = get_mask_account(number)
    else:
        # Для карты используем другую функцию
        masked_number = get_mask_card_number(number)

    return f"{name} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Преобразует строку с датой из формата ISO в формат "ДД.ММ.ГГГГ".
    """
    # Берём только часть до буквы T
    date_part = date_string.split("T")[0]
    # Разделяем на год, месяц, день
    year, month, day = date_part.split("-")
    # Возвращаем в формате ДД.ММ.ГГГГ
    return f"{day}.{month}.{year}"
