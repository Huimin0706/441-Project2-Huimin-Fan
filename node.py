class Node:
    '''
    img: an image file (.png works) that shows the state
    id: the id for the state
    connections: a list of the other states that can be reached from this state
    what else do you want to add...?
    '''
    img = None
    id = -1
    connections = []
    #what else should you add?

    def __init__(self, img=None, nodeId=-1, vacuumPos=0, cells=('D', 'D')):
        self.img = img
        self.id = nodeId
        self.connections = []
        self.vacuumPos = vacuumPos
        self.cells = tuple(cells)
        self.isGoal = all(c == 'C' for c in self.cells)

    def getImg(self):
        return self.img

    def getId(self):
        return self.id

    def getConnections(self):
        return self.connections

    def getVacuumPos(self):
        return self.vacuumPos

    def getCells(self):
        return self.cells

    def getIsGoal(self):
        return self.isGoal

    def setImg(self, img):
        self.img = img

    def setId(self, nodeId):
        self.id = nodeId

    def addConnection(self, otherNode, action):
        self.connections.append((action, otherNode.getId()))

    def setVacuumPos(self, vacuumPos):
        self.vacuumPos = vacuumPos

    def setCells(self,cells):
        self.cells = cells

    def setIsGoal(self, isGoal):
        self.isGoal = isGoal

    def __str__(self):
        return (f"Node(id={self.id}, vacuum={self.vacuumPos}, "
                f"cells={self.cells}, goal={self.isGoal})")