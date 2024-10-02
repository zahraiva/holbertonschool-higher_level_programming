#!/usr/bin/python3
"""Load, add, and save"""

from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = 'add_item.json'

try:
    nl = load_from_json_file(filename)
except FileNotFoundError:
    nl = []

nl.extend(argv[1:])
save_to_json_file(nl, filename)
