#!/usr/bin/env python3.8

from os import listdir
from collections import defaultdict

def get_clear_content(full_path):
	with open(full_path, mode = 'r', encoding= 'Windows-1251') as file:
			content = file.read()
			content = content.lower()
			content = content.replace(",", '')
			content = content.replace(".",'')
			content = content.split()
			content = set(content)
	return content

def get_words_in_books(library_path):
	all_books = listdir(library_path)
	words_in_books = defaultdict(list)
	for book_name in all_books:
		full_path = library_path +'/'+ book_name
		content = get_clear_content(full_path)
		for word in content:
			words_in_books[word].append(book_name)
	return  words_in_books		

def treatment_user_request(user_request, words_in_books):
	user_request = user_request.split( )
	response = set ()
	if len (user_request) == 1 and user_request[0] in words_in_books:
		for book in words_in_books.get(user_request[0]):
			response.add(book)
		return response
	if len (user_request) > 1:
		book_4_sort = []
		for user_request_word in user_request:
			if user_request_word in words_in_books:
				book_4_sort.append(words_in_books.get(user_request_word))
			else:
				response.add ('таких книг нету')
				return response
		for books in book_4_sort:
			book_4_sort[0] = set (books) & set (book_4_sort[0]) 
		for book in book_4_sort[0]:
			response.add(book)
	else:
		response.add('таких книг нету')
	return response

def main():
	library_path = "/home/ghrono/Документы/books"
#	library_path = "/home/ghrono/Документы/sm"
	words_in_books = get_words_in_books (library_path)
	user_request = input ('Введите слов(о/а) для поиска: ')
	response = treatment_user_request(user_request, words_in_books)
	for row in response:
		print (row)

if __name__ == '__main__':
	main()