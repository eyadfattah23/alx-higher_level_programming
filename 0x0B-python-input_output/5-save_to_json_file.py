#!/usr/bin/python3
"""define a function that writes an Object to a text file,
using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file

    Args:
        my_obj: _description_
        filename: _description_
    """
    import json
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
