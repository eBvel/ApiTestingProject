from dataclasses import dataclass


@dataclass
class GoogleMapEndPoints:
    base_url = "https://rahulshettyacademy.com"
    key_param: str = "?key=qaclick123"
    url_of_create_location : str = \
        f"{base_url}/maps/api/place/add/json{key_param}"
    url_of_edit_location : str = \
        f"{base_url}/maps/api/place/update/json{key_param}"
    url_of_get_location : str = \
        f"{base_url}/maps/api/place/get/json{key_param}&place_id="
    url_of_delete_location : str = \
        f"{base_url}/maps/api/place/delete/json{key_param}"