# a
# Written by: Murray Coueslant, Date: 2017/09/08

from pyfiglet import figlet_format
from termcolor import cprint
from random import shuffle, randint

# location definitions

loc1 = 'in a dark room, around you you can feel some sticks. In your pocket you feel a lighter. You bundle some  ' \
       'of the sticks with your shirt to create a makeshift torch. You light the torch, revealing a wooden ' \
       'door to the left of you.'

loc2 = 'in an open clearing. Behind you is the hut you just left. It is twilight so you decide to keep your ' \
       'torch lit. How did you end up here? What were you doing in the hut before you fell unconscious? Ahead of ' \
       'you you spot some broken brush, you follow the tracks.'

loc3 = 'surrounded by trees. On the path in front of you lay strange markings, they seem to lead somewhere so you ' \
       'follow them. Eventually you realise that they are your own footsteps. It is clear that you were running. ' \
       'What could you have been running from?'

loc4 = 'at the end of the tracks, what you find makes you step back a few paces. At your feet lies a glowing green ' \
       'object. What is it? How did it get here? Suddenly, the glowing becomes more and more intense until you can ' \
       'barely see anymore. Above you, you hear a loud droning noise as a shadow descends over the clearing. You turn' \
       'on your heels and run as fast as your legs can muster.'

loc5 = 'being chased by the shadow. You keep running until you begin to find some signs of civilisation, then the ' \
       'shadow stops chasing you. You continue to travel on until you manage to flag down a car to bring you to the ' \
       'next town over. You will never return to those woods.'

loc6 = ''

# variable definitions

introduction = ('Welcome to a text adventure game. You are a lonely wanderer who has woken up in a strange place, '
                'this is the story of your most recent intrepid adventure. Press enter to begin.')
copyrightMessage = ('This game is property of Murray Coueslant. Any enquiries can be sent to '
                    'murray.coueslant1@marist.edu. Fair use is permitted.' + '\n')
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
                self.visitLocation(map)
        elif direction.lower() == 'south':
            self.rowLocation += 1
            if self.rowLocation > (map.rowSize -1):
                game.collisionMessage(self)
                self.rowLocation -= 1
            else:
                self.visitLocation(map)
        elif direction.lower() == 'east':
            self.colLocation += 1
            if self.colLocation > (map.colSize - 1):
                game.collisionMessage(self)
                self.colLocation -= 1
            else:
                self.visitLocation(map)
        elif direction.lower() == 'west':
            self.colLocation -= 1
            if self.colLocation < 0:
                game.collisionMessage(self)
                self.colLocation += 1
            else:
                self.visitLocation(map)
        else:
            game.displayError(1, self)

    def visitLocation(self, map):
        if map.getVisited(self) == 'Flag':
            map.setVisited(self)
        elif map.getVisited(self) is False:
            self.increaseScore()
            map.setVisited(self)
        elif map.getVisited(self) is True:
            print('You have already discovered this location!')

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
            self.getCommand(player, input('Enter new command: '))
        else:
            print('Unrecognised command, enter another.')
            self.getCommand(player, input('Enter new command: '))

    def gameLoop(self, player, gameMap):
        player.getLocation(gameMap)
        player.visitLocation(gameMap)
        player.displayScore()
        while 1:
            self.getCommand(player, input('What would you like to do?: '), gameMap)
            player.getLocation(gameMap)
            player.displayScore()
            count = gameMap.checkVisited()
            if count == gameMap.rowSize * gameMap.colSize:
                self.endGame()

    def endGame(self):
        print('\n' + 'Congratulations, you have explored the whole island!' + '\n')
        print(copyrightMessage)
        print('I hope you enjoyed playing this game. See you soon!' + '\n')
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
    cprint(figlet_format('A Text Adventure!', font='big'),
           'white', attrs=['bold'])


startGame()
