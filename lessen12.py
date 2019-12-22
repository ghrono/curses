#!/usr/bin/env python3.8

from abc import ABC, abstractmethod, abstractproperty

def example1():
	class A:
		"""docstring for A"""
		def __init__(self):
			self._b = 3
		
		@property
		def b(self):
			return self._b
		
		@b.setter
		def b(self, value):
			assert isinstance(value, int), "type must be integer"
			self._b = value

	a = A()

	print (a.b)	
	a.b = 5
	print(a.b)

def example2():

	class Checker:
		"""docstring for Checker"""
		def __set_name__(self, owner, name):
			self.name = name

		def __set__(self, instance, value):
			assert isinstance(value, int), "type must be integer"
			instance.__dict__[self.name] = value 


		def __get__(self, instance, owner):
			return instance.__dict__[self.name]

	class A:
		b = Checker()
		c = Checker()

		def __init__(self):
				self.b = 3
				self.c = 6
	a = A()

	print (a.c)

def example3():

	class Student:
		def __init__(self, name, mark):
			self._name = name
			self.mark = mark

		@property
		def name(self):
				return self._name
			
		@name.setter
		def name(self, value):
			if value.isalpha():
				self._name = value
			else:
				raise ValueError ('name must be only latter')
			
		def __repr__(self):
			return self._name

		def __gt__(self, other):
			return self.mark > other.mark

	s1 = Student('Egor', 5)
	s2 = Student('Vlad', 6)
	s3 = Student('32ffZZ',50)

	print (s1.name)
	print (s1 > s2)

def example4():
	pass

def example5():

	class AbsMessage(ABC):
		
		@abstractmethod
		def render(self):
			pass
		
		@abstractmethod
		def print(self):
			pass

		@abstractproperty
		def valid(self):
			pass
	
		@abstractmethod
		def raise_error(self):
			pass

	class msg_a(AbsMessage):
		
		def render(self):
			pass			

		def print(self):
			return 'printed'
		
		@property
		def valid(self):
			pass
			
		def raise_error(self):
			return 'ERROR'

	def send_msg(msg):
		if msg.valid:
			msg.render()
			msg.print()
		else:
			msg.raise_error()


	send_msg()


def main():
#	example1()
#	example2()
#	example5()




if __name__ == '__main__':
	main()