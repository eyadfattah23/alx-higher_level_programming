#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if isinstance(my_list, list):
        n = my_list.copy()
        if idx >= len(my_list) or idx < 0:
            return n
        n[idx] = element
        return n
