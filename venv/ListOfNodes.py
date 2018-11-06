
# musimy się zastanowić, czy nie lepiej dodać taką klasę, miałaby ona funkcjonalność zwykłej tablicy, lecz dodatkwoo
# sprawdzała by nam, czy przypadkiem nie dodajemy istniejącego już puntu
import random
from Node import Node
class ListOfNodes():
    def __init__(self, size = 50, x_range = 100, y_range = 100):
        x_table = []
        y_table = []

        nodes_table = []


        while x_table.__len__() < size:
            x_temp = random.randint(x_range)
            y_temp = random.randint(y_range)

            if x_temp in x_table and y_temp in y_table:
                continue
            else:
                nodes_table.append(Node)

