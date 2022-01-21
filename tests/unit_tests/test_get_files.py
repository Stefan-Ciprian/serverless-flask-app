"""Unittest module"""
from flaskapp.csv_handler import get_file_path, get_file_names


def test_get_files():
    """Test getting all files"""
    file_path = get_file_path()
    files = get_file_names(file_path)

    assert files == ['trade_sample_3.csv', 'trade_sample_2.csv',
                     'trade_sample_1.csv']
