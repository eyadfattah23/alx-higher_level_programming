#!/usr/bin/python3
def max_integer(my_list=[]):
    n = min(my_list)
    for i in my_list:
        if i > n:
            n = i
    return n
