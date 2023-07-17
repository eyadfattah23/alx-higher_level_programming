#!/usr/bin/python3
"""define class rectangle that inherits from base"""


from models.base import Base


class Rectangle(Base):
    """Rectangle inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize a Rectangle

        Args:
            width (_type_): _description_
            height (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get the width of this Rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        """set the width of this Rectangle"""
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        """get the height of this Rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """set the height of this Rectangle"""
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x"""
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y"""
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """calculates area"""

        return self.__width * self.__height

    def display(self):
        """display the rectangle in #
        """
        if self.__width == 0 or self.__height == 0:
            print()
            return
        for p in range(self.__y):
            print()
        for i in range(self.__height):
            for k in range(self.__x):
                print(' ', end='')
            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """str representation of the rectangle
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y}" \
            f" - {self.__width}/{self.__height}"
