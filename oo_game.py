# a more complex text adventure game, with a randomly generated map and player control
# Written by: Murray Coueslant, Date: 2017/12/15

from random import randint, shuffle

from pyfiglet import figlet_format
from termcolor import cprint

from classes import Locale, Player, game, map

# class instantiation creates a new instance of the game class
game = game()

# calls the newGame method to begin the process of starting the game
game.newGame()