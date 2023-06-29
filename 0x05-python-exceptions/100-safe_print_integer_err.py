#!/usr/bin/python3
def safe_print_integer_err(value):
    i = True
    import sys

    try:
        print('{:d}'.format(value))
    except ValueError as ve:
        print('Exception:{}'.format(ve), file=sys.stderr)
        i = False
    except TypeError as te:
        print('Exception:{}'.format(te), file=sys.stderr)
        i = False
    return i
