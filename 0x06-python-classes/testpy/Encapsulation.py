#!/usr/bin/python3
class Robot:
    def __init__(self, name = None, build_year = None):  #by is new
        self.name = name
        self.build_year = build_year
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def say_hi(self):
        if self.name:
            print(f'hi I am robot {self.name}')
        else:
            print('I\'ve no name')
    def get_by(self):
        return self.build_year
    def set_by(self, by):
        self.build_year = by

x = Robot('edo')
x.say_hi()
print(x.get_name())
x.set_name('euro')
x.say_hi()
y = Robot(x.get_name())
print('y = {}'.format(y.get_name()))
y.set_name(x.get_name() + 'pe')
print('y = {}'.format(y.get_name()))
z = Robot(build_year=1999)
z.say_hi()
print(z.get_by())
