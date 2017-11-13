class Player():
    def __init__(self, name, score, currentX, currentY, moveCount, inventory):
        self.name = name
        self.score = score
        self.currentX = currentX
        self.currentY = currentY
        self.moveCount = moveCount
        self.inventory = inventory

class Locale():
    def __init__(self, name, longDescription, shortDescription, visited, searched, itemList):
        self.name = name
        self.longDescription = longDescription
        self.shortDescription = shortDescription
        self.visited = visited
        self.searched = searched
        self.itemList = itemList