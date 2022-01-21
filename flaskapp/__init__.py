"""
Create Flask application
"""
from flask import Flask
from flask_cors import CORS
from flaskapp.routes import items
from flaskapp.config import Config


def create_app(config_obj: Config) -> Flask:
    """
    Create Flask application

    Parameters
    ----------
    config_obj : Config
        Configuration object

    Returns
    -------
    app : Flask
        instance of Flask
    """
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(items)
    app.config['TESTING'] = config_obj.get_testing()
    app.config['CORS_HEADERS'] = config_obj.get_cors_headers()

    return app
