# a
# Written by: Murray Coueslant, Date: 2017/09/08

from pyfiglet import figlet_format
from termcolor import cprint
from random import shuffle, randint

# location definitions

loc1 = ('a sandy beach, the waves lap onto the shore steadily. You look to the horizon and see nothing but the blue '
        'expanse of the ocean. You contemplate how you got here, and how you are going to get home.')

loc2 = ('a dense rainforest. The sound of creatures in the bush is overwhelming, the smell is tropical. '
        'You are afraid, a predator could appear at any time. You think about what would happen if you did '
        'not return home.')

loc3 = ('an open clearing. On the ground infront of you there is a pile of strange stones. You are not sure what '
        'they are for. You wonder if there were once people here, and if so, where are they now?')

loc4 = ('a roaring waterfall. The white wash rolls from the top of the collosal stones, plunging into a pool of dark '
        'water. You wonder if there is anything down there, or maybe there is a secret passage behind the falls. '
        'You attempt to find the passage, but your luck comes up dry.')

loc5 = ('a strange cave front. There are remnants of exploration here, makeshift torches and tools. You decide that '
        'it is likely not sensible to go into the cave without proper protection. You guess that people have before '
        'you; and it has not ended well.')

loc6 = ('a decrepit marine dock. The wood of the jetty is rotting away, there is a rusting hull of a small sailboat '
        'which is somehow still tied to the jetty. You wonder whether this was once the only connection this '
        'islan had to the outside world.')

# variable definitions

introduction = ('Welcome to a text adventure game. You are a lonely wanderer who has woken up on an island, '
                'it is your task to explore your surroundings. Press enter to begin.')
ending1 = ('\n' + 'Congratulations, you have explored the whole island!' + '\n')
ending2 = ('I hope you enjoyed playing this game. See you soon!' + '\n')
copyrightMessage = ('This game is property of Murray Coueslant. Any enquiries can be sent to '
                    'murray.coueslant1@marist.edu. Fair use is permitted.' + '\n')
helpMessage = ('Help:', '\n', 'Enter a command below, the possible commands are:', '\n', 'north, south, east, west'
               '\n', 'go, move or travel + a direction', '\n', 'quit, exit, leave, end', '\n'
               'or this help command, but you figured that one out, go you!')
mapLocations = [loc1, loc2, loc3, loc4, loc5, loc6]
northCommands = ['n', 'north', 'go north', 'move north', 'travel north']
eastCommands = ['e', 'east', 'go east', 'move east', 'travel east']
southCommands = ['s', 'south', 'go south', 'move south', 'travel south']
westCommands = ['w', 'west', 'go west', 'move west', 'travel west']
helpCommands = ['h', 'help', 'help me', 'get help']
quitCommands = ['q', 'quit', 'exit', 'end', 'leave']

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
                map.visitLocation(self)
        elif direction.lower() == 'south':
            self.rowLocation += 1
            if self.rowLocation > (map.rowSize -1):
                game.collisionMessage(self)
                self.rowLocation -= 1
            else:
                map.visitLocation(self)
        elif direction.lower() == 'east':
            self.colLocation += 1
            if self.colLocation > (map.colSize - 1):
                game.collisionMessage(self)
                self.colLocation -= 1
            else:
                map.visitLocation(self)
        elif direction.lower() == 'west':
            self.colLocation -= 1
            if self.colLocation < 0:
                game.collisionMessage(self)
                self.colLocation += 1
            else:
                map.visitLocation(self)
        else:
            game.displayError(1, self)

    def getName(self):
        return self.name

    def getLocation(self, map):
        print(self.name, 'is currently at:', map.getLocation(self))

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


class map:
    def __init__(self, rowSize, colSize, locations):
        self.rowSize = rowSize
        self.colSize = colSize
        self.locations = locations
        self.map = [[None for col in range(colSize)] for row in range(rowSize)]
        numberOfLocations = len(self.locations)
        orderList = list(range(numberOfLocations))
        shuffle(orderList)
        for i in orderList:
            randRow, randCol = self.randomRowCol()
            placed = False
            while not placed:
                if self.map[randRow][randCol] is None:
                    self.map[randRow][randCol] = [self.locations[i], False]
                    placed = True
                else:
                    randRow, randCol = self.randomRowCol()
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

    def visitLocation(self, player):
        if self.getVisited(player) == 'Flag':
            self.setVisited(player)
        elif self.getVisited(player) is False:
            player.increaseScore()
            self.setVisited(player)
        elif self.getVisited(player) is True:
            print('You have already discovered this location!')

    def randomRowCol(self):
        randRow, randCol = randint(0, (self.rowSize - 1)), randint(0, (self.colSize - 1))
        return randRow, randCol

    def getSizes(self):
        return self.colSize, self.rowSize

    def getLocation(self, player):
        return self.map[player.rowLocation][player.colLocation][0]

    def getVisited(self, player):
        return self.map[player.rowLocation][player.colLocation][1]

    def setVisited(self, player):
        self.map[player.rowLocation][player.colLocation][1] = True

    def getMap(self):
        return self.map


# game class
class game:
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
        print(helpMessage)

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
            self.getCommand(player, input('Enter new command: '), map)
        else:
            print('Unrecognised command, enter another.')
            self.getCommand(player, input('Enter new command: '), map)

    def gameLoop(self, player, gameMap):
        player.getLocation(gameMap)
        gameMap.visitLocation(player)
        player.displayScore()
        while 1:
            self.getCommand(player, input('What would you like to do?: '), gameMap)
            player.getLocation(gameMap)
            player.displayScore()
            count = gameMap.checkVisited()
            if count == gameMap.rowSize * gameMap.colSize:
                self.endGame()

    def endGame(self):
        print(ending1)
        print(copyrightMessage)
        print(ending2)
        quit()


# class instantiations
game = game()
gameMap = map(3, 3, mapLocations)

# starting routine


def startGame():
    displayTitle()
    input(introduction)
    character = Player(input('Enter the name of your character: '), 0, int(gameMap.rowSize / 2),
                       int(gameMap.colSize / 2))
    game.gameLoop(character, gameMap)


# title display routine
def displayTitle():
    cprint(figlet_format('A Text Adventure!', font='big'), 'white', attrs=['bold'])


startGame()
