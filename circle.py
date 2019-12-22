#!/usr/bin/env python3.8
import math

def cir(r=10):
	circ = [[' ']*(r+1) for i in range(r+1)]
	last_x = 0
	for y in range(r+1):
		x = round(math.sqrt(r ** 2 - y ** 2))
		circ[x][y] = '#'
		for x_t in range (x,last_x):
			circ[x_t][y] = '#'
		last_x = x
	for row in circ[::-1]:
		print (*row[::-1] + row)
	for row in circ:
		print (*row[::-1] + row)

def main():
	cir()




if __name__ == '__main__':
	main()