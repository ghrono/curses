#!/usr/bin/env python3.8
from random import shuffle, randint


def example1():
	
	class Student:
		def __init__(self, name, mark):
			self._name = name
			self.mark = mark
			self.right = None
			self.left = None

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

def example2():

	class Bag:
		"""docstring for Bag"""
		def __init__(self, *args):
			assert sum(args) <= 4, "to mach elemets in bag"
			for name_fild, value in zip(['a', 'b', 'c', 'd'], args):
				setattr(self, name_fild, value)



	orders = [randint(1,4) for i in range(10 ** 2)]
	shuffle(orders)
	print(orders)
	print (orders.count(4))
	print (orders.count(3))
	print (orders.count(2))
	print (orders.count(1))
			

	def sorriririr(orders):
		sumka = []
		while orders:
			sumka.append(orders.pop(0))
			print(sumka)
			sumka = []
			
	sorriririr(orders)


	b = Bag(2,1,1)

	print (b.c)





def main():
#	example1()
	example2()


if __name__ == '__main__':
	main()