#!/usr/bin/python3
"""student to JSON"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """initialization of our class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dict of our string"""
        return self.__dict__
