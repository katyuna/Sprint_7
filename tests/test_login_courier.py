import pytest
import allure
from api.base_api import BaseApi
from helpers.assertions import assert_status_code, assert_response_error_message, assert_response_json_data, assert_response_json_contains_field
from helpers.routes import LOGIN_COURIER_URL, BASE_URL


class TestLoginCourier:
    base_api = BaseApi(BASE_URL)

    @allure.title("Курьер может авторизоваться.")
    def test_courier_can_login(self, registered_courier):
        payload_login_password = {"login": registered_courier[0], "password": registered_courier[1]}
        response = self.base_api.send_post_request(LOGIN_COURIER_URL, json=payload_login_password)
        with allure.step("Проверить, что курьер авторизовался: статус 200."):
            assert_status_code(response, 200)
        with allure.step("Проверить, что успешный запрос возвращает id."):  
            assert_response_json_contains_field(response, 'id') 

    @allure.title("Для авторизации нужно передать все обязательные поля.")
    def test_it_is_obligatorily_to_send_all_fields_to_login(self, courier_payload):
        pass

    @allure.title("Система вернёт ошибку, если неправильно указать логин или пароль.")
    def test_login_with_wrong_login_or_password_returns_error(self, courier_payload):
        pass

    @allure.title("Если какого-то поля нет, запрос возвращает ошибку.")
    def test_login_without_required_field_returns_error(self, courier_payload):
        pass

    @allure.title("Если авторизоваться под несуществующим пользователем, запрос возвращает ошибку.")
    def test_login_with_nonexistent_courier_returns_error(self):
        pass

    @allure.title("Успешный запрос возвращает id.")
    def test_success_login_returns_id(self, courier_payload):
        pass
