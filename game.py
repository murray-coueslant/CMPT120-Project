# a more complex text adventure game, with a randomly generated map and player control
# Written by: Murray Coueslant, Date: 2017/09/08

from pyfiglet import figlet_format
from termcolor import cprint
from random import shuffle, randint

# location definitions, these are the places the player can visit

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
        'island had to the outside world.')

# variable definitions, these are things which are used often like message strings etc... or things which would make
# code look ugly if used often in their normal form

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

# player class definition, the player class has a set of methods which apply to the character which the user is
# controlling


class Player:
    # initialising the variables which store the essential data for the player object
    def __init__(self, name, score, rowLocation, colLocation):
        self.name = name
        self.score = score
        self.rowLocation = rowLocation
        self.colLocation = colLocation

    # this method is used to change the location of the player within the world map, it takes a direction in the form
    # of a string and a map object and uses an if elif else statement to decide which direction to move the player in
    # once decided it modifies the current location of the player in the correct way for the desired direction

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

    # the getLocation method is what displays the current location of the character to the user. It has two different
    # messages depending on whether or not there is a special location at the player's current position
    def getLocation(self, map):
        if map.getLocation(self) == 'There is nothing here.':
            print(self.name, 'finds nothing, you should keep exploring.')
        else:
            print(self.name, 'is currently at', map.getLocation(self))

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

# map class definition, the map class contains the required variables and methods pertaining to the world map for the
# game. the methods encompass things such as filling the map with locations on startup etc...


class map:
    def __init__(self, rowSize, colSize, locations):
        self.rowSize = rowSize
        self.colSize = colSize
        self.locations = locations
        # defines a 2D array of a certain size which is defined when the class is instantiated
        self.map = [[None for col in range(colSize)] for row in range(rowSize)]
        numberOfLocations = len(self.locations)
        orderList = list(range(numberOfLocations))
        # the program uses the shuffle command from the random library to determine the positions of the six special
        # locations in the map
        shuffle(orderList)
        # this for loop places the six shuffled locations in six random positions on the map
        for i in orderList:
            randRow, randCol = self.randomRowCol()
            placed = False
            # while loop with a nested if statement which ensures each of the six locations is placed in a distinct
            # location and that two locations are not placed at the same coordinate
            while not placed:
                if self.map[randRow][randCol] is None:
                    self.map[randRow][randCol] = [self.locations[i], False]
                    placed = True
                else:
                    randRow, randCol = self.randomRowCol()
        self.fillEmpty()

    # the fillEmpty routine fills the remaining squares with a default location value and a boolean flag for use when
    # checking if the player should be given points for visiting a location
    def fillEmpty(self):
        for j in range(self.colSize):
            for i in range(self.rowSize):
                if self.map[i][j] is None:
                    self.map[i][j] = ['There is nothing here.', 'Flag']

    # counts all of the locations in the map which the player has already visited so far during the game
    def checkVisited(self):
        visitedCount = 0
        map = self.getMap()
        cols, rows = self.getSizes()
        for j in range(cols):
            for i in range(rows):
                if map[i][j][1] is True:
                    visitedCount += 1
        return visitedCount

    # this method is used to 'visit' a location on the map by changing its flag value and increasing the player's score
    # if it is a previously unvisited special location
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


# game class, the game class contains any of the methods which pertain to the general running of the game
class game:
    # method prints a collision message when the player attempts to move off of the edges of the map
    @staticmethod
    def collisionMessage(player):
        print('Collision, you cannot move this way. Choose another direction', player.name + '.')
        return

    # a versatile error display function which can be expanded with many possible errors using error codes, prints
    # predefined error messages
    @staticmethod
    def displayError(messageNo, player):
        if messageNo == 1:
            message = ('Incorrect direction command entered, please enter another,', player.name)
        else:
            message = 'Unknown error.'
        print(message)

    @staticmethod
    def displayHelp():
        print(helpMessage)

    # the getCommand method is the place where the user input is parsed and the correct action performed depending on
    # the command entered
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
            self.endGame()
        elif command.lower() == '' or None:
            print('Unrecognised command, enter another.')
            self.getCommand(player, input('Enter new command: '), map)
        else:
            print('Unrecognised command, enter another.')
            self.getCommand(player, input('Enter new command: '), map)

    # this method is the main game loop which is called at the start of the game and runs until the end of the process
    def gameLoop(self, player, gameMap):
        player.getLocation(gameMap)
        gameMap.visitLocation(player)
        player.displayScore()
        endFlag = False
        while 1:
            self.getCommand(player, input('What would you like to do?: '), gameMap)
            player.getLocation(gameMap)
            player.displayScore()
            count = gameMap.checkVisited()
            if count == gameMap.rowSize * gameMap.colSize:
                if endFlag is False:
                    decision = input('Would you like to keep exploring? (Y or N): ')
                    if decision.lower() == 'y':
                        endFlag = True
                        print('Enter a quit command to leave the game once you are done exploring!')
                    else:
                        self.endGame()

    @staticmethod
    def endGame():
        print(ending1)
        print(copyrightMessage)
        print(ending2)
        quit()


# class instantiations, defines the size of the map and the locations to place in it
game = game()
gameMap = map(3, 3, mapLocations)


# title display routine
def displayTitle():
    cprint(figlet_format('A Text Adventure!', font='big'), 'white', attrs=['bold'])


# starting routine
def startGame():
    displayTitle()
    input(introduction)
    character = Player(input('Enter the name of your character: '), 0, int(gameMap.rowSize / 2),
                       int(gameMap.colSize / 2))
    game.gameLoop(character, gameMap)


startGame()
