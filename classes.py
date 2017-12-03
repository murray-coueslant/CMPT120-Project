class Player:
    # initialising the variables which store the essential data for the player object
    def __init__(self, name, rowLocation, colLocation, map, score=0):
        self.name = name
        self.score = score
        self.rowLocation = rowLocation
        self.colLocation = colLocation
        self.moves = 0
        self.maxMoves = 0
        self.inventory = []
        self.map = map
    # this method is used to change the location of the player within the world map, it takes a direction in the form
    # of a string and a map object and uses an if elif else statement to decide which direction to move the player in,
    # once decided it modifies the current location of the player in the correct way for the desired direction

    def movePlayer(self, direction, map):
        if direction.lower() == 'north':
            self.rowLocation -= 1
            if self.rowLocation < 0:
                game.displayError(2, self)
                self.rowLocation += 1
            else:
                map.visitLocation(self, map)
                self.increaseMoves()
        elif direction.lower() == 'south':
            self.rowLocation += 1
            if self.rowLocation > (map.rowSize - 1):
                game.displayError(2, self)
                self.rowLocation -= 1
            else:
                map.visitLocation(self, map)
                self.increaseMoves()
        elif direction.lower() == 'east':
            self.colLocation += 1
            if self.colLocation > (map.colSize - 1):
                game.displayError(2, self)
                self.colLocation -= 1
            else:
                map.visitLocation(self, map)
                self.increaseMoves()
        elif direction.lower() == 'west':
            self.colLocation -= 1
            if self.colLocation < 0:
                game.displayError(2, self)
                self.colLocation += 1
            else:
                map.visitLocation(self, map)
                self.increaseMoves()
        else:
            game.displayError(1, self)

    def getName(self):
        return self.name

    # outputs a formatted list of the items which the player has in their inventory currently
    def getInventory(self):
        if len(self.inventory) == 0:
            print('You\'re not carrying anything!')
        else:
            print('In your inventory you have:')
            for i in self.inventory:
                print('-' + '\t' + str(i))

    # the getLocation method is what displays the current location of the character to the user. It has two different
    # messages depending on whether or not there is a special location at the player's current position
    def getLocation(self, map):
        if map.getLocation(self) == 'an empty place.':
            print(self.name, 'finds nothing, you should keep exploring.')
        else:
            print(self.name, 'is currently at', map.getLocation(self))

    # get long location outputs the long description of a location to the player
    def getLongLocation(self, map):
        if map.getLocation(self) == 'an empty place.':
            print(self.name, 'finds nothing, you should keep exploring.')
        else:
            print(self.name, 'is currently at', map.getLongLocation(self))

    # itemSearch looks in the player's current position to see if there is a retrievable item for the player there
    def itemSearch(self, map):
        if map.map[self.rowLocation][self.colLocation].searched is False:
            if len(map.map[self.rowLocation][self.colLocation].items) is not 0:
                item = map.map[self.rowLocation][self.colLocation].items
                print('You have found:')
                for i in item:
                    print('\t'+i)
                map.map[self.rowLocation][self.colLocation].searched = True
            else:
                print('No items here!')
                map.map[self.rowLocation][self.colLocation].searched = True
        else:
            print('You have already searched here!')

    # takeItem adds the item to the player's inventory and marks it as taken, if a player attempts to take it again
    # it will inform them that it has already been taken
    def takeItem(self, map, item):
        if map.map[self.rowLocation][self.colLocation].searched is False:
            print('You can\'t take something you haven\'t looked for!')
        else:
            items = map.map[self.rowLocation][self.colLocation].items
            if item in items:
                self.inventory.append(item)
                items.remove(item)
                print('You have picked up:', item)
            else:
                print('No', item, 'here!')

    # this method checks to see if the player has used up all of their available moves for the current game
    def checkMoves(self):
        if self.moves >= self.maxMoves:
            cprint('You have run out of moves, try again!', 'red')
            game.endGame(2)
        else:
            cprint('You have ' + str(self.maxMoves - self.moves) +
                   ' moves remaining, use them wisely!', 'blue')

    def getXPos(self):
        return self.colLocation

    def getYPos(self):
        return self.rowLocation

    def getScore(self):
        return self.score
    
    def increaseScore(self):
        self.score += 5

    def increaseMoves(self):
        self.moves += 1

    def displayScore(self):
        cprint((self.getName() + ', ' + 'your score is: ' +
                str(self.getScore())), 'blue')

# locale class greatly simplifies accessing the different pieces of data required at each location
class Locale:
    def __init__(self, longDescription, shortDescription, items = [], visited = False, searched = False):
        self.longDescription = longDescription
        self.shortDescription = shortDescription
        self.visited = visited
        self.items = items
        self.searched = searched