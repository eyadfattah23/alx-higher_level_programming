#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    score_weight_prod = 0
    weight_sum = 0
    for tup in my_list:
        score_weight_prod += tup[0]*tup[1]
        weight_sum += tup[1]
    return score_weight_prod / weight_sum
        
