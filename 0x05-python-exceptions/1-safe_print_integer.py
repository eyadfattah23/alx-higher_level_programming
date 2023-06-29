#!/usr/bin/python3
def safe_print_integer(value):
    i = True
    try:
        print('{:d}'.format(value))
    except (ValueError, TypeError):
        i = False
    return i
