import pytest
import allure
from api.base_api import BaseApi
from helpers.assertions import assert_status_code, assert_response_error_message, assert_response_json_data
from helpers.routes import CREATE_COURIER_URL, BASE_URL


class TestCreateCourier:
    base_api = BaseApi(BASE_URL)

    @allure.title("Курьера можно создать.")
    @allure.description("При передаче валидных данных курьер успешно создается "
                        "и возвращается статус 201")
    def test_create_courier_successful_and_status_code_is_201_created(self, courier_payload):
        response = self.base_api.send_post_request(CREATE_COURIER_URL, json=courier_payload)
        assert_status_code(response, 201)

    @allure.title("Нельзя создать двух одинаковых курьеров.")
    def test_it_is_impossible_to_create_two_same_couriers(self, courier_payload):
        response = self.base_api.send_post_request(CREATE_COURIER_URL, json=courier_payload)
        response_double = self.base_api.send_post_request(CREATE_COURIER_URL, json=courier_payload)

        with allure.step("Проверить, что первый курьер создан: статус 201"):
            assert_status_code(response, 201)
        with allure.step("Проверить, что повторный курьер не создан: статус 409"):
            assert_status_code(response_double, 409)

    @allure.title("Чтобы создать курьера, нужно передать в ручку все обязательные поля.")
    def test_it_is_obligatorily_to_send_all_field_to_create_courier(self, courier_payload):
        payload_login_password = {"login": courier_payload["login"], "password": courier_payload["password"]}
        response = self.base_api.send_post_request(CREATE_COURIER_URL, json=payload_login_password)
        assert_status_code(response, 201)

    @allure.title("Если одного из обязательных полей нет, запрос возвращает ошибку.")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_without_required_field_returns_400(self, courier_payload, missing_field):
        payload = courier_payload.copy()
        del payload[missing_field]
        response = self.base_api.send_post_request(CREATE_COURIER_URL, json=payload)

        with allure.step("Проверить статус ответа: 400"):
            assert_status_code(response, 400)
        with allure.step("Проверить текст ошибки в теле ответа"):
            assert_response_error_message(response, "Недостаточно данных для создания учетной записи")

    @allure.title("Успешный запрос возвращает {{\"ok\":true}}.")
    def test_success_request_returns_ok_true(self, courier_payload):
        response = self.base_api.send_post_request(CREATE_COURIER_URL, json=courier_payload)
        assert_response_json_data(response, {"ok": True})
