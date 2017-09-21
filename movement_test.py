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

    def movePlayer(self, direction, map):
        if direction.lower() == 'north':
            self.rowLocation -= 1
            if self.rowLocation < 0:
                game.collisionMessage(self)
                self.rowLocation += 1
            else:
                self.visitLocation()
        elif direction.lower() == 'south':
            self.rowLocation += 1
            if self.rowLocation > (map.rowSize -1):
                game.collisionMessage(self)
                self.rowLocation -= 1
            else:
                self.visitLocation()
        elif direction.lower() == 'east':
            self.colLocation += 1
            if self.colLocation > (map.colSize - 1):
                game.collisionMessage(self)
                self.colLocation -= 1
            else:
                self.visitLocation()
        elif direction.lower() == 'west':
            self.colLocation -= 1
            if self.colLocation < 0:
                game.collisionMessage(self)
                self.colLocation += 1
            else:
                self.visitLocation()
        else:
            game.displayError(1, self)

    def visitLocation(self):
        if map.getVisited(self.rowLocation, self.colLocation) == 'Flag':
            map.setVisited(self.rowLocation, self.colLocation)
        elif map.getVisited(self.rowLocation, self.colLocation) is False:
            self.increaseScore()
            map.setVisited(self.rowLocation, self.colLocation)
        elif map.getVisited(self.rowLocation, self.colLocation) is True:
            print('You have already discovered this location!')

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
        print(self.getName()+',', 'your score is:', self.getScore())

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
            randRow = randint(0, (self.rowSize-1))
            randCol = randint(0, (self.colSize-1))
            print(randRow, randCol)
            placed = False
            while not placed:
                if self.map[randRow][randCol] is None:
                    self.map[randRow][randCol] = [self.locations[i], False]
                    placed = True
                else:
                    randRow = randint(0, rowSize)
                    randCol = randint(0, colSize)
        self.fillEmpty()

    def fillEmpty(self):
        for j in range(self.colSize):
            for i in range(self.rowSize):
                if self.map[i][j] is None:
                    self.map[i][j] = ['There is nothing here.', 'Flag']

    def checkVisited(self):
        visitedCount = 0
        map = self.getMap()
        cols, rows = self.getSizes()
        for j in range(cols):
            for i in range(rows):
                if map[i][j][1] is True:
                    visitedCount += 1
        return visitedCount

    def getSizes(self):
        return self.colSize, self.rowSize

    def getLocation(self, rowPos, colPos):
        return self.map[rowPos][colPos][0]

    def getVisited(self, rowPos, colPos):
        return self.map[rowPos][colPos][1]

    def setVisited(self, rowPos, colPos):
        self.map[rowPos][colPos][1] = True

    def getMap(self):
        return self.map


# game class
class game():
    def collisionMessage(self, player):
        print('Collision, you cannot move this way. Choose another direction', player.name + '.')
        return

    def displayError(self, messageNo, player):
        if messageNo == 1:
            message = ('Incorrect direction command entered, please enter another,', player.name)
        else:
            message = 'Unknown error.'
        print(message)

    def displayHelp(self):
        print('Help:', '\n', 'Enter a command below, the possible commands are:', '\n', 'north, south, east, west'
              '\n', 'go, move or travel + a direction', '\n', 'quit, exit, leave, end', '\n'
              'or this help command, but you figured that one out, go you!')

    def getCommand(self, player, command, map):
        if command.lower() in northCommands:
            player.movePlayer('north', map)
        elif command.lower() in eastCommands:
            player.movePlayer('east', map)
        elif command.lower() in southCommands:
            player.movePlayer('south', map)
        elif command.lower() in westCommands:
            player.movePlayer('west', map)
        elif command.lower() in helpCommands:
            self.displayHelp()
        elif command.lower() in quitCommands:
            input('Thanks for playing, press enter to end the game.')
            quit()
        elif command.lower() == '' or None:
            print('Unrecognised command, enter another.')
            self.getCommand(character, input('Enter new command: '))
        else:
            print('Unrecognised command, enter another.')
            self.getCommand(character, input('Enter new command: '))

    def endGame(self):
        print('\n' + 'Congratulations, you have explored the whole island!' + '\n')
        print(copyrightMessage)
        print('I hope you enjoyed playing this game. See you soon!' + '\n')
        quit()


# variable and array definitions
copyrightMessage = ('This game is property of Murray Coueslant. Any enquiries can be sent to \
                     murray.coueslant1@marist.edu. Fair use is permitted.' + '\n')
mapLocations = ['a', 'b', 'c', 'd', 'e', 'f']
northCommands = ['n', 'north', 'go north', 'move north', 'travel north']
eastCommands = ['e', 'east', 'go east', 'move east', 'travel east']
southCommands = ['s', 'south', 'go south', 'move south', 'travel south']
westCommands = ['w', 'west', 'go west', 'move west', 'travel west']
helpCommands = ['h', 'help', 'help me', 'get help']
quitCommands = ['q', 'quit', 'exit', 'end', 'leave']

game = game()
gameMap = map(3, 3, mapLocations)

character = Player(input('Enter the name of your character: '), 0, int(gameMap.rowSize/2), int(gameMap.colSize/2))
character.getLocation(gameMap)
character.visitLocation()
character.displayScore()
while 1:
    game.getCommand(character, input('What would you like to do?: '), gameMap)
    character.getLocation(gameMap)
    character.displayScore()
    count = gameMap.checkVisited()
    if count == gameMap.rowSize * gameMap.colSize:
        game.endGame()
