#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i, n = 0, 0
    while i < x and my_list[i]:
        try:
            print("{:d}".format(my_list[i]), end='')
            n += 1
        except (ValueError, TypeError):
            pass
        i += 1
    print()
    return n
