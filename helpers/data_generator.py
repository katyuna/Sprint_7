import random
import string
from datetime import date, timedelta


def generate_random_string(length):
    """
    Метод генерирует строку, состоящую только из букв нижнего регистра,
    в качестве параметра передаём длину строки
    :param length:
    :return: случайная строка
    """
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_create_courier_payload():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {"login": login, "password": password, "firstName": first_name}

    return payload


def generate_tomorrow_date():
    """
    :return: завтрашняя дата в формате YYYY-MM-DD
    """
    return (date.today() + timedelta(days=1)).isoformat()


def generate_create_order_payload(color=None):
    """
    Генерирует тело запроса на создание заказа
    :param color: список цветов, например ["BLACK"], ["GREY"], ["BLACK", "GREY"];
                  None - поле color не передаётся
    :return: словарь с данными заказа
    """
    order_payload = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": generate_tomorrow_date(),
        "comment": "Saske, come back to Konoha",
    }
    if color is not None:
        order_payload["color"] = color

    return order_payload