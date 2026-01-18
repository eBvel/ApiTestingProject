import pytest
from requests import Response


def compare_values(value_name, current_value, expected_value):
    print(f"\n{value_name}\n{current_value=}\n{expected_value=}")
    assert current_value == expected_value, f"Incorrect value {current_value}"
    print(f"PASSED: Value '{current_value}' is correct!")


@pytest.mark.usefixtures("session_connection")
class TestGoogleMapAPI:
    def test_create_location(self, default_body):
        print("Create location (POST)")
        post_response : Response = self.api.create_location(default_body)
        compare_values("POST status-code", post_response.status_code, 200)

    def test_get_location(self, default_body):
        print("Create location (POST)")
        post_response: Response = self.api.create_location(default_body)

        print("Get location (GET-POST)")
        get_response: Response = self.api.get_location(post_response.json().get('place_id'))
        compare_values("GET status-code", get_response.status_code, 200)

    def test_update_location(self, default_body, make_body_for_update_location):
        print("Create location (POST)")
        post_response: Response = self.api.create_location(default_body)

        print("Update location (POST-PUT)")
        body = make_body_for_update_location(post_response.json().get('place_id'))
        put_response: Response = self.api.update_location(body)
        compare_values("PUT status-code", put_response.status_code, 200)

    def test_delete_location(
            self,
            default_body,
            make_body_for_delete_location
    ):
        print("Create location (POST)")
        post_response: Response = self.api.create_location(default_body)
        place_id = post_response.json().get('place_id')

        print("Delete location (POST-DELETE)")
        body = make_body_for_delete_location(place_id)
        delete_response : Response = self.api.delete_location(body)
        compare_values("DELETE status-code", delete_response.status_code, 200)

        print("Get location (POST-DELETE-GET)")
        get_response : Response = self.api.get_location(place_id)
        compare_values(
            "GET msg",
            get_response.json().get('msg'),
            "Get operation failed, looks like place_id  doesn't exists"
        )