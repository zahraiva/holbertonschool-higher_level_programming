#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(file_csv):
    """converting csv to json"""
    try:
        with open(file_csv, 'r') as a:
            csvr = csv.DictReader(a)
            content = list(csvr)

        with open('data.json', 'w') as a:
            json.dump(content, a)

        return True
    except (FileNotFoundError, IOError) as e:
        print(f'error: {e}')
        return False
