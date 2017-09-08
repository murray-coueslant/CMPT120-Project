# a simple text adventure game with four locations
# Written by: Murray Coueslant, Date: 2017/09/08

import sys
from pyfiglet import figlet_format
from termcolor import cprint

# location definitions

loc1 = 'a dark room, around you you can feel some sticks. In your pocket you feel a lighter. You bundle some of the ' \
       'sticks with your shirt to create a makeshift torch. You light the torch revealing a wooden ' \
       'door to the left of you.'

loc2 = 'an open clearing. Behind you is the hut you just left. It is twilight so you decide to keep your torch lit.' \
       'How did you end up here? What were you doing in the hut before you fell unconscious? Ahead of you you spot' \
       'some broken brush, you follow the tracks.'

loc3 = 'c'

loc4 = 'd'

loc5 = 'e'

locations = [loc1, loc2, loc3, loc4, loc5]

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
    print('Score:', score, '\n')

# location display routine
def displayLocation(location):
    print('You find yourself in ' + location + '\n')

# main game routine
def game(score, locations):
    locationCounter = 0
    currentLocation = locations[locationCounter]
    while locationCounter <= 4:
        displayLocation(currentLocation)
        if locationCounter == 4:
            score += 5
            displayScore(score)
            input('Press enter to complete the game.' + '\n')
            endGame()
            return
        locationCounter += 1
        currentLocation = locations[locationCounter]
        score += 5
        displayScore(score)
        input('Press enter to move to the next location.'+'\n')

# end of game routine
def endGame():
    print('\n' + 'Congratulations, you have made it home safely. You rest for a few days and then return to normal '
          'life.' + '\n')
    displayCopyright()
    print('I hope you enjoyed playing this game. See you soon!' + '\n')

def displayCopyright():
    print('This game is property of Murray Coueslant. Any enquiries can be sent to murray.coueslant1@marist.edu. Fair'
          ' use is permitted.' + '\n')

startGame()

