from datetime import datetime
from requests import Response
from os import environ, path


class Logger:
    file_name = f"../logs/log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

    @classmethod
    def write_log_to_file(cls, data: str):
        try:
            mode = "a"
            if not path.exists(cls.file_name):
                mode = "w"

            with open(cls.file_name, mode, encoding='UTF-8') as logger_file:
                logger_file.write(data)
        except FileNotFoundError as e:
            print(f"File {cls.file_name} not found!\n{e}")

    @classmethod
    def add_request(cls, url, request_method):
        test_name = environ.get("PYTEST_CURRENT_TEST")

        data = (f"\n<--------------------\nTest: {test_name}\n"
                f"Time: {datetime.now()}\nRequest method: {request_method}\n"
                f"Request URL: {url}\n")

        cls.write_log_to_file(data)

    @classmethod
    def add_response(cls, response: Response):
        headers = response.headers
        cookies = dict(response.cookies)

        data = (f"\nResponse code: {response.status_code}\n"
                f"Response text: {response.text}\nResponse headers: {headers}"
                f"\nResponse cookie: {cookies}\n-------------------->\n")

        cls.write_log_to_file(data)