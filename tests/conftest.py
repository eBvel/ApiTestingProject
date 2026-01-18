import pytest
from utils.api import GoogleMapAPI
from utils.json_manager import JsonManager
from os.path import abspath
from requests import Session


@pytest.fixture(scope="class")
def session_connection(request):
    print("OPEN SESSION")
    with Session() as session:
        request.cls.api = GoogleMapAPI(session)
        yield
    print("CLOSE SESSION")


@pytest.fixture
def default_body():
    return JsonManager.read(
        abspath("..") + "\\google_map_data\\default_location_body.json"
    )


@pytest.fixture
def make_body_for_update_location():
    def _body_for_update_location(place_id):
        return {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
    return _body_for_update_location


@pytest.fixture
def make_body_for_delete_location():
    def _body_for_delete_location(place_id):
        return {"place_id": place_id}
    return _body_for_delete_location