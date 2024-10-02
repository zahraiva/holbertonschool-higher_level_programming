#!/usr/bin/python3
"""writing a file"""


def write_file(filename="", text=""):
    """writing a file"""
    with open(filename, 'w', encoding='utf-8') as a:
        return a.write(text)
