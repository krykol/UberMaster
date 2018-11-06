from Nodes import Nodes
import random


listOfNodes = []  # lista do wpisywania obiektów klasy Nodes
connections = []  # lista ktora binarnie bedzie przechowywala czy istnieja polaczenia miedzy danymi wezlami czy nie

for i in range(0, 5):
    listOfNodes.append(Nodes(random.randint(1, 50), random.randint(1, 50)))

for i in range(0, len(listOfNodes)):
    connections.append(random.randint(0,1))

# for i in listOfNodes:
#     print(str(i.x_d) + '  y: ' + str(i.y_d))

for i in connections:
    print(i)