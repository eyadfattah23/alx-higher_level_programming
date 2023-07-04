#!/usr/bin/python3
'''defines a square by:

    Private instance attribute: size
    Instantiation with size (no type/value verification)
'''


class Square:
    """class Square that represents a square"""
    def __init__(self, size):
        """initializes a square

        Args:
            size (int): size of the square
        """

        self.__size = size
