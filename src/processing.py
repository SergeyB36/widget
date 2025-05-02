def filter_by_state(filter_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция принимает список словарей
    и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей,
    содержащий только те словари, у которых ключ state соответствует указанному значению
    :param filter_list: список словарей
    :param state: параметр фильтра (по умолчанию 'EXECUTED')
    :return: отфильтрованный список словарей
    """
    new_list_dict = []
    for i_dict in filter_list:
        if i_dict["state"] == state:
            new_list_dict.append(i_dict)
    return new_list_dict


def sort_by_date(sort_list: list[dict], ascending: bool = True) -> list[dict]:
    """
    Функция принимает список словарей
    и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
    Функция возвращает новый список, отсортированный по дате
    :param sort_list:список словарей
    :return: отсортированный по дате список словарей
    """
    sorted_list = sorted(sort_list, key=lambda sorted_key: sorted_key["date"][:10], reverse=not ascending)
    return sorted_list
