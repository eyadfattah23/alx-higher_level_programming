#!/usr/bin/python3
"""defines a function that adds a new attribute to an object possible
"""


def add_attribute(object, name, value):
    """adds a new attribute to an object if it’s possible

    Args:
        object (object): _description_
        name : attribute name
        value : attribute value

    Raises:
        TypeError: if u it doesn't have __dict__ attribute
    """
    if hasattr(object, '__dict__'):
        object.name = value
    else:
        raise TypeError('can\'t add new attribute')
