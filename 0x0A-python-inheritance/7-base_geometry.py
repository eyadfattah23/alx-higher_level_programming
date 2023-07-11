#!/usr/bin/python3
"""defines class BaseGeometry.
"""


class BaseGeometry():
    """a BaseGeometry class
    """
    def area(self):
        """raises an Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value

        Args:
            name (string): name of the value variable
            value (int): value

        Raises:
            ValueError: if value is less or equal to 0
            TypeError: if value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
