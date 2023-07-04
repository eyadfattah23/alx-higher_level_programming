#!/usr/bin/python3
class person:
    pass #empty block
p = person()
print(p)

class Person:
    def say_hi(self):
        print('hello')
p = Person()
p.say_hi()
# The previous 2 lines can also be written as
# Person().say_hi()


class PErson:
    def __init__(self, name):
        self.name = name
        
    def say_hi(self):
        print('hi ', self.name)


p = PErson('eyad')
p.say_hi()

class Robot:
    """Represents a robot, with a name."""

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        """Initializes the data."""
        self.name = name
        print("(Initializing {})".format(self.name))

        # When this person is created, the robot
        # adds to the population
        Robot.population += 1

    def die(self):
        """I am dying."""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))

    def say_hi(self):
        """Greeting by the robot.

        Yeah, they can do that."""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print("We have {:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()
droid3 = Robot('dd-3PO')
droid3.age = 100
print(droid3.age)
print(droid3.__dict__)
print(droid2.__dict__)
print(droid1.__dict__)
#print(Robot.age) --> wrong no attribute called age
Robot.brand = 'nokia'
print(Robot.__dict__)
print(droid1.__dict__)
print(droid1.brand)
droid2.brand = 'sony'
print(droid2.brand)
print(Robot.__dict__)
print(droid2.__dict__)
