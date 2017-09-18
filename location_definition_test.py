# an experiment which will generate random 3*3 maps with six explorable locations
# Murray Coueslant, 2017/09/18

# module imports
from random import shuffle, randint

# variable and array definitions
rows = 3
cols = 3
gameMap = [[None for i in range(cols)] for j in range(rows)]
mapLocations = ['a', 'b', 'c', 'd', 'e', 'f']

# map generator


def generateMap(locationList):
    locations = locationList
    numberOfLocations = len(locations)
    orderList = list(range(numberOfLocations))
    shuffle(orderList)
    for i in orderList:
        assignLocation(locations[i], gameMap)
    fillEmpty(gameMap)
    print(gameMap)


def assignLocation(location, map):
    rand_row = randint(0, 2)
    rand_col = randint(0, 2)
    placed = False
    while not placed:
        if map[rand_row][rand_col] == None:
            map[rand_row][rand_col] = [location, False]
            placed = True
        else:
            rand_row = randint(0, 2)
            rand_col = randint(0, 2)


def fillEmpty(map):
    for j in range(cols):
        for i in range(rows):
            if map[i][j] == None:
                map[i][j] = ['There is nothing here.', False]


generateMap(mapLocations)
