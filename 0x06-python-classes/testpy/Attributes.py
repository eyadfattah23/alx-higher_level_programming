#!python3
'''
_name 	Protected 	Protected attributes should not be used outside the class definition, unless inside a subclass definition.

__name 	Private 	This kind of attribute is inaccessible and invisible. It's neither possible to read nor write to those attributes,
                    except inside the class definition itself.
'''
class A():
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"

x = A()
print(x.pub + " and my value can be changed")
print(x._prot + " and my value can be changed in only a subclass")
print(type(x))
u = A()
u.pub = "hahahs"
print(u.pub + " and my value can be changed")
"""python
    print(u.__priv) --> AttributeError: 'A' object has no attribute '__priv'    
""" #this is perfect information hiding.


####Data Encapsulation means, 
# that we should only be able to access private attributes via getters and setters.
class robot:
    def __init__(self, name = None, build_year = None):
        self.__name = name
        self.__build_year = build_year
    def say_hi(self):
        if self.__name:
            print('hi I am {}'.format(self.__name))
        else:
            print('hi I\'ve no name')
        if self.__build_year:
            print('built year is {}'.format(self.__build_year))
        else:
            print('unknown built year')
    
    def set_name(self, new_name):
        self.__name = new_name
    def get_name(self):
        return self.__name
    
    def set_by(self, by):
        self.__build_year = by
    def get_by(self):
        return self.__build_year
            
x = robot('d1', 1999)
y = robot('d2', 1899)
for r in [x, y]:
    r.say_hi()
# print(x.__name) -->AttributeError: 'robot' object has no attribute '__name' 
print(x.get_name(), x.get_by())

x.set_name('edo')
x.set_by(1234)
x.say_hi()
