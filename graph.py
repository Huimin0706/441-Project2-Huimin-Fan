from collections import deque

from node import Node

class Graph:
    '''
    nodes: the list of nodes, these should be node objects
    '''
    nodes = []

    def __init__(self):
        self.nodes = []

    def addNode(self, node):
        self.nodes.append(node)

    def getNodes(self):
        return self.nodes

    def getNode(self, nodeId):
        for n in self.nodes:
            if n.getId() == nodeId:
                return n
        return None

    def addEdge(self, sourceId, destId):
        sourceNode = self.getNode(sourceId)
        destNode = self.getNode(destId)
        if sourceNode is not None and destNode is not None:
            sourceNode.addConnection(destNode, 'Edge')

    def bfs(self, startId):
        ##BREADTH FIRST SEARCH
        startNode = self.getNode(startId)
        if startNode is None:
            return []

        if startNode.getIsGoal():
            return [startId]

        frontier = deque()
        frontier.append((startId, [startId]))
        visited = {startId}

        while frontier:
            currentId, path = frontier.popleft()
            currentNode = self.getNode(currentId)

            for action, neighborId in currentNode.getConnections():
                if neighborId in visited:
                    continue
                visited.add(neighborId)

                newPath = path + [neighborId]
                neighborNode = self.getNode(neighborId)

                if neighborNode.getIsGoal():
                    return newPath

                frontier.append((neighborId, newPath))

        return []

    def dfs(self, startId):
        ##DEPTH FIRST SEARCH
        startNode = self.getNode(startId)
        if startNode is None:
            return []

        if startNode.getIsGoal():
            return [startId]

        frontier = []
        frontier.append((startId, [startId]))
        visited = {startId}

        while frontier:
            currentId, path = frontier.pop()
            currentNode = self.getNode(currentId)

            for action, neighborId in currentNode.getConnections():
                if neighborId in visited:
                    continue
                visited.add(neighborId)

                newPath = path + [neighborId]
                neighborNode = self.getNode(neighborId)

                if neighborNode.getIsGoal():
                    return newPath

                frontier.append((neighborId, newPath))

        return []

    def __str__(self):
        lines = ["Graph:"]
        for n in self.nodes:
            lines.append("  " + str(n))
            for action, destId in n.getConnections():
                lines.append(f"    --[{action}]--> {destId}")
        return "\n".join(lines)