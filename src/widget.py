from masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """
    Функция обработки данных о карте и счете
    """
    name, number = account_card.rsplit(" ", 1)
    if name == "Счет":
        mask = name + " " + get_mask_account(number)

    else:
        mask = name + " " + get_mask_card_number(number)

    return mask
