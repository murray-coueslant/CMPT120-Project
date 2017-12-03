# a more complex text adventure game, with a randomly generated map and player control
# Written by: Murray Coueslant, Date: 2017/12/3

from pyfiglet import figlet_format
from termcolor import cprint
from random import shuffle, randint
from classes import Player, map, Locale, game

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
