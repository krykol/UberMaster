# musimy się zastanowić, czy nie lepiej dodać taką klasę, miałaby ona funkcjonalność zwykłej tablicy, lecz dodatkwoo
# sprawdzała by nam, czy przypadkiem nie dodajemy istniejącego już puntu
import random
from Node import Node


class ListOfNodes:
    def __init__(self, size = 50, x_range = 100, y_range = 100):
        self.x_table = []
        self.y_table = []
        self.nodes_table = []


        while self.x_table.__len__() < size:
            x_temp = random.randint(0, x_range)
            y_temp = random.randint(0, y_range)
            if x_temp in self.x_table:
                if y_temp in self.y_table:
                    continue
            else:
                self.x_table.append(x_temp)
                self.y_table.append(y_temp)
                #print("X: ", x_temp, " Y: ", y_temp)   #sprawdzenie jakie liczby nam się tam pojawiają

        temp = 0

        for x in self.x_table:
            self.nodes_table.append(Node(x, self.y_table[temp]))
            temp+=1


    def showAllNodes(self):
        temp = 1
        for i in self.nodes_table:
            print("Node number: "+ str(temp) + i.__str__())
            temp += 1

    def showX(self):
        for i in self.x_table:
            print(i)

    def showY(self):
        for i in self.y_table:
            print(i)