'''
La clase Interseccion representa un nodo en el grafo. 
Cada nodo tiene un valor (value) que puede ser cualquier tipo 
de dato (por ejemplo, una cadena de texto). 
Cada nodo también tiene una lista llamada conexiones,
que se utiliza para almacenar las aristas que están conectadas
a este nodo.
'''
class Interseccion:
    def __init__(self, id):
        self.id = id
        self.conexiones = []  
    
'''
La clase Calle representa una artista en el grafo. 
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
Esta son funciones independiente que manipulan nodos y calles
'''

# Conecta bilateralmente los nodos
def conectar(origen, calle, destino):
    if calle not in origen.conexiones:
        origen.conexiones.append(calle)
    if calle not in destino.conexiones:
        destino.conexiones.append(calle)

def estaConectado (origen, destino):
    # Primero chequea por conexion Directa
    for conexionA in origen.conexiones:
        if conexionA.destination == destino:
            return True
        elif conexionA.origen == destino:
            return True
    # En caso de que no estén conectados directamente, chequear por medio de DFS si algun camino lleva al nodo destino
    
    return False

# Función que calcula la distancia entre un nodo de origen y un nodo destino, hasta ahora solo hace un
# Chequeo superficial, necesitamos que haga un chequeo profundo en caso de que los dos nodos no estén conectados directamente
def calcDistancia (origen, destino):
    for conexionA in origen.conexiones: 
        if conexionA.destination == destino:
            return conexionA.distancia
        elif conexionA.origen == destino:
            return conexionA.distancia
    return None


# Ejemplo de Construcción
interseccion_a = Interseccion("A")
interseccion_b = Interseccion("B")
interseccion_c = Interseccion("C")

calle_ab = Calle("Máximo Gómez", interseccion_a, interseccion_b, 10)
calle_bc = Calle("Gustavo Mejía Ricart", interseccion_b, interseccion_c, 5)

# Añadir la arista tanto al nodo A como al nodo B
conectar(interseccion_a, calle_ab, interseccion_b)
conectar(interseccion_b, calle_bc, interseccion_c)

# Calcular la distancia entre dos intersecciones y las calles que las une
# Ambas deben imprimir 10, debido a que están conectadas por medio de arista de 10 de longitud
print(calcDistancia(interseccion_a, interseccion_b))
print(calcDistancia(interseccion_b, interseccion_a))


# ESTA ES LA CLASE GPS. Básicamente puede ser o una lista de nodos, o un diccionario de nodos accedidos por nombre.
# Aquí es adonde se van a administrar las funciones de nodos conectados, como búsqueda de caminos, cálculos de distancias, etc.

# Hasta ahora lo que hice fue crear un diccionario, donde cada intersección está colocada de la manera: {interseccion:[calles]}
class GPS:

    def __init__(self):
        self.intersecciones = {}

    def __str__(self):
        return str(self.intersecciones)
    
    def agregar(self, interseccion):
        if interseccion not in self.intersecciones:
            self.intersecciones[interseccion] = [interseccion.conexiones]
        
    '''CONSTRUIR una funcion que devuelva todos los caminos entre dos nodos'''
    # def findPaths(self, start, end):

    """A partir de la funcion anterior, construir una funcion que encuentre el camino mas corto entre dos intersecciones"""
    # camino más corto == menos nodos
    # def shortestPath(self, start, end):


    # Consulta si el grafo está vacío
    def isEmpty(self):
        return self.intersecciones == {}

    # Consulta si la interseccion existe en el grafo
    def existeInterseccion(self, interseccion):
        return interseccion in self.intersecciones

    # Consulta si la calle existe en el grafo
    def existeCalle(self, calle):
        for interseccion in self.intersecciones:
            for conexion in interseccion.conexiones:
                if(calle == conexion):
                    return True
        return False


gps = GPS()

gps.agregar(interseccion_a)
gps.agregar(interseccion_b)


# Estos statements de aquí abajo deberían imprimir true todos, pero el último imprime false ya que la función
# estaConectado no hace una búsqueda de profundidad
print(gps.existeInterseccion(interseccion_a))
print(gps.existeCalle(calle_ab))
print(estaConectado(interseccion_a, interseccion_b))
print(estaConectado(interseccion_b, interseccion_c))
print(estaConectado(interseccion_a, interseccion_c))
