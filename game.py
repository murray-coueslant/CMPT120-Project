# a simple text adventure game with five locations
# Written by: Murray Coueslant, Date: 2017/09/08

from pyfiglet import figlet_format
from termcolor import cprint

#variable definitions

copyright = ('This game is property of Murray Coueslant. Any enquiries can be sent to murray.coueslant1@marist.edu. Fair'
          ' use is permitted.' + '\n')

# location definitions

loc1 = 'in a dark room, around you you can feel some sticks. In your pocket you feel a lighter. You bundle some  ' \
       'of the sticks with your shirt to create a makeshift torch. You light the torch, revealing a wooden ' \
       'door to the left of you.'

loc2 = 'in an open clearing. Behind you is the hut you just left. It is twilight so you decide to keep your ' \
       'torch lit. How did you end up here? What were you doing in the hut before you fell unconscious? Ahead of ' \
       'you you spot some broken brush, you follow the tracks.'

loc3 = 'surrounded by trees. On the path in front of you lay strange markings, they seem to lead somewhere so you ' \
       'follow them. Eventually you realise that they are your own footsteps. It is clear that you were running. ' \
       'What could you have been running from?'

loc4 = 'at the end of the tracks, what you find makes you step back a few paces. At your feet lies a glowing green ' \
       'object. What is it? How did it get here? Suddenly, the glowing becomes more and more intense until you can ' \
       'barely see anymore. Above you, you hear a loud droning noise as a shadow descends over the clearing. You turn' \
       'on your heels and run as fast as your legs can muster.'

loc5 = 'being chased by the shadow. You keep running until you begin to find some signs of civilisation, then the ' \
       'shadow stops chasing you. You continue to travel on until you manage to flag down a car to bring you to the ' \
       'next town over. You will never return to those woods.'

locations = [loc1, loc2, loc3, loc4, loc5]

# storage variables

score = 0

playerLocation = locations[0]


# starting routine
def startGame():
    displayTitle()
    input('Welcome to a text adventure game. You are a lonely wanderer who has woken up in a strange place, this is '
          'the story of your most recent intrepid adventure. Press enter to begin.')
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
    print('You find yourself ' + location + '\n')


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
        else:
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


# copyright message display routine
def displayCopyright():
    print(copyright)


startGame()
