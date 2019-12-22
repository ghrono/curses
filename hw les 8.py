#!/usr/bin/env python3.8
import redis
from os import listdir
from socket import socket
#from netifaces import interfaces, ifaddresses, AF_INET
import netifaces
from threading import Thread
from time import sleep
from select import select

##########################get_ip#####################################
def get_ip():
	ip = netifaces.ifaddresses('wlp4s0')[2][0].get('addr')
	return ip
#########################end get_ip##################################


###################   add bbok to DB   ##############################
def write_2_db(author, name_book, content):
	r_db = redis.Redis(
		host = 'localhost',
		port = 6379)
	r_db.hset(author, name_book, content)

def get_content(full_path):
	with open(full_path, mode = 'r', encoding= 'Windows-1251') as file:
		content = file.read()
	return content

def add_book_in_DB(library_path):
	all_books = listdir(library_path)
	for book in all_books:
		full_path = library_path +'/'+ book
		author_name = book.split('__')[0]
		book_name = book.split('__')[1]
		content = get_content(full_path)
		write_2_db(author_name, book_name, content)

def auto_add_book_2_DB(library_path, pause):
	while True:
		get_list_book_name(library_path)
		sleep(pause)
	#  add  function add only new book.

############### end add bbok to DB  ################################

def get_list_book_name(author_name):
	r_db = redis.Redis(
		host = 'localhost',
		port = 6379)
	print (r_db.hkeys(author_name))


def get_list_author_name():
	r_db = redis.Redis(
		host = 'localhost',
		port = 6379)
	return r_db.keys('*')	

###########################  serv   ################################

def serv_init_socket(ip,port):
	server = socket()
	server.bind((ip, port))
	server.listen()
	return server

def send_msg2client(text, client):
	index = 0
	stop_index = len(text)
	print (stop_index)
	while True:
		msg = text[index].encode('1251')
		client.send(msg)
		index += 1
		if index == stop_index:
			break
		yield

def get_request_client(client):
	pass

def ser():
	srv = serv_init_socket(get_ip(), 9090)
#	client, addr = srv.accept()
#	print(f'accept connect by addr {addr}, {client}')
	spis = get_list_author_name()
	li = []
	for row in spis:
		li.append(str(row).strip("b'") + '\n')

	print (li)
	response = {}

	while True:
		ready2read, ready2write, _ = select([srv], response, [])
	
		if ready2read:
			client, addr = srv.accept()
			print(f'accept connect by addr {addr}')
			response[client] = send_msg2client(li, client)
	
		for sock in ready2write:
			try:
				next(response[sock])
			except StopIteration:
				del response[sock]

def main():
	print ('Ip address server : ', get_ip())
	library_path = "/home/ghrono/Документы/books"
#	Thread(target=auto_add_book_2_DB, args=(library_path, 30)).start()
#	get_list_book_name("Ertel'")
	ser()
	#get_list_author_name()

if __name__ == '__main__':
	main()