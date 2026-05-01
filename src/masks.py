def get_mask_card_number(card_number: str) -> str:
    """Функция get_mask_card_number принимает на вход номер карты в виде строки"""
    # Убираем все пробелы из карты
    cleaned_number = card_number.replace(" ", "")

    if len(cleaned_number) != 16:
        print("Номер карты должен содержать 16 цифр")
        return ""  # или можно вернуть исходную строку

    # Маскируем номер: первые 6 цифр, затем 6 звездочек, последние 4 цифры
    masked = f"{cleaned_number[:6]}******{cleaned_number[-4:]}"
    return masked


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета: видны только последние 4 цифры, перед ними **"""
    # Берем последние 4 цифры, перед ними ставим две звездочки
    return f"**{account_number[-4:]}"
