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

    def __str__(self):
        """get the string representation of the rectangle int #

        Returns:
            __str__: string representation of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ('')
        else:
            name = self.__class__.__name__
            return f"[Rectangle] {self.__width}/{self.__height}"
