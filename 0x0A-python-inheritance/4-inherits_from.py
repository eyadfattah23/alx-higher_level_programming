#!/usr/bin/python3
"""Write a function that returns True if the object
is an instance of a class that
inherited (directly or indirectly)from the specified class;
"""


def inherits_from(obj, a_class):
    """returns True if the object is a subclass of a_class


    Args:
        obj : _description_
        a_class (_type_): _description_
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
