#!/usr/bin/python3
"""define a function that inserts a line of text to a file,
after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r+') as f:
        lines = []
        for line in f:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)
        f.seek(0)
        f.truncate(0)
        for l in lines:
            f.write(l)
