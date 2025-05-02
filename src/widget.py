from typing import Any

from masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> Any:
    """
    Функция обработки данных о карте и счете
    """
    name, number = account_card.rsplit(" ", 1)
    if name == "Счет":
        mask = name + " " + get_mask_account(number)

    else:
        mask = name + " " + get_mask_card_number(number)

    return mask


def get_date(date_string: str) -> str:
    """
    Функция преобразования формата даты
    :rtype: str
    """
    date_need = date_string[:10]
    date_list = []
    date_list = date_need.split("-")
    sort_date_list = date_list[::-1]
    return ".".join(sort_date_list)
