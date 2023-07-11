#!/usr/bin/python3
    """returns the list of available attributes and methods of an object
    """
def lookup(obj):
    """returns the list of available attributes and methods of an object

    Args:
        obj (any): object to lookup

    Returns:
        list: available attributes and methods of an object
    """
    return dir(obj)
