import pytest
from utils.json_manager import JsonManager
from os.path import abspath


@pytest.fixture
def default_body():
    return JsonManager.read(
        abspath("..") + "\\google_map_data\\default_location_body.json"
    )


@pytest.fixture
def make_body_for_update_location():
    def _make_body_for_update_location(place_id):
        return {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
    return _make_body_for_update_location