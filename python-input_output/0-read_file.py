#!/usr/bin/python3
"""reading a file"""

def read_file(filename=""):
    """reading a file"""
    with open(filename, 'r', encoding='utf-8') as e:
        print(e.read(), end='')
