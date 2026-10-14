import requests


class BaseApi:
    def __init__(self, base_url):
        self.base_url = base_url

    def send_get_request(self, endpoint, params=None):
        url = self.base_url + endpoint
        response = requests.get(url, params=params)
        return response

    def send_post_request(self, endpoint, data=None, json=None):
        url = self.base_url + endpoint
        response = requests.post(url, data=data, json=json)
        return response

    def send_put_request(self, endpoint, json=None):
        url = self.base_url + endpoint
        response = requests.put(url, json=json)
        return response

    def send_delete_request(self, endpoint):
        url = self.base_url + endpoint
        response = requests.delete(url)
        return response
