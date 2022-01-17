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