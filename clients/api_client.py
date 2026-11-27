import logging

import requests

from config import BASE_URL, REQUEST_TIMEOUT

logger = logging.getLogger(__name__)


class APIClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.timeout = REQUEST_TIMEOUT

    # Send an HTTP request and log the response or connection error.
    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"

        logger.info("Sending %s request to %s", method, url)

        try:
            response = requests.request(method, url, timeout=self.timeout, **kwargs)
        except requests.exceptions.RequestException:
            logger.exception("HTTP request failed: %s %s", method, url)
            raise

        logger.info("Response status: %s", response.status_code)

        return response

    def get(self, endpoint):
        return self._request("GET", endpoint)

    def post(self, endpoint, payload):
        return self._request("POST", endpoint, json=payload)

    def put(self, endpoint, payload):
        return self._request("PUT", endpoint, json=payload)

    def patch(self, endpoint, payload):
        return self._request("PATCH", endpoint, json=payload)

    def delete(self, endpoint):
        return self._request("DELETE", endpoint)
