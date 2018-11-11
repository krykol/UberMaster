import random
import numpy as np

# klasa odpowiadajaca za tworzenie macierzy wypelnionej binarnie
# aby zbudować listę połączeń między miastami,
# musimy potem sprawdzić czy drzewo jest pełne i je wyizolować
class Connections:
    def __init__(self, size):
        # self.size_of_matrix = size
        # self.matrix = self.create_matrix(size)
        # self.matrix = self.fill_matrix_with_random(self.matrix, self.size_of_matrix)

        self._matrix = np.ones((size,size))

        self._matrix = self.fill_matrix_with_random(self._matrix, size+1)
        self._matrix = self.add_weigths_to_matrix(self._matrix, size, 0, 100)
        print(self._matrix)

    def create_matrix(self, m):
        return np.ones(m, m)

    def fill_matrix_with_random (self, matrix, size_of_matrix):
        for y in range(0, size_of_matrix-1):
            for x in range(0, size_of_matrix-1):
                if y < x:
                    matrix[y, x] = random.randint(0, 1)
                else:
                    matrix[y, x] = 8
        return matrix

    def add_weigths_to_matrix(self, matrix, size_of_matrix, lower_limit, upper_limit):

        for y in range(0, size_of_matrix-1):
            for x in range(0, size_of_matrix-1):
                if matrix[y,x] == 1:
                    matrix[y,x] += (matrix[y,x] + random.randint(lower_limit, upper_limit))

        return matrix









