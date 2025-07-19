#!/usr/bin/python3

"""
A square class
"""


class Square:
    """
    initializing the class at start
    """

    def __init__(self, __size: int = 0):
        if type(__size) != int:
            raise TypeError("size must be an integer")
        if __size < 0:
            raise ValueError("size must be >= 0")
        self.__size = __size

    """
    return area of the square
    """

    def area(self) -> int:
        return self.__size * self.__size
