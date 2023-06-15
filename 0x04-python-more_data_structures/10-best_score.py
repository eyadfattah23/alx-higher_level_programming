#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict):
        if len(a_dictionary) == 0:
            return None
        return max(a_dictionary, key=a_dictionary.get)
