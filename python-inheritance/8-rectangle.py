#!/usr/bin/python3
"""an empty class"""


class BaseGeometry():
    """class basegeometry"""
    def area(self):
        """to raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """to validate value"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))

class Rectangle(BaseGeometry):
    """class rectangle with a parent basegeometry"""
    def __init__(self, width, height) -> None:
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
