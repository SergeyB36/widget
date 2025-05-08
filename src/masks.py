def get_mask_card_number(card_number: str) -> str:
    """
    Функция
    маскировки номера банковской карты
    """
    # проверяем что номер состоит только из цифр и его длина равна 16. Иначе возвращаем ошибку.
    if not card_number.isdigit():
        return "Ошибка ввода"
    if len(card_number) != 16:
        return "Ошибка ввода"
    number_mask = card_number[:6] + ("*" * 6) + card_number[12:]
    card_number_mask = number_mask[:4] + " " + number_mask[4:8] + " " + number_mask[8:12] + " " + number_mask[12:]

    return card_number_mask


def get_mask_account(account_number: str) -> str:
    """
    Функция
    маскировки номера банковского номера
    """
    # проверяем что номер состоит только из цифр и его длина равна 20. Иначе возвращаем ошибку.
    if not account_number.isdigit():
        return "Ошибка ввода"
    if len(account_number) != 20:
        return "Ошибка ввода"

    account_number_mask = "**" + account_number[-4:]

    return account_number_mask
