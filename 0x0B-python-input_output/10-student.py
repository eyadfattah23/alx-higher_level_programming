#!/usr/bin/python3
"""define a class Student that defines a student"""


class Student:
    """defines a student
    """
    def __init__(self, first_name, last_name, age):
        """initialize a Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance
        """
        jdict = {}
        idict = self.__dict__
        if attrs:
            for attr in attrs:
                if attr in idict:
                    jdict[attr] = idict[attr]
            return jdict
        else:
            return self.__dict__
