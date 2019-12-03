#!/usr/bin/env python3.8


def file_open(filein):
	with open ( filein, mode = 'r', encoding= 'Windows-1251'  ) as raw_data:
		raw_file = sorted (raw_data)
	return raw_file

def find_anagrams(file):
	dictonary_anagrams = {}
	for line in file:
		key = str (sorted (line))
		if  key in dictonary_anagrams:
			dictonary_anagrams.get(key).append(line.rstrip())
		else:
			dictonary_anagrams[key] = [line.rstrip()]		
	return dictonary_anagrams.values()

def file_save(fileout, dictonary_anagrams):
	dictonary_anagrams = sorted ( dictonary_anagrams, key = lambda item: -len (item) )
	with open ( fileout, mode = 'w', encoding= 'Windows-1251' ) as out_file:    
		for line in dictonary_anagrams:
			if len (line) == 1:
				break
			for word in line:
				out_file.write( word +' ')
			out_file.write('\r\n')

def anagrams(filein, fileout):
	file = file_open( filein )
	anagrams_file = find_anagrams( file )
	file_save ( fileout, anagrams_file )
	
def main():
	anagrams( '/tmp/zaliznyak.txt', '/tmp/anagrams.txt' )

if __name__ == '__main__':
   main()