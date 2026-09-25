import pytest


@pytest.fixture
def base_url():
    """Фікстура для базового URL API"""
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def headers():
    """Фікстура для заголовків запиту"""
    return {"User": "Student"}
