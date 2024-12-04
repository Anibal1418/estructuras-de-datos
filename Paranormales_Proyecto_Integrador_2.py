'''
La clase Node representa un nodo en el grafo. 
Cada nodo tiene un valor (value) que puede ser cualquier tipo 
de dato (por ejemplo, una cadena de texto). 
Cada nodo también tiene una lista llamada connections,
que se utiliza para almacenar los bordes que están conectados
a este nodo.
'''
class Interseccion:
    def __init__(self, id):
        self.id = id
        self.conexiones = []
    
def calcDistancia (origen, destino):
    for conexionA in origen.conexiones: 
        if conexionA.destination == destino:
            return conexionA.distancia
        elif conexionA.origen == destino:
            return conexionA.distancia
    return None
    
'''
La clase Edge representa una artista en el grafo. 
Cada arista tiene dos partes: un nodo de origen (origin) 
y un nodo de destino (destination), lo que significa que  
la arista va desde el nodo de origen hasta el nodo de destino.
'''
class Calle:
    def __init__(self, name, origin, destination, kilometraje):
        self.name = name
        self.origen = origin
        self.destination = destination
        self.distancia = kilometraje

'''
Se debe buscar una manera para interrelacionar estas clases de manera que sean parte de un solo grafo llamado GPS
en el cual podemos hacer funciones de búsqueda y conexión.
'''

# Ejemplo de Construcción
interseccion_a = Interseccion("A")
interseccion_b = Interseccion("B")

calle_ab = Calle("Máximo Gómez", interseccion_a, interseccion_b, 10)

# Añadir la arista tanto al nodo A como al nodo B
interseccion_a.conexiones.append(calle_ab)
interseccion_b.conexiones.append(calle_ab)

# Calcular la distancia de la calle común que tienen both ways
print(calcDistancia(interseccion_a, interseccion_b))
print(calcDistancia(interseccion_b, interseccion_a))


# Draft de clase que podría agregar grafos y aristas

class GPS:

    def __init__(self):
        self.intersecciones = []

    def __str__(self):
        return str(self.intersecciones)
    
    def agregar(self, interseccion):
        self.intersecciones.append(interseccion)


gps = GPS()

gps.agregar(interseccion_a)
gps.agregar(interseccion_b)
