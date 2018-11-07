from Node import Node
from Connections import Connections
import random



from ListOfNodes import ListOfNodes

listajakas = ListOfNodes(5000, 10000, 10000)


listajakas.showAllNodes()

polaczenia = Connections()

a = polaczenia.create_matrix(4,23)

print(a)

# listajakas.showX()
#
# print("Y \n\n")
#
# listajakas.showY()

