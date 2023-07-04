#!/usr/bin/python3
'''defines a square by:

    Private instance attribute: size
    Instantiation with size (no type/value verification)
'''


class Square:
    """class Square that represents a square"""
    def __init__(self, size=0):
        """initializes a square

        Args:
            size (int): size of the square
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if self.__size < 0:
            raise ValueError('size must be >= 0')
