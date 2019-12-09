#!/usr/bin/env python3.8

from time import time
from socket import socket
from time import sleep

def heshi():
	print( hash('hello'))
	print ()

def my_sum(x, y):
	if x == y:
		raise ValueError ('not support this value: raise except')
	return x + y
def my_sum2(x, y):
	assert x != y, 'not support this value: assert except'
	return x + y
def axceptionsi():
	x,y = 3,5

	for x in range(1,10):
		try:
			print( my_sum(x, y))
			print( my_sum2(x-1, y))

		except ValueError as ve:
			print( *ve.args)

		except AssertionError as ae:
			print( *ae.args)

		except TypeError as te:
			print( *te.args)
	print ('важный кот')

def say_hello(name, pouse):
	start_time = time()
	while True:
		if time() - pouse > start_time :
			print (f"hello {name}")
			start_time = time()
		yield
def async_example(all_time):
	gen1 = say_hello("foo", 3)
	gen2 = say_hello("bar", 5)
	start_time = time()
	
	while start_time + all_time > time():
		next(gen1)
		next(gen2)
	
def connected():
	client = socket()
#	178.121.77.112
	client.connect(('http://8a2ccc25.ngrok.io', 80))
	while True:
	   	print(client.recv(2).decode('1251'), end ='')

def main():
#	heshi()
#	axceptionsi()
#	async_example(35)
	connected()
	

if __name__ == '__main__':
	main()