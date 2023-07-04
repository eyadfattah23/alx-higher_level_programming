#!python3

# https://python-course.eu/oop/properties-vs-getters-and-setters.php


'''
you wanna assign a number between 0 and 1000 to an object
like if we write p1 = P(4002)
p1.x will equal 1000
'''
class P:
	def __init__(self, x):
		self.set_x(x)
	def get_x(self):
		return self.__x
	def set_x(self, x):
		if x < 0:
			self.__x = 0
		elif x > 1000:
			self.__x = 1000
		else:
			self.__x = x
	x = property(get_x, set_x)
'''
We have now two ways to access or change the value of x
Either by using "p1.x = 42" or by "p1.set_x(42)"
'''





'''
We can fix this by turning the getter and the setter methods into private methods,
which can't be accessed anymore by the users of our class P:
'''
class P:
	def __init__(self, x):
		self.__set_x(x)
	def __get_x(self):
		return self.__x
	def __set_x(self, x):
		if x < 0:
			self.__x = 0
		elif x > 1000:
			self.__x = 1000
		else:
			self.__x = x
	x = property(__get_x, __set_x)
p1 = P(6000)
print(p1.x)
## p1.get_x() -> error
## p1.__get_x() -> error
p1.x = 60
print(p1.x)
'''
so the version with the decorator "@property" is the Pythonic way to do it!
'''




class P:
	def __init__(self, x):
		self.x = x
	@property
	def x(self):
		return self.__x
	@x.setter
	def x(self, x):
		if x < 0:
			self.__x = 0
		elif x > 1000:
			self.__x = 1000
		else:
			self.__x = x



class OurClass:
	def __init__(self, a):
		self.OurAtt = a
	@property
	def OurAtt(self):
		return self.__OurAtt
	@OurAtt.setter
	def OurAtt(self, new_a):
		if new_a < 0:
			self.__OurAtt = 0
		elif new_a > 1000:
			self.__OurAtt = 1000
		else:
			self.__OurAtt = new_a

xx = OurClass(300)
print(xx.OurAtt)
xx.OurAtt = 500
print(xx.OurAtt)
