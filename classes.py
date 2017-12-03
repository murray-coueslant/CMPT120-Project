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
        self.movementCommands = ['go', 'move', 'travel']
        self.northCommands = ['n', 'north']
        self.eastCommands = ['e', 'east']
        self.southCommands = ['s', 'south']
        self.westCommands = ['w', 'west']
        self.helpCommands = ['h', 'help']
        self.mapCommands = ['m', 'map', 'world', 'show']
        self.scoreCommands = ['score', 'points', 'total']
        self.yesCommands = ['y', 'yes', 'yep', 'yeah', 'okay', 'please']
        self.noCommands = ['n', 'no', 'nope', 'nah']
        self.quitCommands = ['q', 'quit', 'exit', 'end', 'leave']
        self.lookCommands = ['look', 'view', 'explore']
        self.searchCommands = ['search', 'examine']
        self.inventoryCommands = ['inventory', 'bag', 'things', 'stuff', 'possessions']
        self.takeCommands = ['take', 'grab', 'pick', 'hold']
        self.specialCommands = ['climb', 'scale', 'enter', 'spelunk']

    def getCommand(self, inCommand, map):
        command = inCommand.split(' ')
        if command[0] in self.movementCommands:
            if len(command) == 2:
                if command[1] in self.northCommands:
                    self.movePlayer('n', map)
                elif command[1] in self.eastCommands:
                    self.movePlayer('e', map)
                elif command[1] in self.southCommands:
                    self.movePlayer('s', map)
                elif command[1] in self.westCommands:
                    self.movePlayer('w', map)
            else:
                print(command[0], 'must be paired with a direction. Enter a direction.')
        elif command[0] in self.northCommands:
            self.movePlayer('n', map)
        elif command[0] in self.eastCommands:
            self.movePlayer('e', map)
        elif command[0] in self.southCommands:
            self.movePlayer('s', map)
        elif command[0] in self.westCommands:
            self.movePlayer('w', map)
        elif command[0] in self.takeCommands:
            pass


    def getName(self):
        return self.name

    def movePlayer(self, direction, map):
        if direction == 'n':
            self.currentY -= 1
            if self.currentY < 0:
                print(self.name, 'you have reached the northern edge of the island. Try another move.')
                self.currentY += 1
        elif direction == 'e':
            self.currentX += 1
            if self.currentX > map.cols:
                print(self.name, 'you have reached the eastern edge of the island. Try another move.')
                self.currentX -= 1
        elif direction == 's':
            self.currentY +=1
            if self.currentY > map.rows:
                print(self.name, 'you have reached the southern edge of the island. Try another move.')
                self.currentY -= 1
        else:
            self.currentX -= 1
            if self.currentX < 0:
                print(self.name, 'you have reached the western edge of the island. Try another move.')
                self.currentX += 1

    def increaseMoves(self):
        self.moveCount += 1


class Locale:
    def __init__(self, longDescription, shortDescription, visited = False, searched = False, itemList = None):
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
        else:
            print('You already looked here!')
        
    def longDescription(self):
        return self.longDescription

class World:
    def __init__(self, locationList, cols, rows, itemList, player):
        self.locationList = locationList
        self.player = player
        self.itemList = itemList
        self.cols = cols
        self.rows = rows
        self.worldMap = [ [None for cols in range(self.cols)] for rows in range(self.rows) ]
        self.emptyLocale = Locale('an empty place.', 'nowhere')
        self.placeLocations()
        self.fillEmpty()
        self.placeItems(self.itemList)

    def placeLocations(self):
        randRow, randCol = self.randomRowCol()
        orderList = list(range(len(self.locationList)))
        shuffle(orderList)
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
        orderList = list(range(len(itemList)))
        shuffle(orderList)
        for i in orderList:
            print(i)
            print(itemList[i].name)
            row, col = self.randomRowCol()
            placed = False
            while not placed:
                location = self.worldMap[row][col]
                if location.itemList is None:
                    location.itemList = [itemList[i]]
                    placed = True
                else:
                    row, col = self.randomRowCol()
        
    def spawnPlayer(self):
        row, col = self.randomRowCol()
        self.player.currentX, self.player.currentY = col, row

    def checkVisited(self):
        return self.worldMap[self.player.currentY][self.player.currentX].visited

    def visit(self):
        self.worldMap[self.player.currentY][self.player.currentX].visit()

    def nonVisitedDescription(self):
        try:
            return self.worldMap[self.player.currentY][self.player.currentX].longDescription
        except IndexError:
            return self.worldMap[self.player.currentY][self.player.currentX].longDescription
    
    def visitedDescription(self):
        return self.worldMap[self.player.currentY][self.player.currentX].shortDescription

    def randomRowCol(self):
        randRow, randCol = randint(0, (self.rows - 1)), randint(0, (self.cols - 1))
        return randRow, randCol

    # prints a single row of the game map, along with the correct separators for the map layout
    def printRow(self, row):
        output = '|'
        for val in row:
            output += str(val) + '|'
        print(output)

    # this method is used to print a line separator for the map, similar to above it prints a single row in the output
    def printSeparator(self, length, row):
        output = '+'
        dashLength = '-' * length
        for val in row:
            output += dashLength + '+'
        print(output)

    # the main map display method, it fetches the maximum length of an item in the shortened locations list as well as
    # fetching that list itself. it then uses these things to print the entire map using other functions
    def displayMap(self):
        spacedLocations, maxLen = self.getSpacedLocations(self.worldMap)
        self.printSeparator(maxLen, spacedLocations[0])
        for row in spacedLocations:
            self.printRow(row)
            self.printSeparator(maxLen, row)
    
    # this method returns to us a list of the shortened location names, with the appropriate amount of whitespace append
    # -ed such that all of the locations have the same length. this is required for the display of the map in the game.
    def getSpacedLocations(self, map):
        shortList = []
        spacedLocations = [[None for cols in range(
            self.cols)] for rows in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                shortList.append(self.worldMap[i][j].shortDescription)

        maxLen = self.getMaxLen(shortList)
        for i in range(self.rows):
            for j in range(self.cols):
                if len(self.worldMap[i][j].shortDescription) == maxLen:
                    whitespace = ''
                else:
                    whitespace = (maxLen - len(self.worldMap[i][j].shortDescription)) * ' '
                spacedLocations[i][j] = str(self.worldMap[i][j].shortDescription) + str(whitespace)
        return spacedLocations, maxLen

        # this method uses a findMax algorithm to get the longest element in the shortLocations list in this case. this max
    # value is used to append the appropriate amount of whitespace to the rest of the location elements
    def getMaxLen(self, list):
        maxLen = 0
        for i in range(0, len(list)):
            currLen = len(list[i])
            if currLen > maxLen:
                maxLen = currLen
        return maxLen


