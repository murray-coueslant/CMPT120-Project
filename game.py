# a simple text adventure game with four locations
# Written by: Murray Coueslant, Date: 2017/09/08

import random

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


