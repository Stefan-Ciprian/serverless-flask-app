"""Configure pytest"""
import pytest
from flaskapp import create_app
from flaskapp.config import Config


@pytest.fixture
def test_app_client():
    """
    Generate a test client instance

    Yields
    -------
    test_client
        Test client app instance
    """
    config = Config(True)
    app = create_app(config)

    with app.test_client() as test_client:
        yield test_client
