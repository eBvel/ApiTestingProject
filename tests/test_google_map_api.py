import pytest
from requests import Response

from tests.conftest import expected_positive_get_token
from utils.validation import ValueValidation


@pytest.mark.usefixtures("session_connection")
class TestGoogleMapAPI:
    def test_create_location(
            self,
            default_body,
            expected_positive_post_token
    ):
        print("Create location (POST)")
        post_response : Response = self.api.create_location(default_body)
        ValueValidation.compare_values(
            "POST status-code",
            post_response.status_code,
            200
        )
        ValueValidation.compare_response_token(
            post_response,
            expected_positive_post_token
        )
        ValueValidation.compare_values(
            "POST status",
            post_response.json().get('status'),
            "OK"
        )

    def test_get_location(self, default_body, expected_positive_get_token):
        print("Create location (POST)")
        post_response: Response = self.api.create_location(default_body)

        print("Get location (GET-POST)")
        get_response: Response = self.api.get_location(
            post_response.json().get('place_id')
        )
        ValueValidation.compare_values(
            "GET status-code",
            get_response.status_code,
            200
        )
        ValueValidation.compare_response_token(
            get_response,
            expected_positive_get_token
        )
        ValueValidation.compare_values(
            "GET address",
            get_response.json().get('address'),
            default_body.get('address')
        )

    def test_update_location(
            self,
            default_body,
            make_body_for_update_location,
            expected_positive_put_token
    ):
        print("Create location (POST)")
        post_response: Response = self.api.create_location(default_body)

        print("Update location (POST-PUT)")
        body = make_body_for_update_location(
            post_response.json().get('place_id')
        )
        put_response: Response = self.api.update_location(body)
        ValueValidation.compare_values(
            "PUT status-code",
            put_response.status_code,
            200
        )
        ValueValidation.compare_response_token(
            put_response,
            expected_positive_put_token
        )
        ValueValidation.compare_values(
            "PUT msg",
            put_response.json().get('msg'),
            "Address successfully updated"
        )

    def test_delete_location(
            self,
            default_body,
            make_body_for_delete_location,
            expected_positive_delete_token,
            expected_negative_get_token
    ):
        print("Create location (POST)")
        post_response: Response = self.api.create_location(default_body)
        place_id = post_response.json().get('place_id')

        print("Delete location (POST-DELETE)")
        body = make_body_for_delete_location(place_id)
        delete_response : Response = self.api.delete_location(body)
        ValueValidation.compare_values(
            "DELETE status-code",
            delete_response.status_code,
            200
        )
        ValueValidation.compare_response_token(
            delete_response,
            expected_positive_delete_token
        )
        ValueValidation.compare_values(
            "DELETE status",
            delete_response.json().get('status'),
            "OK"
        )

        print("Get location (POST-DELETE-GET)")
        get_response : Response = self.api.get_location(place_id)
        ValueValidation.compare_values(
            "GET status-code",
            get_response.status_code,
            404
        )
        ValueValidation.compare_response_token(
            get_response,
            expected_negative_get_token
        )
        ValueValidation.search_word_in_text(
            "GET msg",
            get_response.json().get('msg'),
            "failed"
        )