# an experiment which will generate random 3*3 maps with six explorable locations
# Murray Coueslant, 2017/09/18

# variable and array definitions
rows = 3
cols = 3
gameMap = [[0 for i in range(cols)] for j in range(rows)]
mapLocations = ['a','b','c','d','e','f']

# map generator


def generateMap(locationList):
    unusedLocations = locationList
    numberOfLocations = len(unusedLocations)
    usedLocations = [0] * numberOfLocations
    countPlaces(unusedLocations)

def countPlaces(locationList):
    usedCount = 0
    unusedCount = 0
    for i in range(len(locationList)):
        if locationList[i] == 'X':
            usedCount += 1
        else:
            unusedCount += 1


generateMap(mapLocations)