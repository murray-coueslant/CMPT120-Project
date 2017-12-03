# a more complex text adventure game, with a randomly generated map and player control
# Written by: Murray Coueslant, Date: 2017/12/3

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
movementCommands = ['go', 'move', 'travel']
northCommands = ['n', 'north']
eastCommands = ['e', 'east']
southCommands = ['s', 'south']
westCommands = ['w', 'west']
helpCommands = ['h', 'help']
mapCommands = ['m', 'map', 'world']
scoreCommands = ['score', 'points', 'total']
yesCommands = ['y', 'yes', 'yep', 'yeah', 'okay', 'please']
noCommands = ['n', 'no', 'nope', 'nah']
quitCommands = ['q', 'quit', 'exit', 'end', 'leave']
lookCommands = ['look', 'view', 'explore']
searchCommands = ['search', 'examine']
inventoryCommands = ['inventory', 'bag', 'things', 'stuff', 'possessions']
takeCommands = ['take', 'grab', 'pick', 'hold']
specialCommands = ['climb', 'scale', 'enter', 'spelunk']
easyWords = ['easy', 'e', 'simple']
mediumWords = ['medium', 'm', 'moderate']
hardWords = ['hard', 'h', 'complex']





        


# game class, the game class contains any of the methods which pertain to the general running of the game
class game:

    # a versatile error display function which can be expanded with many possible errors using error codes, prints
    # predefined error messages
    @staticmethod
    def displayError(messageNo, player):
        if messageNo == 1:
            message = 'Incorrect direction command entered, please enter another, ' + player.name + '.'
        elif messageNo == 2:
            message = 'You have reached the edge of the island! Choose another direction, ' + \
                player.name + '.'
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
        if map.map[player.rowLocation][player.colLocation].shortDescription == 'Roaring Waterfall':
            if 'rope' in player.inventory:
                cprint('You have something in your possession which might help you here. Try climbing the falls.',
                       'yellow')
            else:
                cprint(
                    'Perhaps if you had a rope or a safety net, you could climb these falls...', 'yellow')
        if map.map[player.rowLocation][player.colLocation].shortDescription == 'Strange Cave Front':
            if 'armour' in player.inventory and 'sword' in player.inventory:
                cprint(
                    'You are well equipped for exploring, try entering the cave.', 'yellow')
            else:
                cprint(
                    'Maybe you could enter the cave, if you had the right equipment...', 'yellow')
        if map.map[player.rowLocation][player.colLocation].shortDescription == 'Fallen Tree':
            if 'armour' not in player.inventory:
                self.specialEnding(player, map)

    # this method sets the max number of moves a player has which acts as the 'difficulty' in the game
    def setDifficulty(self, difficulty, player, map):
        if difficulty.lower().strip() in easyWords:
            player.maxMoves = 5 * (map.colSize * map.rowSize)
            return
        elif difficulty.lower().strip() in mediumWords:
            player.maxMoves = 3 * (map.colSize * map.rowSize)
            return
        elif difficulty.lower().strip() in hardWords:
            player.maxMoves = 2 * (map.colSize * map.rowSize)
            return
        else:
            print('Incorrect difficulty entered, try again.')
            self.setDifficulty(input(
                'What difficulty would you like to play on? (Easy, Medium, Hard): '), player, map)

    # the getCommand method is the place where the user input is parsed and the correct action performed depending on
    # the command entered
    # TODO: this whole function is super long and convoluted, i'm sure there is an easier way to parse commands from the
    # TODO: user and condense this whole code
    def getCommand(self, player, command, map):
        inCommand = command.strip().lower()
        parseCommand = inCommand.split(' ')
        if parseCommand[0] in movementCommands:
            if len(parseCommand) > 1:
                if parseCommand[1] in northCommands:
                    player.movePlayer('north', map)
                elif parseCommand[1] in eastCommands:
                    player.movePlayer('east', map)
                elif parseCommand[1] in southCommands:
                    player.movePlayer('south', map)
                elif parseCommand[1] in westCommands:
                    player.movePlayer('west', map)
            else:
                print(parseCommand[0], 'must be paired with a direction. Try entering a direction.')
        elif parseCommand[0] in helpCommands:
            self.displayHelp()
        elif parseCommand[0] in mapCommands:
            if 'map' in player.inventory:
                map.displayMap()
            else:
                print('You cannot look at a map you do not have!')
        elif parseCommand[0] in scoreCommands:
            player.displayScore()
        elif parseCommand[0] in quitCommands:
            self.endGame(4)
        elif parseCommand[0] in lookCommands:
            player.getLongLocation(map)
            return 'long'
        elif parseCommand[0] in searchCommands:
            player.itemSearch(map)
        elif parseCommand[0] in inventoryCommands:
            player.getInventory()
        elif parseCommand[0] in takeCommands:
            if len(parseCommand) > 1:
                player.takeItem(map, parseCommand[1])
            else:
                print(parseCommand[0], 'must be paired with an item. Enter the item you want to grab.')
        elif parseCommand[0] in specialCommands:
            game.specialEnding(player, map)
        elif parseCommand[0] == '' or None:
            self.displayError(3, player)
            self.getCommand(player, input('Enter new command: '), map)
        else:
            self.displayError(3, player)
            self.getCommand(player, input('Enter new command: '), map)

    # the specialEnding method displays the result of the ending which the player has accessed. It checks the conditions
    # the same as the checkSpecialLocation method to ensure that they are met and then displays a special message and
    # quits the game
    def specialEnding(self, player, map):
        if map.map[player.rowLocation][player.colLocation].shortDescription == 'Roaring Waterfall' and 'rope' in player.inventory:
            cprint('You climb the waterfall and eventually manage to signal a low flying aircraft. You are saved!',
                   'green')
            self.endGame(3)
        elif map.map[player.rowLocation][player.colLocation].shortDescription == 'Roaring Waterfall' and 'rope' not in \
                player.inventory:
            cprint('You try to climb the falls with no rope, this was an obviously stupid idea. You fall to your death '
                   'from 60 feet in the air.', 'red')
            self.endGame(3)
        elif map.map[player.rowLocation][player.colLocation].shortDescription == 'Strange Cave Front' and 'armour' in \
                player.inventory and 'sword' in player.inventory:
            cprint('You enter the cave, alert for danger. You follow it down to discover a hidden cove. A sail boat sits '
                   'idly in the water. You sail it out to sea and eventually come across a larger vessel which rescues '
                   'you. You are saved!', 'green')
            self.endGame(3)
        elif map.map[player.rowLocation][player.colLocation].shortDescription == 'Strange Cave Front' and 'armour' not in \
                player.inventory and 'sword' not in player.inventory:
            cprint('You try to enter the cave without the proper equipment, you walk ten feet into the cave and '
                   'succumb to a well hidden trap.', 'red')
            self.endGame(3)
        elif map.map[player.rowLocation][player.colLocation].shortDescription == 'Fallen Tree':
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
            locationFlag = self.getCommand(player, input(
                '\n' + 'What would you like to do?: '), gameMap)
            game.checkSpecialLocation(player, gameMap)
            if locationFlag == 'long':
                pass
            count = gameMap.checkVisited()
            if count == gameMap.rowSize * gameMap.colSize:
                while endFlag is False:
                    decision = input(
                        'Would you like to keep exploring? (Y or N): ')
                    if decision.lower() in yesCommands:
                        endFlag = True
                        print(
                            'Enter a quit command to leave the game once you are done exploring!')
                    elif decision.lower() in noCommands:
                        self.endGame(1)
            player.checkMoves()


# class instantiations, defines the size of the map and the locations to place in it
game = game()
gameMap = map(5, 4, mapLocations, shortLocations, items)


# title display routine
def displayTitle():
    cprint(figlet_format('A Huge Text Adventure!',
                         font='larry3d'), 'red', attrs=['bold'])


# starting routine
def startGame():
    displayTitle()
    var = input(introduction)
    randomRow, randomColumn = gameMap.randomRowCol()
    while gameMap.map[randomRow][randomColumn].shortDescription == 'Fallen Tree':
        randomRow, randomColumn = gameMap.randomRowCol()
    character = Player(str(input('Enter the name of your character: ')).strip(), randomRow,
                       randomColumn, gameMap)
    game.setDifficulty(input(
        'What difficulty would you like to play on? (Easy, Medium, Hard): '), character, gameMap)
    print('\nEnter the \'help\' command to see what you can do!\n')
    game.gameLoop(character, gameMap)


startGame()
