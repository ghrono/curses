#!/usr/bin/env python3.8
import unittest
import logging
from doctest import testmod

def example1():
	logging.basicConfig(
		format = "%(asctime)s: %(levelname)s: %(message)s", 
		level = logging.WARNING, 
		datefmt = "%Y-%m-%d %A %H:%M:%S",
		filename = '/tmp/test_log.log')

	for x in range(10):
		logging.info('info')
		logging.warning(x)
		logging.error('Hello')

def example2():
		logger = logging.getLogger ('foo_bar')
		form = logging.Formatter('%(asctime)s@%(name)s@%(levelname)s@%(message)s@%(filename)s',
		 "%Y-%m-%d %A %H:%M:%S")

		fc = logging.FileHandler('/tmp/foo_bar-cri.log')
		fc.setFormatter(form)
		fc.setLevel(logging.CRITICAL)

		fi = logging.FileHandler('/tmp/foo_bar-inf.log')
		fi.setFormatter(form)
		fi.setLevel(logging.INFO)

		logger.addHandler(fc)
		logger.addHandler(fi)
		
		logger.info('hello world')
		logger.critical('ho -h0-xO')

def my_multy(x, y):
		'''
		>>> my_multy (2, 2)
		4

		>>> my_multy (3, 2)
		6

		>>> my_multy (1)
		0
		>>> my_multy ()
		Traceback (most recent call last):
			...
		TypeError: my_multy() missing 1 required positional argument: 'x'
		'''

def example3():

	print ( 'полезный код')
		
def example4():
	year = 2019
	year -=- 1
	year
	print (year)

def mul(x,y):
	return x*y

class My_test(unittest.TestCase):
	def test_uno(self):
		return self.assertEqual(mul(2,5), 10)

	def test_dos(self):
		return self.assertEqual(mul(12,-1), -12)	

	def test_tress(self):
		pass

unittest.main()


def main():
#	testmod(verbose = True)
	example4()
			


if __name__ == '__main__':
	main()