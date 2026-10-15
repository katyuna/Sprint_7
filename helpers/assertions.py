from requests import Response

def assert_status_code(response: Response, expected_code: int):
    actual_code = response.status_code
    assert actual_code == expected_code

def assert_response_error_message(response: Response, expected_message: str):
    actual_message = response.json()["message"]
    assert actual_message == expected_message

def assert_response_json_data(response: Response, expected_json: dict):
    actual_json = response.json()
    assert actual_json == expected_json