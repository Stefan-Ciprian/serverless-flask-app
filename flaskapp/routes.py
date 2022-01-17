from flask import Blueprint
from os.path import join
from flaskapp.csv_handler import get_file_path, get_file_names, get_data
from flask_cors import cross_origin

items = Blueprint('items', __name__)


@items.route('/get_files', methods=['GET'])
@cross_origin()
def get_files():
    csv_file_path = get_file_path()

    return {
        'files': get_file_names(csv_file_path)
    }


@items.route('/get_csv_data/<file_name>', methods=['GET'])
@cross_origin()
def get_csv_data(file_name):
    file_name = join(get_file_path(), file_name)

    return get_data(file_name)
