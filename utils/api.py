from utils.http_methods import CustomRequests
from google_map_data.configuration import GoogleMapEndPoints as end_points


class GoogleMapAPI:
    def __init__(self, session):
        self.session = session
        self.custom_requests = CustomRequests(session)

    def create_location(self, body):
        url = end_points.url_of_create_location
        print(url)
        response = self.custom_requests.post(url, body)
        print(response.text)
        return response

    def get_location(self, place_id):
        url = end_points.url_of_get_location+place_id
        print(url)
        response = self.custom_requests.get(url)
        print(response.text)
        return response

    def update_location(self, body):
        url = end_points.url_of_edit_location
        print(url)
        response = self.custom_requests.put(url, body)
        print(response.text)
        return response

    def delete_location(self, body):
        url = end_points.url_of_delete_location
        print(url)
        response = self.custom_requests.delete(url, body)
        print(response.text)
        return response