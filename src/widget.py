from masks import get_mask_card_number
from masks import get_mask_account
def mask_account_card(account_card: str):
    name, number = account_card.rsplit(' ', 1)
    if name == 'Счет':
        return name + get_mask_account(number)