#!/usr/bin/env python3.8
from time import sleep
from threading import Thread
from socket import socket
import select

def fib(n):
	if n<=1:
		return n
	return (fib(n-1)+fib(n-2))

def fact(n):
	if n:
		return (n * fact(n-1))
	else:
		return 1	

def my_pow(x, y):
	if y:
		return x * my_pow(x, y - 1)
	else:
		return 1

def elka(st):
	if st:
		return (str (elka(st[:-1])) + '\n' + st )
	else:
		return ""

def hello(name, pause):
	while True:
		print(name)
		sleep(pause)

def example_tread():
	t1 = Thread(target = hello, args =('egor',3))
	t2 = Thread(target = hello, args = ('pavel',5))
	t1.start()
	t2.start()

def my_in(client_sock):
	while True:
		msg = input ( 'enter msg: ')
		msg = msg.decode('Windows-1251')
		client_sock.send(msg)

def cli_ch():
	client = socket()
	client.connect(('192.168.19.82',5000))

	Thread (target = my_in, args = (client)).start()

	while  True:
		new_msg = client.recv(32)
		#new_msg = new_msg.encode('Windows-1251')
		print (new_msg)


def main():
	print (fib(7))
	print (fact(5))
	print(my_pow(2, 3))
	print (elka('hello world'))
#	example_tread()
	cli_ch()


if __name__ == '__main__':
	main()