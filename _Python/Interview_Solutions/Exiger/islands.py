
# Objective: Return a count of islands
#
_lst_ocean = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 1, 1, 1, 1],
       [0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
       [0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

#_lst_ocean = [[0, 0, 0, 0, 0],
#			  [0, 1, 0, 0, 0],
#			  [0, 1, 0, 1, 1],
#			  [0, 1, 0, 1, 1],
#			  [0, 0, 0, 0, 0],
#			  [0, 0, 0, 0, 0]]


#print('Hello world - Python!')

class Ocean:
    def __init__ (self, ocean):
        ''' init Ocean '''
        self._ocean = []                # 2d matrix of islands'
        self._oceanDict = dict()        # Dict lookup for matrix of indices 11, 12, 13 etc
        self._islands = []              # Output list of islands'

        i = 0
        j = 0

        # populate and map the 2d matrix
        for _1d in ocean:
            i += 1
            _objLevel = []
            for _island in _1d:
                j += 1
                _newIsland = Island(i, j, _island)
                _objLevel.append(_newIsland)
                #print(_newIsland)
                self._oceanDict[str(i)+ str(j)] = _newIsland
            self._ocean.append(_objLevel)
            j = 0
    
    def initNeighbours(self):
        for _1d in self._ocean:
            for _island in _1d:
                _island.find_neighbours(self._oceanDict)

    def buildIslands(self):
        ''' Go through each cell and build islands '''
        while True:
            # find unvisited cells (islands)
            islands = [_island for _islands in self._ocean for _island in _islands if _island._val > 0 and _island._visited == False]

            #build island from a very first cell
            if len(islands) > 0:
                _island = []
                _island = self.buildIsland(islands[0], None, _island)

                if _island:
                    if len(_island) > 0:
                        self._islands.append(_island)
            else:
                break

        print("List of Islands \n")
        for i in self._islands:
          print("Island : \n{}\n".format(i))

    def buildIsland(self, node, parent, island):
        ''' Go through each cell and build islands '''

        if not node._visited:
            island.append(node)
            node._visited = True

        neighbours = [x for x in node._neighbours if not x._visited]

        for neighbour in neighbours:
            island = self.buildIsland(neighbour, node, island)

        #print(island)
        return island
        

class Island:

    def __init__ (self, x, y, val):
        ''' Init island '''
        self._neighbours = []
        self._x = x
        self._y = y
        self._visited = False
        self._val = val

    def find_neighbours(self, _oceanDict):
      _neighbours = []
      if self._val > 0:
        for _x in range(self._x-1, self._x+2):
          for _y in range(self._y-1, self._y+2):
            if (self._x, self._y) != (_x, _y):
              _key = str(_x) + str(_y)
              if _key in _oceanDict.keys():
                #skip zeroes
                if _oceanDict[_key]._val > 0:
                  _neighbours.append(_oceanDict[_key])
          self._neighbours = _neighbours
          #print(self._neighbours)

    def __repr__(self):
        return "(x:{}, y:{}, val:{})".format(self._x, self._y, self._val)

_ocean = Ocean(_lst_ocean)

_ocean.initNeighbours()

_ocean.buildIslands()

print("Count of islands is {}".format(len(_ocean._islands)))

# 1:1, 1:2, 1:3, ... 1:10
# 2:1, 2:2, 2:3, ... 2:10
#....
# 10:1, 10:2, 10:3, ... 10:10


#[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 1, 0, 0, 0, 0, 1, 1, 1, 1],
# [0, 1, 0, 1, 1, 0, 1, 1, 1, 1],

#"1": 2:1, 3:1 ...
#"2": 2:1, 3:1 ...
#"3": 2:1, 3:1 ...
