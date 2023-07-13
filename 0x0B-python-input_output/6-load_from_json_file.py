#!/usr/bin/python3
"""define a function that creates an Object from a “JSON file”"""


def load_from_json_file(filename):
    """creates an Object from a “JSON file”
    """
    import json
    with open(filename, 'r') as f:
        return json.load(f)
