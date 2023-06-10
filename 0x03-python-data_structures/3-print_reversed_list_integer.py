#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    n = my_list
    n.reverse()
    for i in n:
        print("{:d}".format(i))
