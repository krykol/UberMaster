import random as rd

class Node:
    nodeID = 1
    def __init__(self, x_d, y_d, nodeID, numOfAllNodes):
        self.limOfConnections = 5                                   # we have up to 5 hook-up's
        self.nodeID = nodeID
        self.x_d = x_d
        self.y_d = y_d
        self.pobabilityOfProfit = (rd.randint(0,100) / 100)         # this is the probability of making the profit in this node

        if rd.randint(0,1000) > 900:                                # this is info if we do have gas station in the node, there is 105 chance that we do have gas station in the node
            self.gasStation = True
        else:
            self.gasStation = False                                 # ciekawostka, bool(rd.getrandombit(1)) byłoby około 2 razy szybsze od rd.randint(0,1)

        # we need to have list of the node's ID that we are connected with
        self.listOfConnections = []

        for i in range(0, rd.randint(1, self.limOfConnections)):
            self.listOfConnections.append(rd.randint(numOfAllNodes))






        # prawdopodobieństwo wystąpienia klienta
        # prawdopodobieństwo gdzie jedzie


    def __str__(self):
        return "Node ID: "+str(self.nodeID) + "\tX: " +"\t" +str(self.x_d) + " \tY: " + str(self.y_d)

    def XandY(self):
        return self.x_d, self.y_d

    def getX(self):
        return self.x_d

    def getY(self):
        return self.y_d

    def retIDOfConnectedNodes(self):
        return self.listOfConnections