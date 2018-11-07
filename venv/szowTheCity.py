import matplotlib.pyplot as plt
from ListOfNodes import ListOfNodes



listOfNodes = ListOfNodes(50, 10000, 10000)


plt.plot(listOfNodes.retXTable(), listOfNodes.retYTable(),'ro')

plt.show()


print(listOfNodes.retXTable())