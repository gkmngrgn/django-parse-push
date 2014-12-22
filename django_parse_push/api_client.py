import json
import requests
from django_parse_push.settings import APPLICATION_ID, REST_API_KEY


class ApiClient(object):
    api_url = "https://api.parse.com"
    api_version = "1"

    def __init__(self, application_id, rest_api_key):
        self.application_id = application_id
        self.rest_api_key = rest_api_key

    def request(self, method, url_path, data):
        url = "{}/{}/{}".format(self.api_url, self.api_version, url_path)
        headers = {
            "X-Parse-Application-Id": self.application_id,
            "X-Parse-REST-API-Key": self.rest_api_key,
            "Content-Type": "application/json"
        }
        return requests.request(method=method, url=url, headers=headers, data=json.dumps(data))

    def send_notification(self, data):
        """
        Example data:
            {
                "where": {
                    "channels": "Wall",
                    "deviceType": "android"
                },
                "data": {
                    "alert": "test message"
                }
            }
        """
        return self.request(method="post", url_path="push", data=data)


def get_api_client():
    """
    Shortcut method for get api client with required settings.
    :return: ApiClient object
    """
    api_client = ApiClient(application_id=APPLICATION_ID, rest_api_key=REST_API_KEY)
    return api_client
