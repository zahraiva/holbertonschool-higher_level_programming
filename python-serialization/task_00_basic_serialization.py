#!/usr/bin/python3
"""serialization"""
import json


def serialize_and_save_to_file(data, filename):
    """serializing and saving a file"""
    with open(filename, 'w', encoding='UTF-8') as a:
        json.dump(data, a)

def load_and_deserialize(filename):
    """loading and deserializing"""
    with open(filename, 'r', encoding='UTF-8') as a:
        content=json.load(a)
    return content
