#!/usr/bin/python3

"""a class Rectangle that defines a rectangle"""


class Rectangle:
    """a class Rectangle that defines a rectangle by
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """get width of the rectangle

        Returns:
            int: width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, width):
        """set width

        Args:
            value (int): width of the rectangle

        Raises:
            TypeError: width not integer
            ValueError: width less than 0
        """
        if type(width) != int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def height(self):
        """get the height of the rectangle

        Returns:
            int: height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, height):
        """set height

        Args:
            value (int): height of the rectangle

        Raises:
            TypeError: height not integer
            ValueError: height less than 0
        """
        if type(height) != int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height

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
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """get the string representation of the rectangle int #

        Returns:
            __str__: string representation of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ''
        rec = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rec += (str(self.print_symbol))
            if i != self.__height - 1:
                rec += '\n'
        return rec

    def __repr__(self):
        """return a string representation of the rectangle
        to be able to recreate a new instance by using eval()

        Returns:
            __repr__: string representation of the rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print the message Bye rectangle...
        when an instance of Rectangle is deleted
        """
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
