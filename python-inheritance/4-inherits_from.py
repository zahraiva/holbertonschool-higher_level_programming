#!/usr/bin/python3
"""inheriting from a specified class"""


def inherits_from(obj, a_class):
    """checking object of a class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
