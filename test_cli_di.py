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
				index = int(msg)
				response = ''
				flag = False
				continue
		response += symbol
		if len(response) == index:
			break
	return response






def clie():
	

	text = 'hello woreld!.....1.12345678901234567823456787654323456787654323456789876543234567876543234567876543.#..'
	#text += 'EOF'
	index = 0
	

	text = str (len(text)) + ' ' + text
	stop_index = len(text)
	print (text)
	

	client = socket()
	client.connect((get_ip(), 9090))


	while True:
		msg = text[index].encode('1251')
		client.send(msg)
		index += 1
		if index == stop_index:
			break


	

#	print(client.recv(1))

	client.close()

def get_list_author_name():
	r_db = redis.Redis(host = 'localhost', port = 6379)
	list_author_name = []
	for author_name in r_db.keys('*'):
		list_author_name.append(author_name.decode('utf-8'))
	return list_author_name



def main():
	print ('Ip address server : ', get_ip())
#	clie()
	li = get_list_author_name()
	for l in li:
		print (l)

if __name__ == '__main__':
	main()