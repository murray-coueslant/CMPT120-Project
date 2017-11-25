from pyfiglet import figlet_format
from termcolor import cprint
from random import shuffle, randint
from classes import Player, Locale, World, Item

longDescriptions = [('a sandy beach, the waves lap onto the shore steadily. You look to the horizon and see nothing but '
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
                
shortDescriptions = ['Sandy Beach',
                     'Dense Rain forest',
                     'Open Clearing',
                     'Roaring Waterfall',
                     'Strange Cave Front',
                     'Decrepit Marine Dock',
                     'Abandoned Hut',
                     'Little Creek',
                     'Fallen Tree',
                     'Huge Totem']

itemNames = ['map',
             'rope',
             'armour',
             'sword',
             'pickaxe',
             'radio']

items = []

locations = []

for i in range(0, len(longDescriptions)):
    locations.append(Locale(longDescriptions[i], shortDescriptions[i]))

for i in range(0, len(itemNames)):
    items.append(Item(itemNames[i], i))
    print(items[i].name)


gameWorld = World(locations, 5, 5, items)


