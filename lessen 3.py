#!/usr/bin/env python3.8


def les2 ():
	row = "hello world"
	count = 0
	while count < len( row):
		print (row [count])
		count += 1

def les3():
	text = '''В заросшем парке стоит старинный дом
Забиты окна и мрак царит из вечно в нем
Сказать я пытался чудовищ нет на Земле
Но тут же раздался ужасный голос во мгле
Голос во мгле
Мне больно видеть белый свет
Мне лучше в полной темноте
Я очень много много лет
Мечтаю только о еде
Мне слишком тесно в заперти
И я мечтаю об одном
Скорей свободу обрести
Прогрысть свой ветхий старый дом
Проклятый старый дом
Был дед да помер слепой и жутко злой
Никто не вспомнил о нем зимой холодной
Соседи не стали его тогда хоронить
Лишь доски достали решили заколотить
Двери и окна
Мне больно видеть белый свет
Мне лучше в полной темноте
Я очень много много лет
Мечтаю только о еде
Мне слишком тесно в заперти
И я мечтаю об одном
Скорей свободу обрести
Прогрысть свой ветхий старый дом
Проклятый старый дом
И это место стороной проходит сельский люд
И суеверные твердят-
"Там призраки живут"'''
#	mydic.get('brat', "hello")
	slov = {}
	text = text.lower()
	s1 = set (text)
	for _ in s1:
		slov[_] = text.count(_)

	for _ in slov:
		print (_)


	items = list (slov)
	print (items)

def les4():
	digit = input ( ' enter the digit ' )
	digit = int (digit)
	count = 0

	for i in range (99999, -1 , -1):
		#stri = str (i)
		#stri = stri [::-1]
		count2 = 0
		for j in  str(i):
			count2 += int (j)
		if count2 == digit:
			print (i)
			count += 1
		if count >5:
			break 

def les5():
	digit = input ( ' enter the digit ' )
	digit = int (digit)
	count = 0
	if 0 <= digit <= 45 :
		i = 0
		while count < 5 and i < 100000 :
			if sum([int(b) for b in str (i)]) == digit:
				print (str(i))
				count += 1
			i += 1
	else:
		print (' incorrect data entered ')


def main():
#	les2()
#	les3()
#	les4()
	les5()





if __name__ == '__main__':
   main()