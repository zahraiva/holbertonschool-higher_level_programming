#!/usr/bin/python3
"""load from json file"""
import json


def load_from_json_file(filename):
    """load from json file"""
    with open(filename, 'r', encoding='utf-8') as a:
        b = json.loads(a.read())
        return b
    