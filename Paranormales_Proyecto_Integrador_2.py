'''
La clase Node representa un nodo en el grafo. 
Cada nodo tiene un valor (value) que puede ser cualquier tipo 
de dato (por ejemplo, una cadena de texto). 
Cada nodo también tiene una lista llamada connections,
que se utiliza para almacenar los bordes que están conectados
a este nodo.
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.connections = []

'''
La clase Edge representa una artista en el grafo. 
Cada arista tiene dos partes: un nodo de origen (origin) 
y un nodo de destino (destination), lo que significa que  
la arista va desde el nodo de origen hasta el nodo de destino.
'''
class Edge:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination

'''
Se debe buscar una manera para interrelacionar estas clases de manera que sean parte de un solo grafo llamado GPS
en el cual podemos hacer funciones de búsqueda y conexión.
'''

# Ejemplo de Construcción
node_a = Node("A")
node_b = Node("B")

edge_ab = Edge(node_a, node_b)

# Añadir la arista tanto al nodo A como al nodo B
node_a.connections.append(edge_ab)
node_b.connections.append(edge_ab)

# Draft de clase que podría agregar grafos y aristas

class Grafo(object):
    def __init__(self):
        self.relaciones = {}

def __str__(self):
    return str(self.relaciones)
 
def agregar(grafo, nodo):
    grafo.relaciones.update({nodo:[]})

def relacionar(grafo, elemento1, elemento2):
    relacionarUnilateral(grafo, elemento1, elemento2)
    relacionarUnilateral(grafo, elemento2, elemento1)
   
def relacionarUnilateral(grafo, origen, destino):
    grafo.relaciones[origen].append(destino)
