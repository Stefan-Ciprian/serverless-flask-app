# serverless-flask-app

Requirements:

    $ python3.10, pipenv

## Setup ##
    $ sudo apt install pipenv
    $ pipenv shell --python 3.10
    $ pipenv install --dev

## Check code linting ##
    $ pylint flaskapp tests app.py

## Running tests ##
    $ python -m pytest tests
    $ pytest --cov=flaskapp tests

## Documentation ##
    $ cd docs
    $ sphinx-apidoc -o ./source ..
    $ make clean
    $ make html
    Open index.html from build/html/index.html

## Running locally
    $ python app.py

## Example calls ##

##### GET Request
```
http://127.0.0.1:5000/get_files
```
##### Output
```
{
  "files": [
    "trade_sample_1.csv", 
    "trade_sample_2.csv", 
    "trade_sample_3.csv"
  ]
}
```

##### GET Request
```
http://127.0.0.1:5000/get_csv_data/trade_sample_1.csv
```
##### Output
```
{
  "currency": "USD", 
  "series": [
    [
      1326844800000, 
      180
    ], 
    [
      1326931200000, 
      234
    ], 
    ...
  ], 
  "total_earnings": -40331.44
}
```

### The application will read all files in flaskapp/static/csv directory ###

To add more files, copy them to flaskapp/static/csv and they will be automatically displayed.