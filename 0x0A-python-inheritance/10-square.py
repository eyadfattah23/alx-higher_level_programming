#!/usr/bin/python3
"""defines class Square
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle (9-rectangle.py)
    """
    def __init__(self, size):
        """initialization function for size

        Args:
            size (int): size of the square
        """
        self.__size = size
        self.integer_validator('size', self.__size)
        super().__init__(size, self.__size)

    def area(self):
        """calculate area of square

        Returns:
            int: area of square
        """
        return self.__size ** 2
