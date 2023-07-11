#!/usr/bin/python3
"""defines a function that returns True if the object is
an instance of class, False otherwise
"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of a_class

    Args:
        obj (obj): obj to be checked

        a_class (class): the specified class
    """
    if type(obj) == a_class or isinstance(obj, a_class):
        return True
    else:
        return False
