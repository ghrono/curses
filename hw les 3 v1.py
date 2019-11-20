#!/usr/bin/env python3.8

def sumdigit1():
	digit = input ( ' enter the digit ' )
	digit = int (digit)
	count = 0
	if 0 < digit <= 45 :
		for i in range (99999, -1 , -1):
			sumnum = 0
			for j in  str(i):
				sumnum += int (j)
			if sumnum == digit:
				print (i)
				count += 1
			if count  == 5:
				break 
	else:
		if digit == 0:
			print ('00000')
		else:
			print (' incorrect data entered ')

def sumdigit2():
	digit = input ( ' enter the digit ' )
	digit = int (digit)
	count = 0
	if 0 < digit <= 45 :
		i = 10000
		while count < 5 and i < 100000 :
			if sum([int(_) for _ in str (i)]) == digit:
				print (str(i))
				count += 1
			i += 1
	else:
		if digit == 0:
			print ('00000')
		else:
			print (' incorrect data entered ')

def sumdigit3():
	digit = input ( ' enter the digit ' )
	digit = int (digit)
	count = 0
	if 0 < digit <= 45 :
		for i in range (10000,99999):
			j = 0
			sumnum = 0
			while j < 5:
				sumnum += int (str(i)[j])
				j += 1
			if sumnum == digit:
				print (i)
				count += 1
			if count == 5:
				break		
	else:
		if digit == 0:
			print ('00000')
		else:
			print (' incorrect data entered ')

def sumdigit4():
	digit = input ( ' enter the digit ' )
	digit = int (digit)
	if 0 < digit <= 45 :
		count = 0
		i = 99999
		while True:
			j = 0
			sumnum = 0
			while j < 5:
				sumnum += int (str(i)[j])
				j += 1
			if sumnum == digit:
				print (i)
				count += 1
			if count == 5 or i < 10000:	
				break
			else:
				i -= 1		
	else:
		if digit == 0:
			print ('00000')
		else:
			print (' incorrect data entered ')


def exam_1_v1():
	slov = {'1' : 0}#	digit = int (input( ' enter lim numbers '))
	digit = 10 ** 1
	print ('digit = ', digit)
	for i in range (2, digit):
		iter = 0
		numb = i
		print( i, '', end ='')
		while i > 1:
			if  i % 2 == 0:
				i = i / 2
			else:
				i = i * 3 + 1
			print( int (i), '', end ='')	
			iter = iter + 1
		slov[numb] = iter
		print ('   = > ',iter)
	maxi = 0
	maxv = 0
	for i in slov:
		print (i, slov.get(i))
		if slov.get(i) > maxv:
			maxi = i
			maxv = slov.get(i)
	print ('Number = ',maxi,' iter = ',maxv)

def exam_1_v1_2():
	slov = {'1' : 0}
	digit = int (input( ' enter lim numbers '))
	digit = 10 ** 5
	print ('digit = ', digit)
	maxi = '1'
	maxv = 0

	for i in range (2, digit):
		iter = 0
		numb = i
		while i > 1:
			if  not i % 2 :
				i = i / 2
			else:
				i = i * 3 + 1
			iter = iter + 1
		if maxv < iter:
			maxi = numb
			maxv = iter
	print ('Number = ',maxi,' iter = ',maxv)

def exam_2_v1():
	slov = {1 : 0}
	digit = int (input( ' enter lim numbers '))
	print ('digit = ', digit)
	for i in range (2, digit):
		iter = 0
		numb = i
		while i > 1:
			if  i % 2 == 0:
				i = i / 2
				if i < numb:
					iter = iter + slov.get(i) + 1 
					break
			else:
				i = i * 3 + 1
			iter = iter + 1
		slov[numb] = iter
	maxi = 0
	maxv = 0
	for i in slov:
		if slov.get(i) > maxv:
			maxi = i
			maxv = slov.get(i)
	print ('Number = ',maxi,' iter = ',maxv)

def exam_2_v2():
	digit = int (input( ' enter lim numbers '))
	slov = {1 : 0}
	maxi = 1
	maxv = 0
	print ('digit = ', digit)
	for i in range (2, digit):
		iteration = 0
		numb = i
		while numb > 1:
			iteration += 1
			if not numb % 2:
				numb /= 2
				if numb < i:
					iteration += slov.get(numb) 
					break
			else:
				numb = numb * 3 + 1			
		slov[i] = iteration
		if iteration > maxv:
			maxi = i
			maxv = slov.get(i)
	print ('Number = ',maxi,' iter = ',maxv)


def table_mul():
	vari = ['a' , 'b', 'c' , 'd']
	for _ in range(4):
		print (' enter var ', vari[_], ' ',end = '')
		vari[_] = int (input ())
	print (vari)
	for _ in range (vari[0],vari[1]+1):
		print ('\t', _ , '', end = '' )
	print ()
	for i in range (vari[2],vari[3]+1):
		print (i,'', end = '' )
		for j in range (vari[0],vari[1]+1):
			print ('\t', i*j , '', end = '' ) 
		print ()


def exam_task2():
	pass


def main():
#	sumdigit1()			#for 	for
#	sumdigit2()			#while  for
#	sumdigit3()			#for 	while
#	sumdigit4()			#while  while
#	exam_1_v1()			# digit =  1000000  Number =  837799 iter =  524 [Finished in 24.4s]
#	exam_1_v1_2()		# digit =  1000000  Number =  837799 iter =  524 [Finished in 21.6s]
#	exam_2_v1()			# digit =  1000000  Number =  837799 iter =  524 [Finished in 1.4s]
#	exam_2_v2()			#digit =  10000000  Number =  8400511 iter =  685 [Finished in 13.0s]
#	table_mul()
	exam_task2()

if __name__ == '__main__':
   main()