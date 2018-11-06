from Nodes import Nodes
import random

listOfNodes = []  # lista do wpisywania obiektów klasy Nodes, będą współrzędne miejsc z których możemy przewozić ludzi.
connections = []  # lista ktora binarnie bedzie przechowywala czy istnieja polaczenia miedzy danymi wezlami czy nie

weights = []  # tablica w której jeśli istnieje połączenie między dwoma punktami to generowana jest "waga"
# (może to być np. koszt)

# zakładamy koszt z przedziału od 0-100?

for i in range(0, 50):
    listOfNodes.append(Nodes(random.randint(1, 50), random.randint(1, 50)))

print(listOfNodes.__len__())