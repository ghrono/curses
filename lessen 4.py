#!/usr/bin/env python3.8


def multy( x , y = 5):
	
	return	x*y

def encoder(text):
	st = ''
	for char in text:
		st += chr( ord(char) + 5)
	return st	

def decoder(text):
	st = ''
	for char in text:
		st += chr( ord(char) - 5)
	return st


def sum_char_txt(wor):
	sumchar = 0
	for char in wor:
		sumchar += ord(char)
	return sumchar	

def fil():
	spis = ['Olga', 'Eva', 'Adam', 'Moisiy', 'Elementiy', 'Valentina']
	print ( sorted( spis, key = sum_char_txt))

	with open ( '/tmp/testfile.txt', 'w') as file:
		for i in range(100):
			file.write(str (i) + '\n')

def test_list():
	li = []
	for x in range(1,10):
		li.append(x)
		print (li, end ='')
		li[-1] += li [-1]
		print (li)




def main():
#	print (multy(2))
#	ff = encoder('Hello world!')
#	print (ff)
#	print (decoder (ff))
	print ()
	test_list()






if __name__ == '__main__':
   main()