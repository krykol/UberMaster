import random
import numpy as np

# klasa odpowiadajaca za tworzenie macierzy wypelnionej binarnie
# aby zbudować listę połączeń między miastami,
# musimy potem sprawdzić czy drzewo jest pełne i je wyizolować
class Connections:
    def createMatrix(self, m):
        return np.ones(m, m)

    def fillMatrixWithRandom(self, matrix, size_of_array):
        for y in range(0, size_of_array):
            for x in range(0, size_of_array):
                if y < x:
                    matrix[y, x] = random.randint(0, 1)
                else:
                    matrix[y, x] = 8









