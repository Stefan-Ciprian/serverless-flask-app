from flaskapp import create_app
from flaskapp.config import Config


config = Config()
app = create_app(config)

if __name__ == '__main__':
    app.run()
