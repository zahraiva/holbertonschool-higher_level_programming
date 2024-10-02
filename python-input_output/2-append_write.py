#!/usr/bin/python3
"""append write"""


def append_write(filename="", text=""):
    """append write"""
    with open(filename, 'a+r', encoding='utf-8') as a:
        return a.write(text)
