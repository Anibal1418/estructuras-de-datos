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
        conectar(origin, self, destination)

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

# Función DFS independiente fuera de la clase GPS - Luis Muñoz 24-0345
def dfs(nodo_actual, destino, visitados, camino_actual, todos_los_camino):
    visitados.add(nodo_actual)  # Marcar nodo actual como visitado
    camino_actual.append(nodo_actual)  # Agregar nodo al camino actual

    # Si llegamos al destino, guardamos el camino
    if nodo_actual == destino:
        todos_los_camino.append(camino_actual[:])  # Guardar una copia del camino actual
    else:
        # Explorar los nodos vecinos
        for conexion in nodo_actual.conexiones:
            # Determinar el siguiente nodo
            siguiente_interseccion = conexion.destination if conexion.origen == nodo_actual else conexion.origen
            # Si el siguiente nodo no ha sido visitado, explorarlo recursivamente
            if siguiente_interseccion not in visitados:
                dfs(siguiente_interseccion, destino, visitados, camino_actual, todos_los_camino)

    # Retroceder (backtracking): desmarcar el nodo actual y eliminarlo del camino
    camino_actual.pop()  # Eliminar el nodo actual del camino
    visitados.remove(nodo_actual)  # Marcar el nodo actual como no visitado para otros caminos posibles
    
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
    # Función para encontrar todos los caminos posibles entre dos nodos - Luis Muñoz 24-0345
    def findPaths(self, start, end):
        # Si no están conectados, no hay caminos posibles
        if not estaConectado(start, end):
            return []

        todos_los_camino = []  # Lista para almacenar todos los caminos encontrados
        visitados = set()  # Conjunto para llevar el control de nodos visitados
        camino_actual = []  # Lista para almacenar el camino actual

        # Llamada inicial a dfs
        dfs(start, end, visitados, camino_actual, todos_los_camino)
        return todos_los_camino

    # Implementación de shortestPath por Yordi Polanco | 24-0937
    def shortestPath(self, start, end):
        """
        Encuentra el camino más corto entre dos intersecciones usando todos los
        caminos posibles obtenidos por findPaths.
        """
        # Obtener todos los caminos posibles entre start y end
        print(f"Buscando todos los caminos posibles entre {start.id} y {end.id}...")
        all_paths = self.findPaths(start, end)

        # Si no hay caminos, devolver None
        if not all_paths:  # Verificar si la lista de caminos está vacía
            print(f"No se encontraron caminos entre {start.id} y {end.id}.")
            return None

        print(f"Se encontraron {len(all_paths)} camino(s) entre {start.id} y {end.id}.")
        print("Caminos encontrados:")
        for path in all_paths:
            print(" -> ".join([i.id for i in path]))

        # Inicializar variables para almacenar el camino más corto y su distancia
        shortest_path = None  # Aquí almacenaremos el camino más corto encontrado
        shortest_distance = float('inf')  # Se usa infinito como referencia inicial

        # Iterar sobre todos los caminos encontrados
        print("\nCalculando la distancia de cada camino...")
        for idx, path in enumerate(all_paths):
            distance = 0  # Inicializar la distancia del camino actual

            # Calcular la distancia total del camino actual
            print(f"Camino {idx + 1}: {' -> '.join([i.id for i in path])}")
            for i in range(len(path) - 1):
                # Buscar la distancia entre nodos consecutivos en el camino
                for conexion in path[i].conexiones:
                    # Verificar si la conexión une los nodos consecutivos
                    if conexion.destination == path[i + 1] or conexion.origen == path[i + 1]:
                        distance += conexion.distancia  # Sumar la distancia de la calle
                        print(f"  - De {path[i].id} a {path[i + 1].id}: {conexion.distancia} km")
                        break  # Salir del bucle interno porque ya encontramos la conexión
            print(f"  Distancia total del camino {idx + 1}: {distance} km")

            # Comparar la distancia actual con la más corta encontrada hasta ahora
            if distance < shortest_distance:
                print(f"  -> Este es el camino más corto hasta ahora.")
                shortest_distance = distance  # Actualizar la distancia más corta
                shortest_path = path  # Actualizar el camino más corto

        # Devolver el camino más corto y su distancia total
        print("\nEl camino más corto encontrado es:")
        print(" -> ".join([i.id for i in shortest_path]))
        print(f"Distancia total: {shortest_distance} km")
        return shortest_path, shortest_distance
    # Fin de la sección desarrollada por Yordi Polanco | 24-0937

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

interseccion_a = Interseccion("A")
interseccion_b = Interseccion("B")
interseccion_c = Interseccion("C")
interseccion_d = Interseccion("D")
interseccion_e = Interseccion("E")
interseccion_f = Interseccion("F")

calle_ab = Calle("Máximo Gómez", interseccion_a, interseccion_b, 10)
calle_bc = Calle("Gustavo Mejía Ricart", interseccion_b, interseccion_c, 5)

calle_ad = Calle("27 de Febrero", interseccion_a, interseccion_d, 25)
calle_bd = Calle("Gustavo Mejía Ricart", interseccion_b, interseccion_c, 5)

calle_ae = Calle("Avenida México", interseccion_a, interseccion_e, 7)
calle_ef = Calle("Calle César Nicolas Penson", interseccion_e, interseccion_f, 12)

calle_bf = Calle("Avenida Roberto Pastoriza", interseccion_b, interseccion_f, 15)
calle_de = Calle("Avenida Abraham Lincoln", interseccion_d, interseccion_e, 10)
calle_ce = Calle("Calle Ramón Santana", interseccion_c, interseccion_e, 3)


# Calcular la distancia entre dos intersecciones y las calles que las une
# Ambas deben imprimir 10, debido a que están conectadas por medio de arista de 10 de longitud
print(calcDistancia(interseccion_a, interseccion_b))
print(calcDistancia(interseccion_b, interseccion_a))

gps.agregar(interseccion_a)
gps.agregar(interseccion_b)
gps.agregar(interseccion_c)
gps.agregar(interseccion_d)
gps.agregar(interseccion_e)
gps.agregar(interseccion_f)


# Estos statements de aquí abajo deberían imprimir true todos, pero el último imprime false ya que la función
# estaConectado no hace una búsqueda de profundidad
print(gps.existeInterseccion(interseccion_a))
print(gps.existeCalle(calle_ab))
print(gps.existeCalle(calle_bc))
print(estaConectado(interseccion_a, interseccion_b))
print(estaConectado(interseccion_b, interseccion_c))
print(estaConectado(interseccion_a, interseccion_c))

gps.shortestPath(interseccion_a, interseccion_b)
gps.shortestPath(interseccion_b, interseccion_f)
gps.shortestPath(interseccion_d, interseccion_e)
gps.shortestPath(interseccion_a, interseccion_c)