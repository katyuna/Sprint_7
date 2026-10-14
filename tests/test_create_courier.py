import allure
from helpers.data_generator import generate_random_string
import pytest

from api import base_api
from api.base_api import BaseApi
from helpers.assertions import assert_status_code
from helpers .routes import CREATE_COURIER_URL


class TestCreateCourier:
    base_api = BaseApi()

    @allure.title("Курьера можно создать.")
    @allure.description("При передаче валидных данных курьер успешно создается "
                        "и возвращается статус 201")
    def test_create_courier_successful_and_status_code_is_201_created(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        assert assert_status_code(
            base_api.send_get_request(CREATE_COURIER_URL, payload), 201)

    @allure.title("Нельзя создать двух одинаковых курьеров.")
    def test_it_is_impossible_to_create_two_same_couriers(self):
        pass

    @allure.title("Чтобы создать курьера, нужно передать в ручку все обязательные поля.")
    def test_it_is_obligatorily_to_send_all_field_to_create_courier(self):
        pass




    @allure.title("Успешный запрос возвращает {\"ok\":true}.")
    def test_success_request_returns_ok_true(self):
        pass

    @allure.title("Если одного из полей нет, запрос возвращает ошибку.")
    def rrr(self):
        pass

    @allure.title("Если создать пользователя с логином, который уже есть, возвращается ошибка.")
    def sdd(self):
        pass

    @allure.title("Нельзя создать двух одинаковых курьеров.")
    def ggg(self):
        pass

