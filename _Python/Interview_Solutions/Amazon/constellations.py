#
#Assuming that a galaxy of stars can be represented in a 2d matrix where 0's are void space between 
#stars and non-zero numbers are stars, find constellations of neighboring stars and present in 1d format. 
#
#2D MATRIX
#
#1,1,0,2
#0,1,0,3
#0,0,4,0
#6,0,7,9
#
# Expected output: 
#
#[1,1,1,4,7,9,3,2]
#[6]

#[[1,1,0,2,1]
# [0,1,0,0,0]
# [0,0,4,0,0]
# [6,0,7,9,0]]


class Star:
	def __init__(self, x, y, val):
		''' Init a Star '''
		self._neighbours = []
		self._x = x
		self._y = y
		self._visited = False
		self._val = val

	def __repr__(self):
		return "(x:{}, y:{}, val:{})\n".format(self._x, self._y, self._val)

	def find_neighbour_stars(self, _galaxyDict):
		_neighbours = []
		if self._val > 0:
			for _x in range(self._x-1, self._x+2):
				for _y in range(self._y-1,self._y+2):
					if (self._x,self._y)!=(_x,_y): 
						_key = str(_x)+str(_y)
						if _key in _galaxyDict.keys():
							#skip zeroes
							if _galaxyDict[_key]._val > 0:
								_neighbours.append(_galaxyDict[_key])
		self._neighbours = _neighbours 

class Galaxy:
	def __init__(self, galaxy):
		''' Init Galaxy '''
		self._galaxy = []					# 2d matrix of stars
		self._galaxyDict = dict()			# Dict lookup for matrix indices '11','12','13', etc. vs Star() objects
		self._constellations = []			# Output List of Constellations 

		i = 0
		j = 0
		
		''' Populate and map the galaxy 2D matrix '''
		for _1d in galaxy:
			i += 1
			_objLevel = []
			for _star in _1d:
				j += 1
				_newStar = Star(i,j,_star)
				_objLevel.append(_newStar)
				self._galaxyDict[str(i)+str(j)] = _newStar
			self._galaxy.append(_objLevel)
			j = 0

	def initStarNeighbours(self):
		''' Find all neighbours '''
		for _1d in self._galaxy:
			for _star in _1d:
				#print("Star x:{} y:{}".format(_star._x, _star._y))
				_star.find_neighbour_stars(self._galaxyDict)
				#print("Non-zero Neighbours: {}".format(_star._neighbours))

	def buildConstellations(self):
		''' Go through each star and attempt to build constellations '''
		
		while True:
			# find unvisited stars
			stars = [ _star for _stars in self._galaxy for _star in _stars if _star._val > 0 and _star._visited == False ]

			# build constellation from a very firt star
			if len(stars) > 0:
				_constellation = []
				_constellation = self.buildConstellation(stars[0], None, _constellation)
					
				if _constellation: 
					if len(_constellation) > 0:
						self._constellations.append(_constellation)
			else:
				break

		print("List of Constellations \n")
		for i in self._constellations:
			print("Constellation : \n{}\n".format(i))


	def  buildConstellation(self, node, parent, constellation):
		
		if not node._visited:
			constellation.append(node)
			node._visited = True

		neighbours = (x for x in node._neighbours if not x._visited)
		
		for neighbour in neighbours:
			constellation = self.buildConstellation(neighbour, node, constellation)

		return constellation
		
#_galaxy = Galaxy([[1,1,0,2],[0,1,0,3],[0,0,4,0],[6,0,7,9]])
_galaxy = Galaxy([[1,1,0,2,1],[0,1,0,0,0],[0,0,4,0,0],[6,0,7,9,0]])

_galaxy.initStarNeighbours()

_galaxy.buildConstellations()
