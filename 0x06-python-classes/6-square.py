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
                    position not a tuple of 2 positive integers
            ValueError: size is less than 0
    """
    def __init__(self, size=0, position=(0, 0)):
        """initializes a square

        Args:
            size (int, optional): size of the square. Defaults to 0.
            position (tuple, optional): position of the square.
                                    Defaults to (0, 0).
        """
        self.size = size
        self.position = position

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

    def my_print(self):
        """prints in stdout the square with the character #
        """
        if self.size == 0:
            print()
            return
        for p in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(' ', end='')
            for j in range(self.__size):
                print('#', end='')
            print()

    @property
    def position(self):
        """retrieve position of the square

        Returns:
            tuple: position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) \
            or not isinstance(value[0], int) \
                or not isinstance(value[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value
