#!/usr/bin/env python3.8

from socket import socket
import netifaces

def get_ip():
	ip = netifaces.ifaddresses('wlp4s0')[2][0].get('addr')
	return ip

def send_request(msg, socket4connect):
	text2request = str(len(msg)) + ' ' + msg
	stop_index = len(text2request)
	index = 0
	while True:
		msg = text2request[index].encode('1251')
		socket4connect.send(msg)
		index += 1
		if index == stop_index:
			break

def get_response(socket4connect):
	response = ''
	flag = True
	index = -1
	while True :
		symbol = str(socket4connect.recv(1).decode('utf-8'))
		if flag and symbol == ' ':
				index = int(response)
				response = ''
				flag = False
				continue
		response += symbol
		if len(response) == index:
			break
	return response

def init_connect_2_srv():
	socket4connect = socket()
	socket4connect.connect((get_ip(), 9090))
	return socket4connect

def make_str_request(x, y = '', z = ''):
	request = x + '##' + y + '##' + z + '##'
	return request

def get_author_in_lib(socket4connect):
	request = make_str_request ('GET_LIST_AUTHOR')
	send_request(request, socket4connect)
	response_list_author = get_response(socket4connect)
	return response_list_author

def get_books_one_author(author_name, socket4connect):
	request = make_str_request ('GET_LIST_BOOKS', author_name)
	send_request(request, socket4connect)
	response_books_author = get_response(socket4connect)
	return response_books_author

def get_one_book(author_name, book_name, socket4connect):
	request = make_str_request ('GET_BOOK', author_name, book_name)
	send_request(request, socket4connect)
	response_book = get_response(socket4connect)
	return response_book


def client():
	connect_2_srv = init_connect_2_srv()
	li = get_author_in_lib(connect_2_srv).split(',')
	
	for blb in li:
		print (blb.split("'"))
	connect_2_srv.close()


def main():
	client()
		
if __name__ == '__main__':
	main()