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
