import matplotlib.pyplot as plt
from ListOfNodes import ListOfNodes



listOfNodes = ListOfNodes(500, 1000000, 1000000)


plt.plot(listOfNodes.retXTable(), listOfNodes.retYTable(),'ro')

plt.show()


print(listOfNodes.retXTable())