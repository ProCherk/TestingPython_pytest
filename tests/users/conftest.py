import pytest
import requests
from configuration import SERVICE_URL


@pytest.fixture  # smth that will execute before the test
def get_users():
    response = requests.get(SERVICE_URL)
    return response
