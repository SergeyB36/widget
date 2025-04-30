def get_mask_card_number(card_number: str) -> str:
    """
    Функция
    маскировки номера банковской карты
    """

    number_mask = card_number[:6] + ("*" * 6) + card_number[12:]
    card_number_mask = number_mask[:4] + " " + number_mask[4:8] + " " + number_mask[8:12] + " " + number_mask[12:]

    return card_number_mask


def get_mask_account(account_number: str) -> str:
    """
    Функция
    маскировки номера банковского номера
    """

    account_number_mask = "**" + account_number[-4:]

    return account_number_mask

print('first commit')