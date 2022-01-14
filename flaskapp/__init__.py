from flask import Flask
from flaskapp.routes import items


def create_app(config):
    app = Flask(__name__)

    app.register_blueprint(items)
    app.config['TESTING'] = config.TESTING

    return app
