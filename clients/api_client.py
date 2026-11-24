import requests

from config import BASE_URL, REQUEST_TIMEOUT


class APIClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.timeout = REQUEST_TIMEOUT

    def get(self, endpoint):
        return requests.get(
            f"{self.base_url}{endpoint}",
            timeout=self.timeout
        )

    def post(self, endpoint, payload):
        return requests.post(
            f"{self.base_url}{endpoint}",
            json=payload,
            timeout=self.timeout
        )

    def put(self, endpoint, payload):
        return requests.put(
            f"{self.base_url}{endpoint}",
            json=payload,
            timeout=self.timeout
        )

    def patch(self, endpoint, payload):
        return requests.patch(
            f"{self.base_url}{endpoint}",
            json=payload,
            timeout=self.timeout
        )

    def delete(self, endpoint):
        return requests.delete(
            f"{self.base_url}{endpoint}",
            timeout=self.timeout
        )