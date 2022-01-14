from os import listdir
from os.path import isfile, join, dirname, abspath
import csv
import time
import datetime


def get_file_path():
    current_path = dirname(abspath(__file__))
    csv_file_path = join(current_path, 'static/csv')

    return csv_file_path


def get_file_names(path_name):
    file_names = [file_name for file_name in listdir(path_name) if isfile(join(path_name, file_name))]
    
    return file_names


def get_data(file_name):
    results = []
    total_units = 0
    total_earnings = 0
    currency = None

    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for index, row in enumerate(csv_reader):
            if index == 0:
                continue

            if currency is None:
                currency = row[3]

            date_value = row[0]
            ts_value = time.mktime(datetime.datetime.strptime(date_value, "%d/%m/%Y").timetuple())
            ts = int(ts_value) * 1000

            total_units += int(row[1])
            total_earnings += int(row[1]) * float(row[2])

            results.append([ts, total_units])

    return {
        'series': results,
        'total_earnings': round(total_earnings, 2),
        'currency': currency
    }
