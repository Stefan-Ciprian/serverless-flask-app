from flaskapp.csv_handler import get_file_path, get_file_names
import json


def test_get_files():
    file_path = get_file_path()
    files = get_file_names(file_path)

    assert files == ['trade_sample_1.csv', 'trade_sample_2.csv', 'trade_sample_3.csv']


def test_get_files_route(client):
    result = client.get('/get_files')
    json_result = json.loads(result.data)

    assert len(json_result['files']) == 3
    assert json_result['files'] == ['trade_sample_1.csv', 'trade_sample_2.csv', 'trade_sample_3.csv']


def test_get_csv_data_file_one(client):
    result = client.get('/get_csv_data/trade_sample_1.csv')
    json_result = json.loads(result.data)

    assert len(json_result['series']) == 62
    assert json_result['total_earnings'] == -40331.44
    assert json_result['currency'] == 'USD'


def test_get_csv_data_file_two(client):
    result = client.get('/get_csv_data/trade_sample_2.csv')
    json_result = json.loads(result.data)

    assert len(json_result['series']) == 62
    assert json_result['total_earnings'] == -45908.44
    assert json_result['currency'] == 'USD'


def test_get_csv_data_file_three(client):
    result = client.get('/get_csv_data/trade_sample_3.csv')
    json_result = json.loads(result.data)

    assert len(json_result['series']) == 26
    assert json_result['total_earnings'] == 23289.86
    assert json_result['currency'] == 'USD'


