"""
List of application routes
"""
from os.path import join
from flask import Blueprint
from flask_cors import cross_origin
from flaskapp.csv_handler import get_file_path, get_file_names, get_data

items = Blueprint('items', __name__)


@items.route('/api/csv/health', methods=['GET'])
@cross_origin()
def health() -> dict:
    """
    Get health status

    Returns
    -------
    dict
        Dictionary with status True
    """
    return {
        'status': True
    }


@items.route('/api/csv/get_files', methods=['GET'])
@cross_origin()
def get_files() -> dict:
    """
    Get all files for CSV file path

    Returns
    -------
    dict
        Dictionary with all the files names specified in the file path
    """
    csv_file_path = get_file_path()

    return {
        'files': get_file_names(csv_file_path)
    }


@items.route('/api/csv/get_csv_data/<file_name>', methods=['GET'])
@cross_origin()
def get_csv_data(file_name: str) -> dict:
    """
    Get CSV data from specified file name

    Parameters
    ----------
    file_name: str
        Name of the CSV file

    Returns
    -------
    dict
        Dictionary containing series data, total earnings and currency
    """
    file_name = join(get_file_path(), file_name)

    return get_data(file_name)
