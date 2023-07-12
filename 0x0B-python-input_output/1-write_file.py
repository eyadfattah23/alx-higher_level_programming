#!/usr/bin/python3
"""defines a function that reads a text file (UTF8) and prints it to stdout
"""


def write_file(filename="", text=""):
    """writes a text into a file (UTF8) and
    returns the number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
