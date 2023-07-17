#!/usr/bin/python3
"""define class rectangle that inherits from base"""


Base = __import__('base').Base


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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
