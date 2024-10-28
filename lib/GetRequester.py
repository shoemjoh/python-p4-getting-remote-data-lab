import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # sends get request with the URL - requests.get(URL)
        # return the body of the response - response.body()

        response = requests.get(self.url)
        return response.content

    def load_json(self):
        # this isn't exactly how the lab describes it, but passes the test
        response = requests.get(self.url)
        return response.json()