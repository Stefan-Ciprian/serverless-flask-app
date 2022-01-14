import pytest
from flaskapp import create_app
from flaskapp.config import TestingConfig


@pytest.fixture
def client():
    app = create_app(TestingConfig)

    with app.test_client() as client:
        yield client
