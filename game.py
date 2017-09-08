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
    print('Welcome to a text adventure game. You are a lonely wanderer who has woken up in a strange place, this is',
          'the story of your most recent intrepid adventure.'+'\n')
    displayScore(score)
    game(score, locations)

# title display routine
def displayTitle():
    cprint(figlet_format('A Text Adventure!', font='big'),
           'white', attrs=['bold'])

# score display routine
def displayScore(score):
    print('Score:', score)

# location display routine
def displayLocation(location):
    print('You find yourself in', location)

# main game routine
def game(score, locations):
    locationCounter = 0
    currentLocation = locations[locationCounter]
    while locationCounter <= 3:
        displayLocation(currentLocation)
        if locationCounter == 3:
            endGame()
        locationCounter += 1
        currentLocation = locations[locationCounter]
        score += 5
        displayScore(score)
        input('Press enter to move to the next location.')

# end of game routine
def endGame():
    x = 1
startGame()

