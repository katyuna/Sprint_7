import pytest
import allure
from api.orders_api import OrdersApi
from helpers.data_generator import generate_create_order_payload
from helpers.assertions import assert_status_code, assert_response_json_contains_field

class TestCreateOrder:
    orders_api = OrdersApi()

    @allure.title("Создание заказа, цвет: {color}")
    @allure.description("Создание заказа с одним из цветов — BLACK или GREY или оба или None.")
    @pytest.mark.parametrize("color", [
        pytest.param(["BLACK"], id="black"),
        pytest.param(["GREY"], id="grey"),
        pytest.param(["BLACK", "GREY"], id="black_and_grey"),
        pytest.param(None, id="no_color"),
    ])
    def test_create_order(self, color):
        order_payload = generate_create_order_payload(color)
        response = self.orders_api.create_order(order_payload)
        with allure.step("Проверить статус ответа: 201"):
            assert_status_code(response, 201)
        with allure.step("Проверить, что тело ответа содержит track"):
            assert_response_json_contains_field(response, "track")
