#!/usr/bin/python3

"""
A square class
"""


class Square:
    """
    initializing the class at start
    """

    def __init__(self, _size: int = 0):
        if type(_size) != int:
            raise TypeError("size must be an integer")
        if _size < 0:
            raise ValueError("size must be >= 0")
        self._size = _size
