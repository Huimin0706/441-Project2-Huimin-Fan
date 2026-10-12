from itertools import product
from node import Node
from graph import Graph

class World:

    graph = None
    def __init__(self, num):
        # num is how many cells
        g = Graph()
        # in here, create your nodes
        # connect them to each other
        # and add them to the graph
        # object.  This will run in
        # the "main" of "interface.py"
        self._buildStateSpace(g, num)
        self.setGraph(g)

    def _buildStateSpace(self, g, num):
        stateLookup = {}
        nodeId = 0

        for vacuumPos in range(num):
            for cells in product(['D', 'C'], repeat=num):
                node = Node(
                    img=f"images/state_{nodeId}.png",
                    nodeId=nodeId,
                    vacuumPos=vacuumPos,
                    cells=cells
                )
                g.addNode(node)
                stateLookup[(vacuumPos, tuple(cells))] = nodeId
                nodeId += 1

        for node in g.getNodes():
            pos = node.getVacuumPos()
            cells = list(node.getCells())

            if cells[pos] == 'D':
                newCells = list(cells)
                newCells[pos] = 'C'
                targetId = stateLookup.get((pos, tuple(newCells)))
                if targetId is not None:
                    node.addConnection(g.getNode(targetId), 'Suck')

            if pos > 0:
                targetId = stateLookup.get((pos - 1, tuple(cells)))
                if targetId is not None:
                    node.addConnection(g.getNode(targetId), 'Left')

            if pos < num - 1:
                targetId = stateLookup.get((pos + 1, tuple(cells)))
                if targetId is not None:
                    node.addConnection(g.getNode(targetId), 'Right')

    def getGraph(self):
        return self.graph

    def setGraph(self, gr):
        if type(gr) == Graph:
            print('successfully initialized')
            self.graph = gr