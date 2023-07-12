#!/usr/bin/python3
"""CREATE a function that returns the JSON representation of an object (string)
"""


def to_json_string(my_obj):
    """returns the JSON representation of an object

    Args:
        my_obj (string): _description_
    """
    import json
    return (json.dumps(my_obj))
