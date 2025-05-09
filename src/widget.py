from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """
    Функция обработки данных о карте и счете
    """

    try:
        name, number = account_card.rsplit(" ", 1)
    except ValueError:
        return "Ошибка ввода"

    # проверка выбора функции обработки данных
    # выбор обработки счета и проверки ошибки в номере счета
    if name.lower() in ["счет", "счёт"] and get_mask_account(number) != "Ошибка ввода":
        return name + " " + get_mask_account(number)

    # выбор обработки карты
    else:
        # обработка ошибки в номере карты
        if get_mask_card_number(number) == "Ошибка ввода":
            return "Ошибка ввода"

        # обработка корректного названия карты
        if name.isalpha():
            return name + " " + get_mask_card_number(number)
        # обработка названия карты, состоящего из нескольких слов
        elif " " in name:
            if "".join(name.split()).isalpha():
                return name + " " + get_mask_card_number(number)
    # если обработка все-таки не произошла
    return "Ошибка ввода"


def get_date(date_string: str) -> str:
    """
    Функция преобразования формата даты
    "ГГГГ-ММ-ДД" -> "ДД.ММ.ГГГГ"
    """
    # Проверка корректности структуры поступающих данных: "XXXX-XX-XX" или "XXXX-XX-X"
    if len(date_string) < 10:
        return "Ошибка ввода"
    date_need = date_string[:10]
    # Проверка наличия в структуре данных нужного количества разделителей
    if date_need.count("-") != 2:
        return "Ошибка ввода"
    date_list = date_need.split("-")
    # Проверка наличия в структуре данных трех элементов их длину
    if len(date_list[0]) != 4 or len(date_list[1]) != 2 or len(date_list[2]) != 2:
        return "Ошибка ввода"
    # Проверка наличия в структуре данных только цифр
    for number in date_list:
        if not number.isdigit():
            return "Ошибка ввода"

    # Формируем требуемый порядок данных
    true_date_list = date_list[::-1]

    # Формируем структуру данных
    true_date = ".".join(true_date_list)

    return true_date
