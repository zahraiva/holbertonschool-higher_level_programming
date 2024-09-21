#!/usr/bin/python3
"""Define a class"""


class Square:
    """Square classssss"""

    def __init__(self, size=0):
        if not isinstance:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
