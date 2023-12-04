#!/usr/bin/python3
'''function to find the peak element in a list of ints'''


def find_peak(list_of_integers):
    '''finds a peak in a list of unsorted integers.'''
    if not list_of_integers:
        return None
    mid_index = int(len(list_of_integers) / 2)

    peak = list_of_integers[mid_index]
    left = list_of_integers[mid_index - 1]
    right = list_of_integers[mid_index + 1]
    l_index = mid_index-1
    r_index = mid_index+1

    if left >= peak:
        while l_index > - 1 and left >= list_of_integers[l_index + 1]:
            peak = left
            l_index -= 1
            left = list_of_integers[l_index]
    if right >= peak:
        while r_index < len(list_of_integers) - 1 \
                and right >= list_of_integers[r_index - 1]:
            peak = right
            r_index += 1
            right = list_of_integers[r_index]

    return max(peak, max(left, right))
