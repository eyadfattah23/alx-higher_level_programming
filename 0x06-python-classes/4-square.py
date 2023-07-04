#!/usr/bin/python3
'''defines a square by:

    Private instance attribute: size
    Instantiation with size (no type/value verification)
    Public instance method: def area(self):  returns the current square area
'''


class Square:
    """define a square

    Raises:
            TypeError: size not an integer,
            ValueError: size is less than 0
    """
    def __init__(self, size=0):
        """initializes a square

        Args:
            size (int): size of the square

        Raises:
            TypeError: size not an integer,
            ValueError: size is less than 0
        """
        self.size = size
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if self.size < 0:
            raise ValueError('size must be >= 0')

    @property
    def size(self):
        """retrieve size

        Returns:
            int: size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """set size to value

        Args:
            value (int): new size of the square
        """
        self.__size = value
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if self.__size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """calculates area of the square

        Returns:
            int: area of the square
        """
        return self.__size ** 2
