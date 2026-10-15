from requests import Response

def assert_status_code(response: Response, expected_code: int):
    actual_code = response.status_code
    assert actual_code == expected_code, \
        f'Ожидался код {expected_code}, получен {actual_code}.'

def assert_response_error_message(response: Response, expected_message: str):
    actual_message = response.json()["message"]
    assert actual_message == expected_message, \
        f'Ожидалось сообщение "{expected_message}", получено "{actual_message}"'

def assert_response_json_data(response: Response, expected_json: dict):
    actual_json = response.json()
    assert actual_json == expected_json, \
        f'Ожидалось тело ответа {expected_json}, получено {actual_json}'


def assert_response_json_contains_field(response: Response, field_name: str):
    actual_json = response.json()
    assert field_name in actual_json, \
        f'В теле ответа нет поля "{field_name}", получено {actual_json}'
