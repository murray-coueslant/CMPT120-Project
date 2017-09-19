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
                collisionMessage()
                self.rowLocation += 1
        elif direction.lower() == 'south':
            self.rowLocation += 1
            if self.rowLocation > 2:
                collisionMessage()
                self.rowLocation -= 1
        elif direction.lower() == 'east':
            self.colLocation += 1
            if self.colLocation > 2:
                collisionMessage()
                self.colLocation -= 1
        elif direction.lower() == 'west':
            self.colLocation -= 1
            if self.colLocation < 0:
                collisionMessage()
                self.colLocation += 1
        else:
            displayError(1)

    def getLocation(self):
        print(self.name, 'is currently at:', gameMap[self.rowLocation][self.colLocation][0])


# variable and array definitions
rows = 3
cols = 3
gameMap = [[None for i in range(cols)] for j in range(rows)]
mapLocations = ['a', 'b', 'c', 'd', 'e', 'f']
northCommands = ['north', 'go north', 'move north', 'travel north']
eastCommands = ['east', 'go east', 'move east', 'travel east']
southCommands = ['south', 'go south', 'move south', 'travel south']
westCommands = ['west', 'go west', 'move west', 'travel west']
helpCommands = ['help', 'help me', 'get help']

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


def collisionMessage():
    print('Collision, you cannot move this way.')
    return


def displayError(messageNo):
    if messageNo == 1:
        message = 'Incorrect direction command entered, please enter another.'
    else:
        message = 'Unknown error.'
    print(message)


def displayHelp():
    print('Help message')


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
    elif command.lower() == "" or None:
        print('Unrecognised command, enter another.')
        getCommand(character, input("Enter new command: "))
    else:
        print('Unrecognised command, enter another.')
        getCommand(character, input("Enter new command: "))

generateMap(mapLocations)
character = Player('Murray', 0, 1, 1)
character.getLocation()

while 1:
    getCommand(character, input('What would you like to do?: '))
    character.getLocation()

