import pytest

from src.widget import get_date, mask_account_card


# Тесты для mask_account_card
@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("Счет 12345678901234567890", "Счет **7890"),
        ("Карта 1234567812345678", "Карта 1234 56** **** 5678"),
        ("Счет 00000000000000000000", "Счет **0000"),
        ("Карта Visa 1111222233334444", "Карта Visa 1111 22** **** 4444"),
    ],
)
def test_mask_account_card(input_data: str, expected_output: str) -> None:
    assert mask_account_card(input_data) == expected_output


@pytest.fixture
def invalid_input_data() -> list:
    return [
        "Ошибка ввода",
        "Счет",
        "Карта Visa",
        "Счет 1234567890123456789",
        "Карта 123456781234567",
    ]


def test_mask_account_card_invalid(invalid_input_data: list) -> None:
    for input_data in invalid_input_data:
        assert mask_account_card(input_data) == "Ошибка ввода"


# Тесты для get_date
@pytest.mark.parametrize(
    "input_date, expected_output",
    [
        ("2023-10-1:data", "1.10.2023"),
        ("2023-10-01:data", "01.10.2023"),
        ("2023-01-151111", "15.01.2023"),
        ("2022-12-31t    ", "31.12.2022"),
        ("2022-12-3    ", "3.12.2022"),
        ("2022-12-3T   ", "3.12.2022"),
    ],
)
def test_get_date_valid(input_date: str, expected_output: str) -> None:
    assert get_date(input_date) == expected_output


@pytest.fixture
def invalid_date_data() -> list:
    return [
        "aaaa-ss-f1",
        "2022-123-1t",
        "",
        "12-12-1212",
        "2022 12 31",
        "2022-12/31",
        "2022/12-3",
        "2023/10/01",
        "Ошибка ввода",
    ]


def test_get_date_invalid(invalid_date_data: list) -> None:
    for date_data in invalid_date_data:
        assert get_date(date_data) == "Ошибка ввода"
