import requests


class CustomRequests:
    headers = {"Content-type": "application/json"}
    cookie = {}

    @staticmethod
    def get(url):
        return requests.get(
            url,
            headers=CustomRequests.headers,
            cookies=CustomRequests.cookie
        )

    @staticmethod
    def post(url, body):
        return requests.post(
            url, json=body,
            headers=CustomRequests.headers,
            cookies=CustomRequests.cookie
        )

    @staticmethod
    def put(url, body):
        return requests.put(
            url,
            json=body,
            headers=CustomRequests.headers,
            cookies=CustomRequests.cookie
        )

    @staticmethod
    def delete(url, body):
        return requests.delete(
            url,
            json=body,
            headers=CustomRequests.headers,
            cookies=CustomRequests.cookie
        )