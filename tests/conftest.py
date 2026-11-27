import pytest

from clients.api_client import APIClient


# Provide an API client instance for each test.
@pytest.fixture
def client():
    return APIClient()
