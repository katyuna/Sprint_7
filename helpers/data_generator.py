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

def generate_create_courier_payload():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    
    payload = {"login": login, "password": password,"firstName": first_name}

    return payload