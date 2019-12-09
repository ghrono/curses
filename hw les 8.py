#!/usr/bin/env python3.8
import redis
from os import listdir
import socket
from netifaces import interfaces, ifaddresses, AF_INET
import netifaces


def read_write_2_db():
	r_db = redis.Redis(
		host = 'localhost',
		port = 6379)
	r_db.set('foo', 'bar')
	value = list (r_db.get('foo'))
	print(value)






def main():
	read_write_2_db()
	hostname = socket.gethostname()    
	IPAddr = socket.gethostbyname(hostname)    
	print("Your Computer Name is:" + hostname)    
	print("Your Computer IP Address is:" + IPAddr)   

	for ifaceName in interfaces():
		addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
		print ('%s: %s' % (ifaceName, ', '.join(addresses)))
	print (netifaces.interfaces()) 
	#wlp4s0
	print (netifaces.ifaddresses('wlp4s0')[2][0].get('addr'))

if __name__ == '__main__':
	main()