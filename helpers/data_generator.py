import requests
import random
import string


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


def register_new_courier_and_return_login_password():
    """
    Метод регистрации нового курьера возвращает список из логина и пароля,
    если регистрация не удалась, возвращает пустой список
    :return: список из логина и пароля
    """

    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post('https://qa-scooter.education-services.ru/api/v1/courier', data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass