#!/usr/bin/python3
"""Module containing Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square with a parent Rectangle"""
    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """calculating area"""
        return self.__size ** 2

    def __str__(self):
        """printing our square"""
        return f"[Square] {self.__size}/{self.__size}"
