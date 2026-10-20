import pytest
import allure
from api.courier_api import CourierApi
from helpers.assertions import assert_status_code, assert_response_error_message, assert_response_json_contains_field
from helpers.data import NOT_ENOUGH_DATA_TO_LOGIN, ACCOUNT_NOT_FOUND
from helpers.data_generator import generate_random_string


class TestLoginCourier:
    courier_api = CourierApi()

    @allure.title("Курьер может авторизоваться.")
    def test_courier_can_login(self, registered_courier):
        response = self.courier_api.login_courier(registered_courier["login"], registered_courier["password"])
        with allure.step("Проверить, что курьер авторизовался: статус 200."):
            assert_status_code(response, 200)
        with allure.step("Проверить, что успешный запрос возвращает id."):
            assert_response_json_contains_field(response, 'id')

    @allure.title("Для авторизации нужно передать все обязательные поля. Если какого-то поля нет, запрос возвращает ошибку.")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_courier_without_required_field_returns_400(self, registered_courier, missing_field):
        payload = registered_courier.copy()
        del payload[missing_field]
        response = self.courier_api.login_courier(payload.get("login"), payload.get("password"))
        with allure.step("Проверить статус ответа: 400."):
            assert_status_code(response, 400)
        with allure.step("Проверить текст ошибки в теле ответа."):
            assert_response_error_message(response, NOT_ENOUGH_DATA_TO_LOGIN)

    @allure.title("Система вернёт ошибку, если неправильно указать логин или пароль.")
    @pytest.mark.parametrize("wrong_field", ["login", "password"])
    def test_login_with_wrong_login_or_password_returns_error(self, registered_courier, wrong_field):
        payload = registered_courier.copy()
        payload[wrong_field] = payload[wrong_field] + "wrong"
        response = self.courier_api.login_courier(payload.get("login"), payload.get("password"))
        with allure.step("Проверить статус ответа: 404."):
            assert_status_code(response, 404)
        with allure.step("Проверить текст ошибки в теле ответа."):
            assert_response_error_message(response, ACCOUNT_NOT_FOUND)

    @allure.title("Если авторизоваться под несуществующим пользователем, запрос возвращает ошибку.")
    def test_login_with_nonexistent_courier_returns_error(self):
        payload = {"login": generate_random_string(10), "password": generate_random_string(10)}
        response = self.courier_api.login_courier(payload.get("login"), payload.get("password"))
        with allure.step("Проверить статус ответа: 404."):
            assert_status_code(response, 404)
        with allure.step("Проверить текст ошибки в теле ответа."):
            assert_response_error_message(response, ACCOUNT_NOT_FOUND)
