from requests import Response
from utils.api import GoogleMapAPI as api


def compare_values(value_name, current_value, expected_value):
    print(f"\n{value_name}\n{current_value=}\n{expected_value=}")
    assert current_value == expected_value, f"Incorrect value {current_value}"
    print(f"PASSED: Value '{current_value}' is correct!")


class TestGoogleMapAPI:
    def test_create_location(self, default_body):
        print("Create location (POST)")
        post_response : Response = api.create_location(default_body)
        compare_values("POST status-code", post_response.status_code, 200)

        print("Get location (GET)")
        get_response : Response = api.get_location(post_response.json().get('place_id'))
        compare_values("GET status-code", get_response.status_code, 200)