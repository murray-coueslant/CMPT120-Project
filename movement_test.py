# implementing movement between the locations, implementing the player class in order to keep track of the current
# position

# module imports
from random import shuffle, randint


# player class definition

class Player:
    def __init__(self, name, score, rowLocation, colLocation):
        self.name = name
        self.score = score
        self.rowLocation = rowLocation
        self.colLocation = colLocation

    def movePlayer(self, direction):
        if direction.lower() == 'north':
            self.rowLocation -= 1
            if self.rowLocation < 0:
                collisionMessage(self)
                self.rowLocation += 1
            else:
                visitLocation(self.rowLocation, self.colLocation, self)
        elif direction.lower() == 'south':
            self.rowLocation += 1
            if self.rowLocation > 2:
                collisionMessage(self)
                self.rowLocation -= 1
            else:
                visitLocation(self.rowLocation, self.colLocation, self)
        elif direction.lower() == 'east':
            self.colLocation += 1
            if self.colLocation > 2:
                collisionMessage(self)
                self.colLocation -= 1
            else:
                visitLocation(self.rowLocation, self.colLocation, self)
        elif direction.lower() == 'west':
            self.colLocation -= 1
            if self.colLocation < 0:
                collisionMessage(self)
                self.colLocation += 1
            else:
                visitLocation(self.rowLocation, self.colLocation, self)
        else:
            displayError(1, self)

    def getName(self):
        return self.name

    def getLocation(self, map):
        print(self.name, 'is currently at:', map.getLocation(self.colLocation, self.rowLocation))

    def getXPos(self):
        return self.colLocation

    def getYPos(self):
        return self.rowLocation

    def getScore(self):
        return self.score

    def increaseScore(self):
        self.score += 5

    def displayScore(self):
        print(self.getName(), 'your score is:', self.getScore())

# map class definition

class map():
    def __init__(self, rowSize, colSize, locations):
        self.rowSize = rowSize
        self.colSize = colSize
        self.locations = locations
        self.map = [[None for col in range(colSize)] for row in range(rowSize)]
        numberOfLocations = len(self.locations)
        orderList = list(range(numberOfLocations))
        shuffle(orderList)
        for i in orderList:
            randRow = randint(0, 2)
            randCol = randint(0, 2)
            placed = False
            while not placed:
                if self.map[randRow][randCol] is None:
                    self.map[randRow][randCol] = [self.locations[i], False]
                    placed = True
                else:
                    randRow = randint(0, 2)
                    randCol = randint(0, 2)
        self.fillEmpty()


    def fillEmpty(self):
        for j in range(cols):
            for i in range(rows):
                if self.map[i][j] == None:
                    self.map[i][j] = ['There is nothing here.', False]

    def getLocation(self, rowPos, colPos):
        return self.map[rowPos][colPos][0]

    def getVisited(self, rowPos, colPos):
        return self.map[rowPos][colPos][1]

    def setVisited(self, rowPos, colPos):
        self.map[rowPos][colPos][1] = True

    def getMap(self):
        return self.map

# variable and array definitions
rows = 3
cols = 3
gameMap = [[None for i in range(cols)] for j in range(rows)]
mapLocations = ['a', 'b', 'c', 'd', 'e', 'f']
northCommands = ['n', 'north', 'go north', 'move north', 'travel north']
eastCommands = ['e', 'east', 'go east', 'move east', 'travel east']
southCommands = ['s', 'south', 'go south', 'move south', 'travel south']
westCommands = ['w', 'west', 'go west', 'move west', 'travel west']
helpCommands = ['h', 'help', 'help me', 'get help']
quitCommands = ['q', 'quit', 'exit', 'end', 'leave']


# general game modules

def collisionMessage(player):
    print('Collision, you cannot move this way. Choose another direction', player.name + '.')
    return


def displayError(messageNo, player):
    if messageNo == 1:
        message = ('Incorrect direction command entered, please enter another,', player.name)
    else:
        message = 'Unknown error.'
    print(message)


def displayHelp():
    print('Help:', '\n', 'Enter a command in the prompt, the possible commands are:', '\n', 'north, south, east, west'
          '\n', 'go, move or travel + a direction', '\n', 'quit, exit, leave, end', '\n'
          'or this help command, but you figured that one out, go you!')


def getCommand(player, command):
    if command.lower() in northCommands:
        player.movePlayer('north')
    elif command.lower() in eastCommands:
        player.movePlayer('east')
    elif command.lower() in southCommands:
        player.movePlayer('south')
    elif command.lower() in westCommands:
        player.movePlayer('west')
    elif command.lower() in helpCommands:
        displayHelp()
    elif command.lower() in quitCommands:
        input('Thanks for playing, press enter to end the game.')
        quit()
    elif command.lower() == "" or None:
        print('Unrecognised command, enter another.')
        getCommand(character, input("Enter new command: "))
    else:
        print('Unrecognised command, enter another.')
        getCommand(character, input("Enter new command: "))


def visitLocation(locationRow, locationCol, player):
    if gameMap.getVisited(locationRow, locationCol) is False:
        player.increaseScore()
        gameMap.setVisited(locationRow, locationCol)
    elif gameMap.getVisited(locationRow, locationCol) is True:
        print('You have already discovered this location!')
def checkVisited(map):
    visitedCount = 0
    for j in range(cols):
        for i in range(rows):
            if map[i][j] == True:
                visitedCount += 1
    return visitedCount

def endGame():
    print('\n' + 'Congratulations, you have made it home safely. You rest for a few days and then return to normal '
          'life.' + '\n')
    displayCopyright()
    print('I hope you enjoyed playing this game. See you soon!' + '\n')

gameMap = map(3, 3, mapLocations)
character = Player('Murray', 0, 1, 1)
character.getLocation(gameMap)
visitLocation(1, 1, character)
character.displayScore()
while 1:
    getCommand(character, input('What would you like to do?: '))
    character.getLocation(gameMap)
    character.displayScore()
    count = checkVisited(gameMap.getMap())
    print(count)
    if count == 9:
        endGame()
