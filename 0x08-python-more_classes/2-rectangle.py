#!/usr/bin/python3
"""a class Rectangle that defines a rectangle"""


class Rectangle:
    """a class Rectangle that defines a rectangle by
    """
    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get width of the rectangle

        Returns:
            int: width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """set width

        Args:
            value (int): width of the rectangle

        Raises:
            TypeError: width not integer
            ValueError: width less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle

        Returns:
            int: height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """set height

        Args:
            value (int): height of the rectangle

        Raises:
            TypeError: height not integer
            ValueError: height less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """get the area of the rectangle

        Returns:
            int: area of the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """get perimeter of the rectangle

        Returns:
            int: perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
