#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        while i < x:
            print(f"{my_list[i]}", end='')
            i += 1
        print()
    except IndexError:
        i = 0
        for j in my_list:
            print(f"{j}", end='')
            i += 1
        print()
    return i
