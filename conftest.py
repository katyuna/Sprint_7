import pytest
from helpers.data_generator import generate_create_courier_payload
from api.courier_api import CourierApi

@pytest.fixture
def courier_payload():
    payload = generate_create_courier_payload()

    yield payload  

    courier_api = CourierApi()
    login_response = courier_api.login_courier(payload["login"], payload["password"])
    if login_response.status_code == 200:  
        courier_id = login_response.json()["id"]
        courier_api.delete_courier(courier_id)


@pytest.fixture
def registered_courier():
    courier_api = CourierApi()
    login_pass = courier_api.register_new_courier_and_return_login_password()

    yield login_pass

    login_response = courier_api.login_courier(login_pass[0], login_pass[1])
    if login_response.status_code == 200:
        courier_id = login_response.json()["id"]
        courier_api.delete_courier(courier_id)
