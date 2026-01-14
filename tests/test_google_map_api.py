from requests import Response
from utils.api import GoogleMapAPI as api


class TestGoogleMapAPI:
    def test_create_location(self, default_body):
        print("TEST: Create location (POST)")
        response : Response = api.create_location(default_body)
        response_status_code = response.status_code
        print(f"Status-code: {response_status_code}")
        assert response_status_code == 200
        print(f"PASSED: Status code is correct!")