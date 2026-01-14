from utils.http_methods import CustomRequests
from google_map_data.configuration import GoogleMapEndPoints as end_points


class GoogleMapAPI:
    @staticmethod
    def create_location(body):
        url = end_points.url_of_create_location
        print(url)
        response = CustomRequests.post(url, body)
        print(response.text)
        return response