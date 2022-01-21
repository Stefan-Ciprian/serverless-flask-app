"""Create integration tests"""
import json


def test_health_check(test_app_client):
    """
    Test health check

    Parameters
    ----------
    test_app_client
    """
    result = test_app_client.get('/api/csv/health')
    json_result = json.loads(result.data)

    assert json_result['status'] is True


def test_get_files_route(test_app_client):
    """
    Test get all files endpoint

    Parameters
    ----------
    test_app_client
    """
    result = test_app_client.get('/api/csv/get_files')
    json_result = json.loads(result.data)

    assert len(json_result['files']) == 3
    assert json_result['files'] == ['trade_sample_3.csv', 'trade_sample_2.csv',
                                    'trade_sample_1.csv']


def test_get_csv_data_file_one(test_app_client):
    """
    Test get CSV data from trade_sample_1.csv

    Parameters
    ----------
    test_app_client
    """
    result = test_app_client.get('/api/csv/get_csv_data/trade_sample_1.csv')
    json_result = json.loads(result.data)

    assert len(json_result['series']) == 62
    assert json_result['total_earnings'] == -40331.44
    assert json_result['currency'] == 'USD'


def test_get_csv_data_file_two(test_app_client):
    """
    Test get CSV data from trade_sample_2.csv

    Parameters
    ----------
    test_app_client
    """
    result = test_app_client.get('/api/csv/get_csv_data/trade_sample_2.csv')
    json_result = json.loads(result.data)

    assert len(json_result['series']) == 62
    assert json_result['total_earnings'] == -45908.44
    assert json_result['currency'] == 'USD'


def test_get_csv_data_file_three(test_app_client):
    """
    Test get CSV data from trade_sample_3.csv

    Parameters
    ----------
    test_app_client
    """
    result = test_app_client.get('/api/csv/get_csv_data/trade_sample_3.csv')
    json_result = json.loads(result.data)

    assert len(json_result['series']) == 26
    assert json_result['total_earnings'] == 23289.86
    assert json_result['currency'] == 'USD'
