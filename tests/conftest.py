import pytest
from utils.json_manager import JsonManager
from os.path import abspath


@pytest.fixture
def default_body():
    return JsonManager.read(
        abspath("..") + "\\google_map_data\\default_location_body.json"
    )
