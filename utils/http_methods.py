from requests import Session
from utils.logger import logger_decorator


class CustomRequests:
    def __init__(self, session):
        self.session : Session = session
        self.headers = {"Content-type": "application/json"}
        self.cookie = {}

    @logger_decorator
    def get(self, url):
        return self.session.get(
            url,
            headers=self.headers,
            cookies=self.cookie
        )

    @logger_decorator
    def post(self, url, body):
        return self.session.post(
            url, json=body,
            headers=self.headers,
            cookies=self.cookie
        )

    @logger_decorator
    def put(self, url, body):
        return self.session.put(
            url,
            json=body,
            headers=self.headers,
            cookies=self.cookie
        )

    @logger_decorator
    def delete(self, url, body):
        return self.session.delete(
            url,
            json=body,
            headers=self.headers,
            cookies=self.cookie
        )