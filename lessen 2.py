#!/usr/bin/env python3.8

def feb():
	print (" найти все числа feb до 100")
	fiblist = [0 ,1]
	for _ in range(100):
		fiblist.append( int( fiblist[-1]) + int( fiblist[-2]) )
		if int( fiblist[_] ) > 100:
			break
		print(fiblist[_],'', end = '')
	print ()

def feb1():
	print (" найти все числа feb до 100")
	fiblist = [0 ,1]
	for _ in range(100):
		fiblist.append( int( fiblist[-1]) + int( fiblist[-2]) )
		if int( fiblist[_] ) < 100:
			print(fiblist[_],'', end = '')
	print ()

def feb2():
	print (" найти все числа feb до 100")
	a,b = 0,1
	for _ in range (20):
		if a < 100 : 
			print (a, '', end = '')
			a,b = b, a+b
	print ()

def feb3():
	print (" найти все числа feb до 100")
	fiblist = []
	a,b = 0,1
	for _ in range (20):
		if a < 100 : 
			fiblist.append(a)
			a,b = b, a+b
	print (fiblist)
	del a,b, fiblist

def feb4():
	print (" найти все числа feb до 100")
	fiblist = [0, 1]
	for _ in range(100):
		if fiblist[-1]+fiblist[-2] < 100:
			fiblist.append(fiblist[-1]+fiblist[-2])
	print (fiblist)
 

def simplenum():
	print (" найти все простые чила до лимита")
	ren = input ('введите лимит поиска простых чисел ')
	ren = int(ren)
	simlist = [1,2,3]
	if (ren > 3): 
		for i in range(5,ren,2):
			flag = 1
			for j in range(2,i):
				if not (i % j):
					flag = 0
					break
			if flag:
				simlist.append(i)
		print (*simlist)
	else:
		for i in range(ren):
			print (simlist[i],'', end = '')
		print()

def simplenum1():
	print (" найти все простые чила до лимита")
	ren = input ('введите лимит поиска простых чисел ')
	ren = int(ren)
	listraw = list(range(1,ren+1))
	for i in range (1,len (listraw)):
		if listraw[i]:
			for j in  range (i+1,len (listraw)):
				if listraw[j]:
					if  not (listraw[j] % listraw[i]):
						listraw[j] = 0
	for i in range (len (listraw)):
		if listraw[i]:
			print (listraw[i],'', end = '')
	print()

def simplenum2():
	print (" найти все простые чила до лимита")
	ren = input ('введите лимит поиска простых чисел ')
	ren = int(ren)
	listraw = [1]
	for i in range (2,ren+1):
		flag = 1
		for j in  range (1,len(listraw)):
			if  not (i % listraw[j]):
				flag = 0
				break
		if flag:
			listraw.append(i)
	for i in range (len(listraw)):
		print (listraw[i],'', end = '')
	print ()

def simplenum3():
	print (" найти все простые чила до лимита")
	ren = input ('введите лимит поиска простых чисел ')
	ren = int(ren)
	listraw = [1]
	for _ in range (2,ren):
		listraw.append(_)
		for j in  range (1,len(listraw)-1):
			if  not ( _  % listraw[j]):
				listraw.pop(-1)
				break
	print (*listraw)


def sumnum():
	sumnum = 0
	print (" найти сумму цифр числа digit")
	pislo = input ('enter digit ')
	for _ in pislo:
		sumnum += int(_)
	print ('Summ Numbers = ',sumnum) 


def main():
	feb()
	feb2()
	feb3()
	feb4()
	simplenum()
	simplenum1()
	simplenum2()
	simplenum3()
	sumnum()

if __name__ == '__main__':
   main()
   