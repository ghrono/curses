#!/usr/bin/env python3.8

from datetime import datetime as dt
import sys
from time import sleep
from beeply



def main():
	try:
		alarm_time = sys.argv[1]

	except IndexError:
		print ('alarm do not activate')
		alarm_time = ''
	alarm_flag = False
	s_time = 1
	while True:
		sleep(s_time)
		print(dt.now().strftime('%H:%M:%S'), end="\r")
		if alarm_time == str (dt.now().strftime('%H:%M')):
			alarm_flag = True
			s_time = 0
		if alarm_flag:

			mybeep.hear('C',1000)
			print ('	alarma    ')



if __name__ == '__main__':
	main()