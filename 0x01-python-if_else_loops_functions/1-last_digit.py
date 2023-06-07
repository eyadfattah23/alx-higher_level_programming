#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number
if number < 0:
    num = -number
print("Last digit of {} is {} ".format(number, num % 10), end="")
if num % 10 > 5:
    print("and is greater than 5")
elif num % 10 == 0:
    print("and is 0")
elif num % 10 < 6 and num % 10 != 0:
    print("and is less than 6 and not 0")
    