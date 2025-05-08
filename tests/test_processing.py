import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def valid_filter_by_state() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def valid_filter_by_state_executed() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def valid_filter_by_state_canceled() -> list[dict]:
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def invalid_filter_by_state() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXE", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "date": "2018-10-14T08:21:33.419441"},
    ]


def test_valid_filter_by_state_f(
    valid_filter_by_state: list[dict],
    valid_filter_by_state_executed: list[dict],
    valid_filter_by_state_canceled: list[dict],
) -> None:
    assert filter_by_state(valid_filter_by_state) == valid_filter_by_state_executed
    assert filter_by_state(valid_filter_by_state, "CANCELED") == valid_filter_by_state_canceled


def test_invalid_filter_by_state_f(invalid_filter_by_state: list[dict]) -> None:
    assert filter_by_state(invalid_filter_by_state) == "Ошибка"


@pytest.fixture
def valid_sort_by_date() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:20:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:34.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.420441"},
    ]


@pytest.fixture
def valid_sort_by_date_result_rev_true() -> list[dict]:
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:20:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.420441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:34.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def valid_sort_by_date_result_rev_false() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:34.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.420441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:20:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_valid_sort_by_date_f(
    valid_sort_by_date: list[dict],
    valid_sort_by_date_result_rev_true: list[dict],
    valid_sort_by_date_result_rev_false: list[dict],
) -> None:
    assert sort_by_date(valid_sort_by_date) == valid_sort_by_date_result_rev_true
    assert sort_by_date(valid_sort_by_date, False) == valid_sort_by_date_result_rev_false
