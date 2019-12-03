#!/usr/bin/env python3.8

from os import listdir

def fun (*args):
	for i in args:
		print (i)


def main():
	ll = ('rrr', 'rrr', 'rrr', 'rrr')
	fun (*ll)

if __name__ == '__main__':
   main()





	print (len (user_request))
	if words_in_books.get( *user_request):
		if len (user_request) == 1:

			for nn in words_in_books.get( user_request, 'None'):
				response.add(nn)
		else:
			for nn in words_in_books.get( word_in_user_request[0]):
					response.add(nn)

			for word_in_user_request in user_request:	
				stfff = set ()
				for nn in words_in_books.get( word_in_user_request):
					stfff.add(nn) 

				response = response & stfff
	else:	response.add ('таких слов нет')