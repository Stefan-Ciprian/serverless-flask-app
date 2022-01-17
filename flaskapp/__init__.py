from flask import Flask
from flaskapp.routes import items
from flask_cors import CORS


def create_app(config):
    app = Flask(__name__)
    cors = CORS(app)

    app.register_blueprint(items)
    app.config['TESTING'] = config.TESTING
    app.config['CORS_HEADERS'] = 'Content-Type'

    return app
