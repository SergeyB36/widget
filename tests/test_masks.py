import pytest

from src.masks import get_mask_account, get_mask_card_number


# тесты для get_mask_card_number
@pytest.fixture
def invalid_card_number() -> list:
    return ["12345678901212", "123456789o121234", "", "123456789012345?", "12345678901234  ", "1234 5678 9012 3456"]


@pytest.fixture
def valid_card_number() -> list[tuple]:
    return [
        ("1234567890121211", "1234 56** **** 1211"),
        ("0987676543245674", "0987 67** **** 5674"),
        ("1234567890123456", "1234 56** **** 3456"),
    ]


def test_invalid_mask_card_number(invalid_card_number: list) -> None:
    for number in invalid_card_number:
        assert get_mask_card_number(number) == "Ошибка ввода"


def test_valid_mask_card_number(valid_card_number: list[tuple]) -> None:
    for number, expected in valid_card_number:
        assert get_mask_card_number(number) == expected


# тесты для get_mask_account
@pytest.fixture
def invalid_account_number() -> list:
    return [
        "12345678901212",
        "123456789o1212341212",
        "",
        "1234567890123121245?",
        "123456789011212234  ",
        "1234 5678 9012 3456 1234",
    ]


@pytest.fixture
def valid_account_number() -> list[tuple]:
    return [("12345678901234561212", "**1212"), ("65342678901234563445", "**3445"), ("45675688901234563987", "**3987")]


def test_invalid_mask_card_account(invalid_account_number: list) -> None:
    for number in invalid_account_number:
        assert get_mask_account(number) == "Ошибка ввода"


def test_valid_account_number(valid_account_number: list) -> None:
    for number, expected in valid_account_number:
        assert get_mask_account(number) == expected
