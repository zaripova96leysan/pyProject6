def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты: первые 4 цифры, потом 6 звёздочек, потом последние 4 цифры"""
    if not card_number:
        return ""
    if len(card_number) < 16:
        return card_number
    # ПРАВИЛЬНО: первые 4 цифры + ****** + последние 4 цифры
    return card_number[:4] + "******" + card_number[-4:]


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счёта: две звёздочки и последние 4 цифры"""
    if not account_number:
        return ""  # Пустая строка возвращает пустую строку
    if len(account_number) < 4:
        return account_number
    # ПРАВИЛЬНО: ** + последние 4 цифры
    return "**" + account_number[-4:]