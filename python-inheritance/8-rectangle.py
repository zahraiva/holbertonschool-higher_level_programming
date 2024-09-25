#!/usr/bin/python3
"""Module containing BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle with a parent basegeometry"""
    def __init__(self, width, height) -> None:
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
