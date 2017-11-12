# a more complex text adventure game, with a randomly generated map and player control
# Written by: Murray Coueslant, Date: 2017/11/12

from pyfiglet import figlet_format
from termcolor import cprint
from random import shuffle, randint


# variable definitions, these are things which are used often like message strings etc... or things which would make
# code look ugly if used often in their normal form

introduction = ('Welcome to a text adventure game. You are a lonely wanderer who has woken up on an island, '
                'it is your task to explore your surroundings. Press enter to begin.')
ending1 = '\nCongratulations, you have explored the whole island!\n'
ending2 = '\nUnfortunately, you have run out of moves!\n'
ending3 = '\nYou discovered a special ending, congratulations!\n'
ending4 = 'I hope you enjoyed playing this game. See you soon!\n'
ending5 = '\nSuccessfully quitting game, thank you for playing.\n'
copyrightMessage = ('This game is property of Murray Coueslant. Any enquiries can be sent to '
                    'murray.coueslant1@marist.edu. Fair use is permitted.\n')
helpMessage = ('Help:\nEnter a command below, the possible commands are:\n\tnorth, south, '
               'east, west\n\tgo, move or travel + a direction\n\tquit, exit, leave, end\n\tmap, world, view world '
               '(only once you find the map!)\n\tpoints, score or total\n\tlook, explore\n\tsearch, examine\n'
               'or this help command, but you figured that one out, go you!')

# location set definition
mapLocations = [('a sandy beach, the waves lap onto the shore steadily. You look to the horizon and see nothing but '
                 'the blue expanse of the ocean. You contemplate how you got here, and how you are going to get home.'),
                ('a dense rain forest. The sound of creatures in the bush is overwhelming, the smell is tropical. '
                 'You are afraid, a predator could appear at any time. You think about what would happen if you did '
                 'not return home.'),
                ('an open clearing. On the ground in front of you there is a pile of strange stones. You are not '
                 'sure what they are for. You wonder if there were once people here, and if so, where are they now?'),
                ('a roaring waterfall. The white wash rolls from the top of the colossal stones, plunging into a '
                 'pool of dark water. You wonder if there is anything down there, or maybe there is a secret passage '
                 'behind the falls. You attempt to find the passage, but your luck comes up dry.'),
                ('a strange cave front. There are remnants of exploration here, makeshift torches and tools. '
                 'You decide that it is likely not sensible to go into the cave without proper protection. '
                 'You guess that people have before you; and it has not ended well.'),
                ('a decrepit marine dock. The wood of the jetty is rotting away, there is a rusting hull of a small '
                 'sailboat which is somehow still tied to the jetty. You wonder whether this was once the only '
                 'connection this island had to the outside world.'),
                ('an abandoned hut. The side of the hut has strange images painted on it in red paint, and there are '
                 'no windows on any side. The door sits ajar, you pry it open to reveal some more bizarre paintings '
                 'on the wall as well as hundreds of papers on the floor. You decide not to enter any farther into '
                 'the structure for fear of crazies.'),
                ('a little creek. The water rushes by and you see some small fish glimmering in the sunlight. '
                 'You dip your hands into the water and take a drink. The water is cold and fresh, you fill your '
                 'vessel from the creek and carry on ahead.'),
                ('a fallen tree. The collosal trunk is hollow after all of the time spent laying on the ground. '
                 'There are clearly animals who call this trunk their home. You decide to move on, you\'d rather not '
                 'meet any of them.'),
                ('a huge totem. There are bizarre symbols carved into the sculpture. Maybe you will return to figure '
                 'out what they mean.')]
shortLocations = ['Sandy Beach',
                  'Dense Rain forest',
                  'Open Clearing',
                  'Roaring Waterfall',
                  'Strange Cave Front',
                  'Decrepit Marine Dock',
                  'Abandoned Hut',
                  'Little Creek',
                  'Fallen Tree',
                  'Huge Totem']

# item set definition
items = ['map',
         'rope',
         'armour',
         'sword']

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
lookCommands = ['look', 'look around', 'view', 'explore']
searchCommands = ['search', 'search area', 'search location', 'examine']
inventoryCommands = ['inventory', 'bag', 'things', 'stuff', 'possessions']
takeCommands = ['take', 'grab', 'pick up', 'pick', 'hold']
specialCommands = ['climb', 'scale', 'enter', 'spelunk']
easyWords = ['easy', 'e', 'simple']
mediumWords = ['medium', 'm', 'moderate']
hardWords = ['hard', 'h', 'complex']

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
        self.maxMoves = 0
        self.inventory = []
        self.map = map
    # this method is used to change the location of the player within the world map, it takes a direction in the form
    # of a string and a map object and uses an if elif else statement to decide which direction to move the player in,
    # once decided it modifies the current location of the player in the correct way for the desired direction

    def movePlayer(self, direction, map):
        if direction.lower() == 'north':
            self.rowLocation -= 1
            if self.rowLocation < 0:
                game.displayError(2, self)
                self.rowLocation += 1
            else:
                map.visitLocation(self, map)
                self.increaseMoves()
        elif direction.lower() == 'south':
            self.rowLocation += 1
            if self.rowLocation > (map.rowSize - 1):
                game.displayError(2, self)
                self.rowLocation -= 1
            else:
                map.visitLocation(self, map)
                self.increaseMoves()
        elif direction.lower() == 'east':
            self.colLocation += 1
            if self.colLocation > (map.colSize - 1):
                game.displayError(2, self)
                self.colLocation -= 1
            else:
                map.visitLocation(self, map)
                self.increaseMoves()
        elif direction.lower() == 'west':
            self.colLocation -= 1
            if self.colLocation < 0:
                game.displayError(2, self)
                self.colLocation += 1
            else:
                map.visitLocation(self, map)
                self.increaseMoves()
        else:
            game.displayError(1, self)

    def getName(self):
        return self.name

    # outputs a formatted list of the items which the player has in their inventory currently
    def getInventory(self):
        if len(self.inventory) == 0:
            print('You\'re not carrying anything!')
        else:
            print('In your inventory you have:')
            for i in self.inventory:
                print('-' + '\t'+str(i))

    # the getLocation method is what displays the current location of the character to the user. It has two different
    # messages depending on whether or not there is a special location at the player's current position
    def getLocation(self, map):
        if map.getLocation(self) == 'There is nothing here.':
            print(self.name, 'finds nothing, you should keep exploring.')
        else:
            print(self.name, 'is currently at', map.getLocation(self))

    # get long location outputs the long description of a location to the player
    def getLongLocation(self, map):
        if map.getLocation(self) == 'There is nothing here.':
            print(self.name, 'finds nothing, you should keep exploring.')
        else:
            print(self.name, 'is currently at', map.getLongLocation(self))

    # itemSearch looks in the player's current position to see if there is a retrievable item for the player there
    def itemSearch(self, map):
        if map.map[self.rowLocation][self.colLocation][4] is False:
            if map.map[self.rowLocation][self.colLocation][3] is not None:
                item = map.map[self.rowLocation][self.colLocation][3]
                print('You have found:', item[0])
                map.map[self.rowLocation][self.colLocation][4] = True
            else:
                print('No items here!')
                map.map[self.rowLocation][self.colLocation][4] = True
        else:
            print('You have already searched here!')

    # takeItem adds the item to the player's inventory and marks it as taken, if a player attempts to take it again
    # it will inform them that it has already been taken
    def takeItem(self, map):
        if map.map[self.rowLocation][self.colLocation][4] is False:
            print('You can\'t take something you haven\'t looked for!')
        else:
            if map.map[self.rowLocation][self.colLocation][3] is not None:
                item = map.map[self.rowLocation][self.colLocation][3]
                if item[1] is False:
                    self.inventory.append(item[0])
                    print('You have picked up:', item[0])
                    item[1] = True
                else:
                    print("You have already picked up the", item[0])
            else:
                cprint('Nothing to take!', 'red')

    # this method checks to see if the player has used up all of their available moves for the current game
    def checkMoves(self):
        if self.moves >= self.maxMoves:
            cprint('You have run out of moves, try again!', 'red')
            game.endGame(2)
        else:
            cprint('You have ' + str(self.maxMoves-self.moves) + ' moves remaining, use them wisely!', 'blue')

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
        cprint((self.getName()+', ' + 'your score is: ' + str(self.getScore())), 'blue')

# map class definition, the map class contains the required variables and methods pertaining to the world map for the
# game. the methods encompass things such as filling the map with locations on startup etc...


class map:
    def __init__(self, rowSize, colSize, locations, shortLocations, items):
        self.rowSize = rowSize
        self.colSize = colSize
        self.locations = locations
        self.shortLocations = shortLocations
        self.items = items
        # defines a 2D array of an arbitrary size which is defined when the class is instantiated
        self.map = [[None for cols in range(colSize)] for rows in range(rowSize)]
        orderList = list(range(len(self.locations)))
        itemList = list(range(len(self.items)))
        # the program uses the shuffle command from the random library to determine the positions of the 10 special
        # locations in the map
        shuffle(orderList)
        shuffle(itemList)
        itemCounter = 0
        # this for loop places the 10 shuffled locations in 10 random positions on the map
        for i in orderList:
            randRow, randCol = self.randomRowCol()
            placed = False
            # while loop with a nested if statement which ensures each of the ten locations is placed in a distinct
            # location and that two locations are not placed at the same coordinate
            while not placed:
                if self.map[randRow][randCol] is None and itemCounter < 4:
                    if self.shortLocations[i] == 'Fallen Tree':
                        self.map[randRow][randCol] = [self.locations[i], self.shortLocations[i], False, [None, True],
                                                      False]
                        placed = True
                    else:
                        self.map[randRow][randCol] = [self.locations[i], self.shortLocations[i], False,
                                                      [items[itemList[itemCounter]], False], False]
                        itemCounter += 1
                        placed = True
                elif self.map[randRow][randCol] is None:
                    self.map[randRow][randCol] = [self.locations[i], self.shortLocations[i], False, None, False]
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
                    self.map[i][j] = ['There is nothing here.', 'X X X', 'Flag', None, False]

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
    def visitLocation(self, player, map):
        if self.getVisited(player) == 'Flag':
            player.getLongLocation(map)
            self.setVisited(player)
        elif self.getVisited(player) is False:
            player.increaseScore()
            player.displayScore()
            player.getLongLocation(map)
            self.setVisited(player)
        elif self.getVisited(player) is True:
            print('You have already discovered this location!')
            player.getLocation(map)

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

    # this method uses a findMax algorithm to get the longest element in the shortLocations list in this case. this max
    # value is used to append the appropriate amount of whitespace to the rest of the location elements
    def getMaxLen(self, list):
        maxLen = 0
        for i in range(0, len(list)):
            currLen = len(list[i])
            if currLen > maxLen:
                maxLen = currLen
        return maxLen

    # returns a random row and column within the bounds of the map for use when it is required
    def randomRowCol(self):
        randRow, randCol = randint(0, (self.rowSize - 1)), randint(0, (self.colSize - 1))
        return randRow, randCol

    def getSizes(self):
        return self.colSize, self.rowSize

    def getLocation(self, player):
        return self.map[player.rowLocation][player.colLocation][1]

    def getLongLocation(self, player):
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
            message = 'You have reached the edge of the island! Choose another direction, ' + player.name + '.'
        elif messageNo == 3:
            message = 'Unrecognised command, please enter another, ' + player.name + '.'
        else:
            message = 'Unknown error.'
        cprint(message, 'red')

    @staticmethod
    def displayHelp():
        cprint(helpMessage, 'yellow')

    # checkSpecialLocation looks at the player's current location and checks whether it is one of the locations which
    # has a special ending. If the correct items for the ending are in the player's inventory, a message is shown, if
    # not nothing is shown to the player until they have the correct items
    def checkSpecialLocation(self, player, map):
        if map.map[player.rowLocation][player.colLocation][1] == 'Roaring Waterfall':
            if 'rope' in player.inventory:
                cprint('You have something in your possession which might help you here. Try climbing the falls.',
                       'yellow')
            else:
                cprint('Perhaps if you had a rope or a safety net, you could climb these falls...', 'yellow')
        if map.map[player.rowLocation][player.colLocation][1] == 'Strange Cave Front':
            if 'armour' in player.inventory and 'sword' in player.inventory:
                cprint('You are well equipped for exploring, try entering the cave.', 'yellow')
            else:
                cprint('Maybe you could enter the cave, if you had the right equipment...', 'yellow')
        if map.map[player.rowLocation][player.colLocation][1] == 'Fallen Tree':
            if 'armour' not in player.inventory:
                self.specialEnding(player, map)

    # this method sets the max number of moves a player has which acts as the 'difficulty' in the game
    def setDifficulty(self, difficulty, player, map):
        if difficulty.lower() in easyWords:
            player.maxMoves = 5 * (map.colSize * map.rowSize)
            return
        elif difficulty.lower() in mediumWords:
            player.maxMoves = 3 * (map.colSize * map.rowSize)
            return
        elif difficulty.lower() in hardWords:
            player.maxMoves = 2 * (map.colSize * map.rowSize)
            return
        else:
            print('Incorrect difficulty entered, try again.')
            self.setDifficulty(input('What difficulty would you like to play on? (Easy, Medium, Hard): '), player, map)

    # the getCommand method is the place where the user input is parsed and the correct action performed depending on
    # the command entered
    # TODO: this whole function is super long and convoluted, i'm sure there is an easier way to parse commands from the
    # TODO: user and condense this whole code
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
            if 'map' in player.inventory:
                map.displayMap()
            else:
                print('You cannot look at a map you do not have!')
        elif command.lower() in scoreCommands:
            player.displayScore()
        elif command.lower() in quitCommands:
            self.endGame(4)
        elif command.lower() in lookCommands:
            player.getLongLocation(map)
            return 'long'
        elif command.lower() in searchCommands:
            player.itemSearch(map)
        elif command.lower() in inventoryCommands:
            player.getInventory()
        elif command.lower() in takeCommands:
            player.takeItem(map)
        elif command.lower() in specialCommands:
            game.specialEnding(player, map)
        elif command.lower() == '' or None:
            self.displayError(3, player)
            self.getCommand(player, input('Enter new command: '), map)
        else:
            self.displayError(3, player)
            self.getCommand(player, input('Enter new command: '), map)

    # the specialEnding method displays the result of the ending which the player has accessed. It checks the conditions
    # the same as the checkSpecialLocation method to ensure that they are met and then displays a special message and
    # quits the game
    def specialEnding(self, player, map):
        if map.map[player.rowLocation][player.colLocation][1] == 'Roaring Waterfall' and 'rope' in player.inventory:
            cprint('You climb the waterfall and eventually manage to signal a low flying aircraft. You are saved!',
                   'green')
            self.endGame(3)
        elif map.map[player.rowLocation][player.colLocation][1] == 'Roaring Waterfall' and 'rope' not in \
                player.inventory:
            cprint('You try to climb the falls with no rope, this was an obviously stupid idea. You fall to your death '
                  'from 60 feet in the air.', 'red')
            self.endGame(3)
        elif map.map[player.rowLocation][player.colLocation][1] == 'Strange Cave Front' and 'armour' in \
                player.inventory and 'sword' in player.inventory:
            cprint('You enter the cave, alert for danger. You follow it down to discover a hidden cove. A sail boat sits'
                  'idly in the water. You sail it out to sea and eventually come across a larger vessel which rescues '
                  'you. You are saved!', 'green')
            self.endGame(3)
        elif map.map[player.rowLocation][player.colLocation][1] == 'Strange Cave Front' and 'armour' not in \
                player.inventory and 'sword' not in player.inventory:
            cprint('You try to enter the cave without the proper equipment, you walk ten feet into the cave and '
                  'succumb to a well hidden trap.', 'red')
            self.endGame(3)
        elif map.map[player.rowLocation][player.colLocation][1] == 'Fallen Tree':
            cprint('You are set upon by a large beast which appeared from a huge fallen tree trunk. You do not make it '
                  'out alive.', 'red')
            self.endGame(3)

    @staticmethod
    def endGame(endingNo):
        if endingNo == 1:
            cprint(ending1 + copyrightMessage + ending4, 'blue')
            quit()
        elif endingNo == 2:
            cprint(ending2 + copyrightMessage + ending4, 'blue')
            quit()
        elif endingNo == 3:
            cprint(ending3 + copyrightMessage + ending4, 'blue')
            quit()
        elif endingNo == 4:
            cprint(ending5 + copyrightMessage, 'blue')
            quit()

    # this method is the main game loop which is called at the start of the game and runs until the end of the process
    # it handles getting the command from the user, checking to see if the player has visited all of the locations as
    # well as checking the amount of moves the player has completed
    def gameLoop(self, player, gameMap):
        gameMap.visitLocation(player, gameMap)
        endFlag = False
        while 1:
            locationFlag = self.getCommand(player, input('\n' + 'What would you like to do?: '), gameMap)
            game.checkSpecialLocation(player, gameMap)
            if locationFlag == 'long':
                pass
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


# class instantiations, defines the size of the map and the locations to place in it
game = game()
gameMap = map(5, 4, mapLocations, shortLocations, items)


# title display routine
def displayTitle():
    cprint(figlet_format('A Huge Text Adventure!', font='larry3d'), 'red', attrs=['bold'])


# starting routine
def startGame():
    displayTitle()
    var = input(introduction)
    randomRow, randomColumn = gameMap.randomRowCol()
    while gameMap.map[randomRow][randomColumn][1] == 'Fallen Tree':
        randomRow, randomColumn = gameMap.randomRowCol()
    character = Player(input('Enter the name of your character: '), randomRow,
                       randomColumn, gameMap)
    game.setDifficulty(input('What difficulty would you like to play on? (Easy, Medium, Hard): '), character, gameMap)
    print('\nEnter the \'help\' command to see what you can do!\n')
    game.gameLoop(character, gameMap)


startGame()
