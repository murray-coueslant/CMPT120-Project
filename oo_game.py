# a more complex text adventure game, with a randomly generated map and player control
# Written by: Murray Coueslant, Date: 2017/12/3

from pyfiglet import figlet_format
from termcolor import cprint
from random import shuffle, randint
from classes import Player, map, Locale, game

introduction = ('Welcome to a text adventure game. You are a lonely wanderer who has woken up on an island, '
                'it is your task to explore your surroundings. Press enter to begin.')

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
                 'out what they mean.'),
                ('a crashed plane. The hull is rusted and old. There are signs of previous inhabitants here, however it'
                 'does not look like anyone has lived here for a long time.'),
                ('a deep well. You drop a stone down the structure, but you never hear it land. You wonder where it leads.')]
shortLocations = ['Sandy Beach',
                  'Dense Rain forest',
                  'Open Clearing',
                  'Roaring Waterfall',
                  'Strange Cave Front',
                  'Decrepit Marine Dock',
                  'Abandoned Hut',
                  'Little Creek',
                  'Fallen Tree',
                  'Huge Totem',
                  'Crashed Plane',
                  'Deep Well']

# item set definition
items = ['map',
         'rope',
         'armour',
         'sword',
         'radio',
         'pickaxe']

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