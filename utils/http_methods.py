from requests import Session


class CustomRequests:
    def __init__(self, session):
        self.session : Session = session
        self.headers = {"Content-type": "application/json"}
        self.cookie = {}

    def get(self, url):
        return self.session.get(
            url,
            headers=self.headers,
            cookies=self.cookie
        )

    def post(self, url, body):
        return self.session.post(
            url, json=body,
            headers=self.headers,
            cookies=self.cookie
        )

    def put(self, url, body):
        return self.session.put(
            url,
            json=body,
            headers=self.headers,
            cookies=self.cookie
        )

    def delete(self, url, body):
        return self.session.delete(
            url,
            json=body,
            headers=self.headers,
            cookies=self.cookie
        )