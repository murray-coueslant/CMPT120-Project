# an experiment which will generate random 3*3 maps with six explorable locations
# Murray Coueslant, 2017/09/18

# module imports
from random import shuffle

# variable and array definitions
rows = 3
cols = 3
gameMap = [[0 for i in range(cols)] for j in range(rows)]
mapLocations = ['a', 'b', 'c', 'd', 'e', 'f']

# map generator


def generateMap(locationList):
    unusedLocations = locationList
    numberOfLocations = len(unusedLocations)
    orderList = list(range(numberOfLocations))
    shuffle(orderList)
    

def assignLocation(location, map):
    map[0][0] = location


generateMap(mapLocations)
