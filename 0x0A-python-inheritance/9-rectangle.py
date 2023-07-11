#!/usr/bin/python3
"""defines class Rectangle
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry
    (7-base_geometry.py)
    """
    def __init__(self, width, height):
        """init function for w and h

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.__width = width
        self.__height = height
        self.integer_validator('width', self.__width)
        self.integer_validator('height', self.__height)

    def area(self):
        """calculate area of rectangle

        Returns:
            int: area of rectangle
        """
        return self.__height * self.__width
