#!/usr/bin/python3
"""defines a function that returns True if the object is
exactly an instance of the specified class ;
otherwise False
"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance

    Args:
        obj (obj): obj to be checked
        a_class (class): the specified class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
