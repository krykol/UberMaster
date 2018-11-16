from Node import Node
import random


listOfNodes = []    # lista do wpisywania obiektów klasy Nodes, będą współrzędne miejsc z których możemy przewozić ludzi.
connections = []    # lista ktora binarnie bedzie przechowywala czy istnieja polaczenia miedzy danymi wezlami czy nie

weights = []        # tablica w której jeśli istnieje połączenie między dwoma punktami to generowana jest "waga"
                    # (może to być np. koszt)

# zakładamy koszt z przedziału od 0-100?

while listOfNodes.__len__() < 51:   #musi być while, bo możliwe, że 50 razy trafimy na te same punky i wtedy dupa xd

    # musimy sprawdzać czy nie utworzyliśmy istniejącego już punktu, jeśli tak to nie dodajemy go do tablicy
    x_d = random.randint(1,100)
    y_d = random.randint(1,100)



    listOfNodes.append(Nodes(random.randint(1, 50), random.randint(1, 50)))

for i in listOfNodes:
    for j in listOfNodes:
        if i == j:
            continue




# for i in listOfNodes:
#     print(str(i.x_d) + '  y: ' + str(i.y_d))

for i in connections:
    print(i)