#!/usr/bin/env python3.8
import datetime as dt
from tkinter import * 

def fffff():

	root = Tk()

	label = Label(root, text="eny text", width = 30)
	entry = Entry (root, width= 15, font =15 )
	text = Text(root, width= 10, height=10)


	def hello(event):
		text.insert(0.0, "hello world")

	def com_but():
		label['text'] += " hello"

	def world(event):
		txt = text.get(0.0, "end")
		text.insert(0.0, txt[::-1])


	button = Button(root, text= "OK", width = 30, font= 15, height= 2)


	button.bind("<Button-3>", world)
	button.bind("<Button-1>", hello)	

	

	
	entry.grid(column=0, row =1)
	button.grid(column=1, row=0, rowspan=2)
	label.grid(column = 0, row =0)
	text.grid(column=0, row=2, columnspan=2)

	root.mainloop()

def example_calss():
	class cat:
		name = "Tom"
		age = 5

	cat = cat()

	print (cat.name, cat.age)

def example_calss2():

	class Cat:
		""" doc string """
		def __init__(self, name, age):
			self.name = name
			self.age = age
		def feed(self, food):
			if food == "wiskass":
				return __eat_system(food)
			else:
				return "shhhhhhhhhhhh"
		def voice(self):
			return "MEOW"
		def __eat_system(self, food):
			return "om om om !!"	
#		def _eat_thise(self):
#			return "om om om !!"

		def __add__(self, other):
			return [Cat(None, 0) for i in range(6)]

	cat = Cat("Tom", 5)
	cat1 = Cat("Gav", 4)
	print (cat.age)
	print (cat1.age)
	cat.feet = "43"
	print ( cat.feet)
	cat.feed("mouse")
	print (cat.feed('fruts'))
	print (cat.voice())
	print("fuflo ", cat._Cat__eat_system("fuflo"))
#	print( cat._eat_thise('fff'))

	bla = (cat + cat)[0].age
	print (bla)


def example3():

	class Cat:
		"""docstring"""
		def __init__(self, name):
			self.name = name
			self.__born_date = dt.datetime.now()   #.strftime('%T:%Y')			

		
		@property
		def born_date(self):
			return self.__born_date.strftime('%T:%Y')
		
		@property
		def seconds(self):
			return dt.datetime.now() - self.__born_date


	cat = Cat("Tom")

	print (cat.born_date)
	print (cat.seconds)


def gui_oop():

#	class 
		pass	

def example4():

	class Array:
		def __init__(self, *args):
			self.args = args

		def __add__(self, other):
			vect = [sum (item) for item in zip(self.args, other.args)]
			return Array (*vect)
			
		def __repr__(self):
			return str(self.args)

	ar1 = Array(1, 2, 3, 4, 5)
	ar2 = Array(6, 7, 8, 9, 0)

	print (ar1 + ar2)

def main():
#	fffff()
#	example_calss()
#	example_calss2()
#	example3()
	example4()

if __name__ == '__main__':
	main()