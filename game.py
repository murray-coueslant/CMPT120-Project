# a more complex text adventure game, with a randomly generated map and player control
# Written by: Murray Coueslant, Date: 2017/09/08

from pyfiglet import figlet_format
from termcolor import cprint
from random import shuffle, randint

# location definitions, these are the places the player can visit

loc1 = ('a sandy beach, the waves lap onto the shore steadily. You look to the horizon and see nothing but the blue '
        'expanse of the ocean. You contemplate how you got here, and how you are going to get home.')

loc1Short = 'Sandy Beach'

loc2 = ('a dense rainforest. The sound of creatures in the bush is overwhelming, the smell is tropical. '
        'You are afraid, a predator could appear at any time. You think about what would happen if you did '
        'not return home.')

loc2Short = 'Dense Rainforest'

loc3 = ('an open clearing. On the ground in front of you there is a pile of strange stones. You are not sure what '
        'they are for. You wonder if there were once people here, and if so, where are they now?')

loc3Short = 'Open Clearing'

loc4 = ('a roaring waterfall. The white wash rolls from the top of the collosal stones, plunging into a pool of dark '
        'water. You wonder if there is anything down there, or maybe there is a secret passage behind the falls. '
        'You attempt to find the passage, but your luck comes up dry.')

loc4Short = 'Roaring Waterfall'

loc5 = ('a strange cave front. There are remnants of exploration here, makeshift torches and tools. You decide that '
        'it is likely not sensible to go into the cave without proper protection. You guess that people have before '
        'you; and it has not ended well.')

loc5Short = 'Strange Cave Front'

loc6 = ('a decrepit marine dock. The wood of the jetty is rotting away, there is a rusting hull of a small sailboat '
        'which is somehow still tied to the jetty. You wonder whether this was once the only connection this '
        'island had to the outside world.')

loc6Short = 'Decrepit Marine Dock'

loc7 = ('an abandoned hut. The side of the hut has strange images painted on it in red paint, and there are no windows'
        'on any side. The door sits ajar, you pry it open to reveal some more bizarre paintings on the wall as well as'
        'hundreds of papers on the floor. You decide not to enter any farther into the structure for fear of crazies.')

loc7Short = 'Abandoned Hut'

loc8 = ('a little creek. The water rushes by and you see some small fish glimmering in the sunlight. You dip your hands'
        'into the water and take a drink. The water is cold and fresh, you fill your vessel from the creek and carry'
        'on ahead.')

loc8Short = 'Little Creek'

loc9 = ('a fallen tree. The collosal trunk is hollow after all of the time spent laying on the ground. There are '
        'clearly animals who call this trunk their home. You decide to move on, you\'d rather not meet any of them.')

loc9Short = 'Fallen Tree'

# variable definitions, these are things which are used often like message strings etc... or things which would make
# code look ugly if used often in their normal form

introduction = ('Welcome to a text adventure game. You are a lonely wanderer who has woken up on an island, '
                'it is your task to explore your surroundings. Press enter to begin.')
ending1 = '\nCongratulations, you have explored the whole island!\n'
ending2 = '\nUnfortunately, you have run out of moves!\n'
ending3 = 'I hope you enjoyed playing this game. See you soon!\n'
copyrightMessage = ('This game is property of Murray Coueslant. Any enquiries can be sent to '
                    'murray.coueslant1@marist.edu. Fair use is permitted.\n')
helpMessage = ('Help:\nEnter a command below, the possible commands are:\n\tnorth, south, '
               'east, west\n\tgo, move or travel + a direction\n\tquit, exit, leave, end\n\tmap, world, view world\n\t'
               'points, score or total\nor this help command, but you figured that one out, go you!')

# location set definition
mapLocations = [loc1, loc2, loc3, loc4, loc5, loc6, loc7, loc8, loc9]
shortLocations = [loc1Short, loc2Short, loc3Short, loc4Short, loc5Short, loc6Short, loc7Short, loc8Short, loc9Short]

# command set definitions
northCommands = ['n', 'north', 'go north', 'move north', 'travel north']
eastCommands = ['e', 'east', 'go east', 'move east', 'travel east']
southCommands = ['s', 'south', 'go south', 'move south', 'travel south']
westCommands = ['w', 'west', 'go west', 'move west', 'travel west']
helpCommands = ['h', 'help', 'help me', 'get help']
mapCommands = ['m', 'map', 'world', 'show map', 'view world']
scoreCommands = ['score', 'points', 'total']
yesCommands = ['y', 'yes', 'yep', 'yeah', 'okay', 'please']
noCommands = ['n', 'no', 'nope', 'nah', 'no thanks']
quitCommands = ['q', 'quit', 'exit', 'end', 'leave']

# player class definition, the player class has a set of methods which apply to the character which the user is
# controlling


class Player:
    # initialising the variables which store the essential data for the player object
    def __init__(self, name, rowLocation, colLocation, map, score=0):
        self.name = name
        self.score = score
        self.rowLocation = rowLocation
        self.colLocation = colLocation
        self.moves = 0
        self.maxMoves = map.rowSize * map.colSize

    # this method is used to change the location of the player within the world map, it takes a direction in the form
    # of a string and a map object and uses an if elif else statement to decide which direction to move the player in
    # once decided it modifies the current location of the player in the correct way for the desired direction

    def movePlayer(self, direction, map):
        if direction.lower() == 'north':
            self.rowLocation -= 1
            if self.rowLocation < 0:
                game.displayError(2, self)
                self.rowLocation += 1
            else:
                map.visitLocation(self)
                self.increaseMoves()
        elif direction.lower() == 'south':
            self.rowLocation += 1
            if self.rowLocation > (map.rowSize - 1):
                game.displayError(2, self)
                self.rowLocation -= 1
            else:
                map.visitLocation(self)
                self.increaseMoves()
        elif direction.lower() == 'east':
            self.colLocation += 1
            if self.colLocation > (map.colSize - 1):
                game.displayError(2, self)
                self.colLocation -= 1
            else:
                map.visitLocation(self)
                self.increaseMoves()
        elif direction.lower() == 'west':
            self.colLocation -= 1
            if self.colLocation < 0:
                game.displayError(2, self)
                self.colLocation += 1
            else:
                map.visitLocation(self)
                self.increaseMoves()
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

    # this method checks to see if the player has used up all of their available moves for the current game
    def checkMoves(self):
        if self.moves >= self.maxMoves:
            print('You have run out of moves, try again!')
            game.endGame(2)
        else:
            print('You have', self.maxMoves-self.moves, 'moves remaining, use them wisely!')

    def getXPos(self):
        return self.colLocation

    def getYPos(self):
        return self.rowLocation

    def getScore(self):
        return self.score

    def increaseScore(self):
        self.score += 5

    def increaseMoves(self):
        self.moves += 1

    def displayScore(self):
        print(self.getName()+',', 'your score is:', self.getScore())

# map class definition, the map class contains the required variables and methods pertaining to the world map for the
# game. the methods encompass things such as filling the map with locations on startup etc...


class map:
    def __init__(self, rowSize, colSize, locations, shortLocations):
        self.rowSize = rowSize
        self.colSize = colSize
        self.locations = locations
        self.shortLocations = shortLocations
        # defines a 2D array of a certain size which is defined when the class is instantiated
        self.map = [[None for cols in range(colSize)] for rows in range(rowSize)]
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
                    self.map[randRow][randCol] = [self.locations[i], self.shortLocations[i], False]
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
                    self.map[i][j] = ['There is nothing here.', 'X X X', 'Flag']

    # counts all of the locations in the map which the player has already visited so far during the game
    def checkVisited(self):
        visitedCount = 0
        map = self.getMap()
        cols, rows = self.getSizes()
        for j in range(cols):
            for i in range(rows):
                if map[i][j][2] is True:
                    visitedCount += 1
        return visitedCount

    # this method is used to 'visit' a location on the map by changing its flag value and increasing the player's score
    # if it is a previously unvisited special location
    def visitLocation(self, player):
        if self.getVisited(player) == 'Flag':
            self.setVisited(player)
        elif self.getVisited(player) is False:
            player.increaseScore()
            player.displayScore()
            self.setVisited(player)
        elif self.getVisited(player) is True:
            print('You have already discovered this location!')

    # this method returns to us a list of the shortened location names, with the appropriate amount of whitespace append
    # -ed such that all of the locations have the same length. this is required for the display of the map in the game.
    def getSpacedLocations(self, map):
        spacedLocations = [[None for cols in range(self.colSize)] for rows in range(self.rowSize)]
        maxLen = self.getMaxLen(self.shortLocations)
        for i in range(self.rowSize):
            for j in range(self.colSize):
                if len(map[i][j][1]) == maxLen:
                    whitespace = ''
                else:
                    whitespace = (maxLen - len(map[i][j][1])) * ' '
                spacedLocations[i][j] = str(map[i][j][1]) + str(whitespace)
        return spacedLocations, maxLen

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
        spacedLocations, maxLen = self.getSpacedLocations(self.map)
        self.printSeparator(maxLen, spacedLocations[0])
        for row in spacedLocations:
            self.printRow(row)
            self.printSeparator(maxLen, row)

    # this method uses a findmax algorithm to get the longest element in the shortLocations list in this case. this max
    # value is used to append the appropriate amount of whitespace to the rest of the location elements
    def getMaxLen(self, list):
        maxLen = 0
        for i in range(0, len(list)):
            currLen = len(list[i])
            if currLen > maxLen:
                maxLen = currLen
        return maxLen

    # returns a random row and column for use when it is required
    def randomRowCol(self):
        randRow, randCol = randint(0, (self.rowSize - 1)), randint(0, (self.colSize - 1))
        return randRow, randCol

    def getSizes(self):
        return self.colSize, self.rowSize

    def getLocation(self, player):
        return self.map[player.rowLocation][player.colLocation][0]

    def getVisited(self, player):
        return self.map[player.rowLocation][player.colLocation][2]

    def setVisited(self, player):
        self.map[player.rowLocation][player.colLocation][2] = True

    def getMap(self):
        return self.map


# game class, the game class contains any of the methods which pertain to the general running of the game
class game:

    # a versatile error display function which can be expanded with many possible errors using error codes, prints
    # predefined error messages
    @staticmethod
    def displayError(messageNo, player):
        if messageNo == 1:
            message = 'Incorrect direction command entered, please enter another, ' + player.name + '.'
        elif messageNo == 2:
            message = 'Collision, you cannot move this way. Choose another direction, ' + player.name + '.'
        elif messageNo == 3:
            message = 'Unrecognised command, please enter another, ' + player.name + '.'
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
        elif command.lower() in mapCommands:
            map.displayMap()
        elif command.lower() in scoreCommands:
            player.displayScore()
        elif command.lower() in quitCommands:
            self.endGame()
        elif command.lower() == '' or None:
            self.displayError(3, player)
            self.getCommand(player, input('Enter new command: '), map)
        else:
            self.displayError(3, player)
            self.getCommand(player, input('Enter new command: '), map)

    # this method is the main game loop which is called at the start of the game and runs until the end of the process
    # it handles getting the command from the user, checking to see if the player has visited all of the locations as
    # well as checking the amount of moves the player has completed
    def gameLoop(self, player, gameMap):
        player.getLocation(gameMap)
        gameMap.visitLocation(player)
        endFlag = False
        while 1:
            self.getCommand(player, input('\n' + 'What would you like to do?: '), gameMap)
            player.getLocation(gameMap)
            count = gameMap.checkVisited()
            if count == gameMap.rowSize * gameMap.colSize:
                while endFlag is False:
                    decision = input('Would you like to keep exploring? (Y or N): ')
                    if decision.lower() in yesCommands:
                        endFlag = True
                        print('Enter a quit command to leave the game once you are done exploring!')
                    elif decision.lower() in noCommands:
                        self.endGame(1)
            player.checkMoves()

    @staticmethod
    def endGame(endingNo):
        if endingNo == 1:
            print(ending1 + copyrightMessage + ending3)
            quit()
        elif endingNo == 2:
            print(ending2 + copyrightMessage + ending3)
            quit()


# class instantiations, defines the size of the map and the locations to place in it
game = game()
gameMap = map(4, 4, mapLocations, shortLocations)


# title display routine
def displayTitle():
    cprint(figlet_format('A Text Adventure!', font='big'), 'white', attrs=['bold'])


# starting routine
def startGame():
    displayTitle()
    input(introduction)
    randomRow, randomColumn = gameMap.randomRowCol()
    character = Player(input('Enter the name of your character: '), randomRow,
                       randomColumn, gameMap)
    game.gameLoop(character, gameMap)


startGame()
