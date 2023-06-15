#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not isinstance(roman_string, str)) or len(roman_string) == 0:
        return 0
    dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
        "M": 1000,
    }
    res = 0
    i = 1
    while i < len(roman_string):
        if roman_string[i - 1] + roman_string[i] in dict:
            res += dict[roman_string[i - 1] + roman_string[i]]
            i += 2
        else:
            res += dict[roman_string[i - 1]]
            i += 1
    if len(roman_string) == 1:
        res += dict[roman_string[0]]
    if roman_string[-2:] not in dict:
        res += dict[roman_string[-1]]
    return res
