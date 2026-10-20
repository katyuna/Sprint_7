import allure
from api.orders_api import OrdersApi
from helpers.assertions import assert_status_code, assert_response_json_contains_field

class TestOrderList:
    orders_api = OrdersApi()

    @allure.title("Получить список заказов.")
    def test_get_orders_list_returns_list_of_orders(self):
        response = self.orders_api.get_orders_list()
        with allure.step("Проверить статус ответа: 200"):
            assert_status_code(response, 200)
        with allure.step("Проверить, что в ответе есть поле orders"):
            assert_response_json_contains_field(response, "orders")
        with allure.step("Проверить, что orders - список"):
            assert isinstance(response.json()["orders"], list), f'Поле "orders" должно быть списком, получено {response.json()["orders"]}'
