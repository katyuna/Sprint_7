from helpers.routes import BASE_URL, CREATE_ORDER_URL, ORDER_LIST_URL
from api.base_api import BaseApi


class OrdersApi(BaseApi):
    def __init__(self):
        super().__init__(BASE_URL)

    def create_order(self, payload):
        return self.send_post_request(CREATE_ORDER_URL, json=payload)

    def get_orders_list(self, params=None):
        return self.send_get_request(ORDER_LIST_URL, params=params)
