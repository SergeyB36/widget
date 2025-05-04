import pytest

from src.masks import get_mask_card_number


@pytest.mark.parametrize(
    "number, expected",
    [
        ("12345678901212", "Не верный номер карты"),
        ("123456789o121234", "Не верный номер карты"),
        ("", "Не верный номер карты"),
        ("123456789012345?", "Не верный номер карты"),
        ("12345678901234  ", "Не верный номер карты"),
        ("1234 5678 9012 3456", "Не верный номер карты"),
        ("1234567890123456", "1234 56** **** 3456"),
    ],
)
def test_true_work_mask_card_number(number, expected):
    assert get_mask_card_number(number) == expected
