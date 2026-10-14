from requests import Response

def assert_status_code(response: Response, expected_code: int):
    actual_code = response.status_code
    assert actual_code == expected_code, \
    f'Ожидался статус код "{expected_code}", но получен {actual_code}. Тело ответа {response.text}'