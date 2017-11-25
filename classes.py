from random import randint, shuffle
class Item:
    def __init__(self, name, ID, used = False):
        self.name = str(name)
        self.used = used
        self.ID = int(ID)

class Player:
    def __init__(self, name, score = 0, currentX = 0, currentY = 0, moveCount = 0, inventory = []):
        self.name = str(name)
        self.score = score
        self.currentX = currentX
        self.currentY = currentY
        self.moveCount = moveCount
        self.inventory = inventory

    def getName(self):
        return self.name

    def movePlayer(self, direction):
        pass

    def increaseMoves(self):
        self.moveCount += 1


class Locale:
    def __init__(self, longDescription, shortDescription, visited = False, searched = False, itemList = []):
        self.longDescription = longDescription
        self.shortDescription = shortDescription
        self.visited = visited
        self.searched = searched
        self.itemList = itemList
    
    def visit(self):
        self.visited = True

    def search(self):
        if self.searched == False:
            self.searched = True
            if len(itemList) > 0:
                print('You have found: \n')
                for i in range(0, len(itemList)):
                    print('\t' + str(itemList[i]))
        
    def longDescription(self):
        return self.longDescription

class World:
    def __init__(self, locationList, cols, rows, player = None, itemList = []):
        self.locationList = locationList
        self.player = player
        self.itemList = itemList
        self.cols = cols
        self.rows = rows
        self.worldMap = [ [None for cols in range(self.cols)] for rows in range(self.rows) ]
        self.emptyLocale = Locale('an empty place.', 'nowhere')
        self.placeLocations()
        self.fillEmpty()
        self.placeItems(itemList)

    def placeLocations(self):
        randRow, randCol = self.randomRowCol()
        orderList = list(range(len(self.locationList)))
        itemList = list(range(len(self.itemList)))
        shuffle(orderList)
        shuffle(itemList)

        for i in orderList:
            placed = False
            while not placed:
                if self.worldMap[randRow][randCol] == None:
                    self.worldMap[randRow][randCol] = self.locationList[i]
                    placed = True
                else:
                    randRow, randCol = self.randomRowCol()
    
    def fillEmpty(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.worldMap[i][j] == None:
                    self.setEmpty(i, j)

    def setEmpty(self, rowLocation, colLocation):
        self.worldMap[rowLocation][colLocation] = self.emptyLocale

    def placeItems(self, itemList):
        orderList = list(range(0, len(itemList)))
        shuffle(orderList)
        counter = 0
        for i in range(self.rows):
            for j in range(self.cols):
                rand = randint(0, 10)
                if len(itemList) > 0:
                    if rand >= 5:
                        self.worldMap[i][j].itemList.append(itemList[orderList[counter]])
                        counter += 1
                print(self.itemList)


    def randomRowCol(self):
        randRow, randCol = randint(
            0, (self.rows - 1)), randint(0, (self.cols - 1))
        return randRow, randCol


