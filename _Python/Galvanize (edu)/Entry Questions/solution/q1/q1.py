#
# Roman Gekhman - 
# Galvanize Coding Exercise 6/26/18
# roman.gekhman@gmail.com
# 
# Description: 
#	The program should output:
#	1. The total word count - (done)
#	2. The count of unique words - (done)
#	3. The number of sentences - (done)
#	Example output:
#	Total word count: 468
#	Unique words: 223
#	Sentences: 38
#				 
#	Brownie points will be awarded for the following extras:
#	1. The ability to calculate the average sentence length in words - (done)
#	2. The ability to find often used phrases (a phrase of 3 or more words used over 3 times) (use of PyTextRank) - (not done, requires additional time)
#	3. A list of words used, in order of descending frequency - (done)
#	4. The ability to accept input from STDIN, or from a file specified on the command line. - (done)
#
#	Note: Developed / tested on Python 3.6.5
#
# usage: c:\>python q1.py --file <input filename>
#
from collections import Counter
import string
import argparse

try:
	#input filename arguments 
	parser = argparse.ArgumentParser()   
	parser.add_argument("--file", "-f", type=str, required=True)
	args = parser.parse_args()

	#open a file with text, read text
	_text1 = ""
	with open(args.file, 'r') as _file:
		_text1 = _file.readlines()

	# remove punctuation characters
	_excl = set(string.punctuation)
	_str = ''.join(_char for _char in _text1 if _char not in _excl)

	# Get a list of sentences and sentence count
	_strList  = _str.replace('\n','').strip().split('.')
	_strList = list(filter(None, _strList))
	_cntSentences = len(_strList)

	#get total word count
	_str = _str.replace('.','')
	_cntWords = len(_str.split())

	#Count word occurences
	_cList = Counter(_str.split()).most_common()

	#get counts of all occurences
	_setCount = set(map(lambda x: x[1], _cList))

	#reverse sort of a count
	_setCount = sorted(_setCount, key=lambda _x: _x, reverse=True)

	#Create a list of tuples with the lists of word counts sorted descending and respective words sorted ascending	
	_cList = [(sorted([ _y[0] for _y in _cList if _y[1]== _x], key=lambda _x: _x, reverse=False), _x) for _x in _setCount]

	#get count of unique words
	_cUniqList = [t[0] for t in _cList if t[1] == 1]
	_cntUniqWords = len(_cUniqList[0])

	#Output summary results on screen
	print("Total word count: ", _cntWords)
	print("Unique words: ", _cntUniqWords)
	print("Sentences: ", _cntSentences)
	print("Average Sentence Length: ", _cntWords / _cntSentences)

	#output a list of words in order of descending frequency and ascending alphabetically
	print("\nOutput a list of words in order of descending frequency and ascending alphabetically")
	for _item in _cList:
		for _word in _item[0]:
			print(_item[1], _word)

except Exception as ex:
	print ("Error : ", ex.args)