#
# Roman Gekhman Coding Exercise 4/6/18
# roman.gekhman@gmail.com
# 
# Description: This program reads text from a file and returns the counts of 
#				all the words in descending word count order. 
#				 
# Note: Developed / tested on Python 3.6.5
#
# usage: c:\>python <folder>/graph.py
#
#
#	Consider a directed graph of small integer values, where each integer is a positive number
#		and each integer is unique. Each unique integer node has zero or more child nodes.
#	Write 3 functions that:
#	1. Create a node in a graph.
#	2. Inserts a node as a child of an existing node.
#	3. Print a graph.
#	Do not use an existing graph library. You need to write the 3 functions:
#	1. Create(new node with an integer value)
#	2. Insert (node as child of an existing node)
#	3. Print (graph)
#	Create and Insert must ensure in a language-idiomatic way that the graph is acyclic - a node
#		must not directly or indirectly point to itself.
#

def printGraph():
	for _key in sorted(_graph.keys()):
		print("{} -> {}".format(_key, printChildren(_graph[_key])))

def printChildren(_node):
	if not _node: 
		return "No Children" 
	else: 
		return ",".join(str(_x) for _x in _node)

#create graph node
def Create(_n):
	_graph[_n] = []

#
# check the foloowing:
# 1. self - refernce
# 2. deep references 
def hasCyclicalRef(_key, _val):
	_res = False

	# Shallow check 1.
	#Check if referncing itself
	if _val == _key:
		return True

	# shallow scan (of transposed graph)
	# is possible here to quicken insertion algorythm in some cases. 
	# (see explanation below, in a header of isParentExists() function)
	# if isInTransposedGraph(_key, _val):
	#	return True

	# deep scan (multilevel)
	if isParentExists(_val, _key):
		return True

	return _res

#
# Deep scan of the branches 
# Traverse the graph to find if parent exists 
# The assumption is that it does, so call _child node being inserted as if it was a parent and search 
# all nodes till path is found. If found - return true, if not - false.
#
# For the sake of performance, this step can be slightly quickened by skipping the deep scan in some cases. 
# Here is how: Create a mirrored graph (transposed graph) where all the mirrored slots of the original 
# graph's occupied cells cannot be assigned by the definition of the acyclic graph. 
# for example: If Parend 1 has child 4,  will   
def isParentExists(_parent, _child):
	_res = False
	#if assumed parent has empty list of children - it is no parent.  
	if not _graph[_parent]:
		return False
	else:
		#iterate proposed parent's branches all a way down till last one 
		for _node in _graph[_parent]:
			if _child == _node:
				return True
			else:
				_res = isParentExists(_node, _child)
				if _res:
					return True

#			
# Valide Node can be inserted if all conditions are met: 
#	1. Parent node exists 
#	2. Node does not already exists in a list of children nodes 
#	3. Node has no cyclical ref
def isValid(_key, _val):
	_res = False

	try:
		#check if parent exists
		if not _val in _graph.keys():
			raise Exception("Parent node {} does not exist.".format(_val))

		#do not insert duplicates in children
		if _val in _graph[_key]:
			raise Exception("Cannot insert duplicate {} in a list of leaves {} for {}".format(
				_val, ",".join(str(_x) for _x in _graph[_key]), _key))
		
		#check for cyclical refs
		if hasCyclicalRef(_key, _val):
			raise Exception("Cannot insert child node {} for parent node {} as it would create a cycle".format(
			_val, _key))
		else:
			_res = True
	except Exception as ex:
		print( "Error {} ", ex.args)
	return _res

def Insert(_cmd):
	_keyVal = _cmd.split("as child of")
	_val = int(_keyVal[0])
	_key = int(_keyVal[1])
	try:
		if _key in _graph.keys():
			#append if node value passed validation
			if isValid(_key, _val):
				_graph[_key].append(_val)

		else:
			raise Exception("Node {} does not exist. Execute Create({}) command first".format(_key, _key))
	except Exception as ex:
		print( "Error {} ", ex.args)

def outputGraph():
	#Output
	print("\n_Graph")
	printGraph()

def resetGraph():
	for _key in _graph:
		_graph[_key] =[]

#Create / Build graph (parent to children 1 : n)
_graph = {}

Create(1) 
Create(2)
Create(3)
Create(4)
Create(5)
Create(6)

print("\n\n *** test case1 ***\n")
Insert("2 as child of 2")
Insert("2 as child of 1")
Insert("3 as child of 1")
Insert("4 as child of 1")
Insert("1 as child of 4")
Insert("5 as child of 2")
Insert("6 as child of 3")
Insert("3 as child of 4")
Insert("6 as child of 4")
Insert("6 as child of 5")
Insert("3 as child of 1")

outputGraph()

resetGraph()

print("\n\n *** test case2 ***\n")
Insert("3 as child of 1")
Insert("4 as child of 1")
Insert("3 as child of 4")
Insert("5 as child of 3")
Insert("3 as child of 3")
Insert("6 as child of 3")
Insert("6 as child of 4")
Insert("3 as child of 5")
Insert("2 as child of 5")
Insert("1 as child of 2")

outputGraph()

resetGraph()

print("\n\n *** test case3 ***\n")
Insert("5 as child of 3")
Insert("5 as child of 1")
Insert("4 as child of 3")
Insert("2 as child of 4")
Insert("1 as child of 2")
Insert("5 as child of 1")
Insert("6 as child of 5")
Insert("1 as child of 6")

outputGraph()

	