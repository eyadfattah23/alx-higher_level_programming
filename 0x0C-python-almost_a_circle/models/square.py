#!/usr/bin/python3
"""define class square that inherits from rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class square that inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str representation of the rectangle
        """
        return f"[Square] ({self.id}) {self.x}/{self.y}" \
            f" - {self.width}"

    @property
    def size(self):
        """get size of the square"""
        return self.width

    @size.setter
    def size(self, size):
        """set size of the square"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update the class Rectangle"""

        if args and len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        elif kwargs:
            for k in kwargs:
                if k == 'id':
                    self.id = kwargs[k]
                elif k == 'size':
                    self.size = kwargs[k]
                elif k == 'x':
                    self.x = kwargs[k]
                elif k == 'y':
                    self.y = kwargs[k]
