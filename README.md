# serverless-flask-app

Requirements:

    $ python3.9, python3.9-dev, python3.9-venv

## Setup
    $ sudo apt install python3.9-dev
    $ sudo apt install python3.9-venv
    $ python3.9 -m venv env
    $ source env/bin/activate
    $ pip install -r requirements.txt

## Running tests
    $ python -m pytest tests

## Running locally
    $ python app.py

### The application will read all files in flaskapp/static/csv directory ###

To add more files, copy them to flaskapp/static/csv and they will be automatically displayed.