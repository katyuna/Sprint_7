from helpers.data_generator import generate_random_string
from helpers.routes import CREATE_COURIER_URL, BASE_URL, DELETE_COURIER_URL, LOGIN_COURIER_URL
from api.base_api import BaseApi
from helpers.data_generator import generate_create_courier_payload

class CourierApi:
    base_api = BaseApi(BASE_URL)

    def register_new_courier_and_return_login_password(self):
        """
        Метод регистрации нового курьера возвращает список из логина и пароля,
        если регистрация не удалась - возвращает пустой список
        :return: список из логина и пароля
        """
        login_pass = []

        payload = generate_create_courier_payload()
        
        response = self.base_api.send_post_request(CREATE_COURIER_URL, json=payload)

        if response.status_code == 201:
            login_pass.append(payload["login"])
            login_pass.append(payload["password"])

        return login_pass
    
    def login_courier(self, login, password):
        payload = {"login": login, "password": password}
        return self.base_api.send_post_request(LOGIN_COURIER_URL, json=payload)

    def delete_courier(self, courier_id):
        payload = {"id": str(courier_id)}
        return self.base_api.send_delete_request(f"{DELETE_COURIER_URL}{courier_id}", json=payload)
