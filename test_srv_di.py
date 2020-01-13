#!/usr/bin/env python3.8
import redis
from os import listdir
from socket import socket
import netifaces
from threading import Thread

##########################get_ip#####################################
def get_ip():
	ip = netifaces.ifaddresses('wlp4s0')[2][0].get('addr')
	return ip

def get_list_author_name():
	r_db = redis.Redis(host = 'localhost', port = 6379)
	list_author_name = []
	for author_name in r_db.keys('*'):
		list_author_name.append(author_name.decode('utf-8'))
	return list_author_name

def get_list_book_name(author_name):
	r_db = redis.Redis(
		host = 'localhost',
		port = 6379)
	return (r_db.hkeys(author_name))

def serv_init_socket(ip,port):
	server = socket()
	server.bind((ip, port))
	server.listen()
	return server

def send_response(msg, socket4connect):
	text2request = str(len(msg)) + ' ' + msg
	stop_index = len(text2request)
	index = 0
	while True:
		msg = text2request[index].encode('1251')
		socket4connect.send(msg)
		index += 1
		if index == stop_index:
			break

def get_request(socket4connect):
	request = ''
	flag = True
	index = -1
	while True :
		symbol = str(socket4connect.recv(1).decode('utf-8'))
		if flag and symbol == ' ':
				index = int(request)
				request = ''
				flag = False
				continue
		request += symbol
		if len(request) == index:
			break
	return request

def serv():
	serv_soc = serv_init_socket(get_ip(), 9090)
	client, addr = serv_soc.accept()
	if get_request(client).split('##')[0] == 'GET_LIST_AUTHOR':
		rs = get_list_author_name()
		send_response(str(rs), client)


	serv_soc.close()



def main():
	print ('Ip address server : ', get_ip())
	serv()


if __name__ == '__main__':
	main()