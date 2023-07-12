#!/usr/bin/python3
"""Defines a class MyInt that inherits from int
"""


class MyInt(int):
    """opposite of int
    """

    def __eq__(self, __value: int):
        """checks for inequality

        Args:
            __value (int): value to compare

        Returns:
            bool: True if __value isn't equal to self
        """
        if isinstance(__value, MyInt):
            return self != __value
        return False

    def __ne__(self, __value: object):
        """checks for equality

        Args:
            __value (int): value to compare

        Returns:
            bool: True if __value is equal to self
        """
        return super().__eq__(__value)
