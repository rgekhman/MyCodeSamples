#
# Roman Gekhman Coding Exercise 4/6/18
# roman.gekhman@gmail.com
# 
# Description: This program reads text from a file and returns the counts of 
#				all the words in descending word count order. 
#				 
# Note: Developed / tested on Python 3.6.5
#
# usage: c:\>python word_count.py
#
from collections import Counter
import string
import os

try:
	currPath = os.path.dirname(os.path.realpath(__file__))

	#open a file with text, read text
	_text1 = ""
	with open(currPath + "\\text.txt", 'r') as _file:
		_text1 = _file.readlines()

	# remove punctuation characters
	_excl = list(set(string.punctuation))

	_str = ''.join(_char for _line in _text1 for _char in _line if _char not in _excl)

	#Count word occurences
	_cList = Counter(_str.split()).most_common()

	#get counts of all occurences
	_setCount = set(map(lambda x: x[1], _cList))

	#reverse sort of a count
	_setCount = sorted(_setCount, key=lambda _x: _x, reverse=True)

	#Create a list of tuples with the lists of words sorted ascending and respective word counts 
	_cList = [(sorted([ _y[0] for _y in _cList if _y[1]== _x], key=lambda _x: _x, reverse=False), _x) for _x in _setCount]

	#Output results on screen
	for _item in _cList:
		for _word in _item[0]:
			print(_item[1], _word)

except Exception as ex:
	print ("Error : ", ex.args)