# a simple text adventure game with four locations
# Written by: Murray Coueslant, Date: 2017/09/08

import sys
from pyfiglet import figlet_format
from termcolor import cprint

# location definitions

loc1 = 'a dark room, around you you can feel some sticks. In your pocket you feel a lighter. You bundle some of the ' \
       'sticks with your shirt to create a makeshift torch. You light the torch revealing a wooden ' \
       'door to the left of you.'

loc2 = 'b'

loc3 = 'c'

loc4 = 'd'

locations = [loc1, loc2, loc3, loc4]

# storage variables

score = 0

playerLocation = locations[0]

# starting routine
def startGame():
    displayTitle()

# title display routine
def displayTitle():
    cprint(figlet_format('A Text Adventure!', font='big'),
           'white', attrs=['bold'])

startGame()

