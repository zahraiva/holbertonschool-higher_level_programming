#!/usr/bin/python3
"""student to JSON"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """initialization of our class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

     def to_json(self, attrs=None):
        if isinstance(attrs, list) and \
                all(isinstance(element, str) for element in attrs):
            new_dict = dict()
            for i in attrs:
                if i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
            return new_dict
        return self.__dict__
