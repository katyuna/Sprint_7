import pytest
import allure
from api.courier_api import CourierApi
from helpers.assertions import assert_status_code, assert_response_error_message, assert_response_json_data
from helpers.data import NOT_ENOUGH_DATA_TO_CREATE_COURIER, LOGIN_ALREADY_IN_USE
from helpers.data_generator import generate_create_courier_payload


class TestCreateCourier:
    courier_api = CourierApi()

    @allure.title("Курьера можно создать.")
    @allure.description("При передаче валидных данных курьер успешно создается "
                        "и возвращается статус 201")
    def test_create_courier_successful_and_status_code_is_201_created(self, courier_payload):
        response = self.courier_api.create_courier(courier_payload)
        with allure.step("Проверить, что курьер создан: статус 201"):
            assert_status_code(response, 201)
        with allure.step("Проверить, что успешный запрос возвращает {{\"ok\":true}}."):
            assert_response_json_data(response, {"ok": True})

    @allure.title("Нельзя создать двух одинаковых курьеров.")
    def test_it_is_impossible_to_create_two_same_couriers(self, courier_payload):
        response = self.courier_api.create_courier(courier_payload)
        response_double = self.courier_api.create_courier(courier_payload)

        with allure.step("Проверить, что первый курьер создан: статус 201"):
            assert_status_code(response, 201)
        with allure.step("Проверить, что повторный курьер не создан: статус 409"):
            assert_status_code(response_double, 409)
            assert_response_error_message(response_double, LOGIN_ALREADY_IN_USE)

    @allure.title("Нельзя создать курьера с логином, который уже есть.")
    def test_create_courier_with_existing_login_returns_409(self, courier_payload):
        response = self.courier_api.create_courier(courier_payload)
        payload_same_login = generate_create_courier_payload()
        payload_same_login["login"] = courier_payload["login"]
        response_same_login = self.courier_api.create_courier(payload_same_login)

        with allure.step("Проверить, что первый курьер создан: статус 201"):
            assert_status_code(response, 201)
        with allure.step("Проверить, что курьер с тем же логином не создан: статус 409"):
            assert_status_code(response_same_login, 409)
        with allure.step("Проверить текст ошибки в теле ответа"):
            assert_response_error_message(response_same_login, LOGIN_ALREADY_IN_USE)

    @allure.title("Чтобы создать курьера, нужно передать в ручку все обязательные поля.")
    def test_it_is_obligatorily_to_send_all_field_to_create_courier(self, courier_payload):
        payload_login_password = {"login": courier_payload["login"], "password": courier_payload["password"]}
        response = self.courier_api.create_courier(payload_login_password)
        assert_status_code(response, 201)

    @allure.title("Если одного из обязательных полей нет, запрос возвращает ошибку.")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_without_required_field_returns_400(self, courier_payload, missing_field):
        payload = courier_payload.copy()
        del payload[missing_field]
        response = self.courier_api.create_courier(payload)

        with allure.step("Проверить статус ответа: 400"):
            assert_status_code(response, 400)
        with allure.step("Проверить текст ошибки в теле ответа"):
            assert_response_error_message(response, NOT_ENOUGH_DATA_TO_CREATE_COURIER)
