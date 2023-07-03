#!/usr/bin/python3
def hi(obj):
    print("Hi, I am " + obj.name + "!")
class Robot:
    pass
x = Robot()
x.name = "Marvin"
hi(x)

''''''

class RObot:
    say_hi = hi
x = RObot()
x.name = "Marvin"
RObot.say_hi(x)
x.say_hi()
'''
"Robot.say_hi(x)". and "x.say_hi()" are equivalent
'''
