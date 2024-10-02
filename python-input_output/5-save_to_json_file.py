#!/usr/bin/python3
"""save to json file"""
import json


def save_to_json_file(my_obj, filename):
    with open(my_obj, 'w', encoding='utf-8') as a:
        a.write(json.dumps(my_obj))
