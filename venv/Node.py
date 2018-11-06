class Node:
    def __init__(self, x_d, y_d):
        self.x_d = x_d
        self.y_d = y_d

    def __str__(self):
        return " \tX: " +"\t" +str(self.x_d) + " \tY: " + str(self.y_d)
