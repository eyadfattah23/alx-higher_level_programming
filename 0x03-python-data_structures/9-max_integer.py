#!/usr/bin/python3
def max_integer(my_list=[]):
    if isinstance(my_list, list):
        if len(my_list) == 0:
            return None
        n = my_list[0]
        for i in my_list:
            if i > n:
                n = i
        return n
