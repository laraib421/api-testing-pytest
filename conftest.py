import os
import pytest
from utils.api_client import APIClient

BASE_URL = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")


@pytest.fixture(scope="session")
def api():
    return APIClient(BASE_URL)
