class Player():
    def __init__(self, name, score = 0, currentX = 0, currentY = 0, moveCount = 0, inventory = []):
        self.name = str(name)
        self.score = score
        self.currentX = currentX
        self.currentY = currentY
        self.moveCount = moveCount
        self.inventory = inventory

    def getName(self):
        print(self.name)

class Locale():
    def __init__(self, longDescription, shortDescription, visited = False, searched = False, itemList = []):
        self.name = name
        self.longDescription = longDescription
        self.shortDescription = shortDescription
        self.visited = visited
        self.searched = searched
        self.itemList = itemList
    
    def visit(self):
        self.visited = True

    def search(self):
        if self.searched = False:
            self.searched = True
            if len(itemList) > 0:
                print('You have found: \n')
                for i in range(0, len(itemList)):
                    print('\t' + str(itemList[i]))
        
    def longDescription(self):
        return self.longDescription

class world:
    def __init__(self):
        