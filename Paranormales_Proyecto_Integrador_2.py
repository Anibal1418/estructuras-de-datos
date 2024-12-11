''' Luis Sánchez 24-0057
La clase Interseccion representa un nodo en el grafo. 
Cada nodo tiene un identificador y una lista llamada conexiones,
que se utiliza para almacenar las aristas que están conectadas
a este nodo, en este caso, las Calles.
'''
class Interseccion:
    def __init__(self, id):
        self.id = id
        self.conexiones = []  
    
'''
La clase Calle representa una artista en el grafo. 
Cada arista conecta un nodo de origen y un nodo de destino, y almacena más información como su nombre,
y la distancia que cubre en kilómetros.
'''
class Calle:
    def __init__(self, name, origen, destino, kilometraje):
        self.name = name
        self.origen = origen
        self.destination = destino
        self.distancia = kilometraje
        self.conectar(origen, destino)

    def conectar(self, origen, destino):
        origen.conexiones.append(self)
        destino.conexiones.append(self)
        print(f"Calle '{self.name}' creada.")

'''
Estas son funciones independientes que manipulan nodos y calles
'''

# Función para confirmar conexión - Eduardo Alba 24-0050
def estaConectado(origen, destino):
    # Conjunto para llevar registro de nodos visitados
    visitados = set()

    # Función interna recursiva para realizar DFS simplificado optimizado para esta función
    def dfs_simpl(nodo_actual):
        if nodo_actual == destino:
            return True
        visitados.add(nodo_actual)
        for conexion in nodo_actual.conexiones:
            siguiente_nodo = conexion.destination if conexion.origen == nodo_actual else conexion.origen
            if siguiente_nodo not in visitados:
                if dfs_simpl(siguiente_nodo): # Llamada recursiva a la función dfs
                    return True
        return False

    # Iniciar DFS desde el nodo de origen
    return dfs_simpl(origen)

# Función DFS compleja e independiente, añade esa búsqueda a una lista llamada todos_los_camino - Luis Muñoz 24-0345
def DFS(nodo_actual, destino, visitados, camino_actual, todos_los_camino):
    visitados.add(nodo_actual)  # Marcar nodo actual como visitado
    camino_actual.append(nodo_actual)  # Agregar nodo al camino actual

    # Si llegamos al destino, guardamos el camino
    if nodo_actual == destino:
        if camino_actual not in todos_los_camino:
            todos_los_camino.append(camino_actual[:])  # Guardar una copia del camino actual
    else:
        # Explorar los nodos vecinos
        for conexion in nodo_actual.conexiones:
            # Determinar el siguiente nodo
            siguiente_interseccion = conexion.destination if conexion.origen == nodo_actual else conexion.origen
            # Si el siguiente nodo no ha sido visitado, explorarlo recursivamente
            if siguiente_interseccion not in visitados:
                DFS(siguiente_interseccion, destino, visitados, camino_actual, todos_los_camino)
                # Llamada recursiva a la función DFS

    # Retroceder (backtracking): desmarcar el nodo actual y eliminarlo del camino
    camino_actual.pop()  # Eliminar el nodo actual del camino
    visitados.remove(nodo_actual)  # Marcar el nodo actual como no visitado para ver otros caminos posibles

# Función para imprimir todos los caminos que unen una lista de nodos
# Alisha Núñez 24-0813
def imprimirCaminos(lista_de_nodos): #Toma una lista de nodos como la que retorna caminoMasCorto
    print("\nLos caminos que debe tomar para llegar más rápido a su destino son:")
    i = 1 #Iterador para analizar el nodo siguiente
    for nodo in lista_de_nodos: #Itera por cada nodo
        for camino in nodo.conexiones:
            if(i < len(lista_de_nodos)):
                #Si el nodo analizado y el nodo que le sigue son parte del mismo camino, imprimirlo
                if(camino.origen == nodo and camino.destination == lista_de_nodos[i]): 
                    print(camino.name)
                    break
                elif(camino.destination == nodo and camino.origen == lista_de_nodos[i]):
                    print(camino.name)
                    break
        i+=1
    
''' ESTA ES LA CLASE GPS. Básicamente es un diccionario de nodos accedidos por nombre.
Aquí es adonde se administran las funciones de nodos conectados, como búsqueda de caminos, cálculos de distancias, etc.
Luis Sánchez 24-0057'''

class GPS:

    def __init__(self):
        self.intersecciones = {}

    def __str__(self):
        return str(self.intersecciones)
    
    def agregarInterseccion(self, interseccion):
        if interseccion not in self.intersecciones:
            self.intersecciones[interseccion] = [interseccion.conexiones]
            print(f"Intersección '{interseccion.id}' agregada.")
        else:
            print(f"La intersección '{interseccion.id}' ya existe.")
        
    # Función para encontrar todos los caminos posibles entre dos nodos - Luis Muñoz 24-0345
    def encontrarCaminos(self, start, end):
        # Si no están conectados, no hay caminos posibles
        if not estaConectado(start, end):
            return []

        todos_los_caminos = []  # Lista para almacenar todos los caminos encontrados
        visitados = set()  # Conjunto para llevar el control de nodos visitados
        camino_actual = []  # Lista para almacenar el camino actual

        # Llamada inicial a dfs
        DFS(start, end, visitados, camino_actual, todos_los_caminos)
        return todos_los_caminos

    # Implementación de caminoMasCorto por Yordi Polanco 24-0937 y Alisha Núñez 24-0813
    def caminoMasCorto(self, inicio, final):

        # Obtener todos los caminos posibles entre start y end
        print(f"Buscando todos los caminos posibles entre {inicio.id} y {final.id}...")
        todo_camino = self.encontrarCaminos(inicio, final)

        # Si no hay caminos, devolver None
        if not todo_camino or self.isEmpty():  # Verificar si la lista de caminos está vacía, o el grafo en sí
            print(f"No se encontraron caminos entre {inicio.id} y {final.id}.")
            return None

        print(f"Se encontraron {len(todo_camino)} camino(s) entre {inicio.id} y {final.id}.")
        print("Caminos encontrados:")
        for camino in todo_camino:
            print(" -> ".join([i.id for i in camino]))

        # Inicializar variables para almacenar el camino más corto y su distancia
        camino_mas_corto = None  # Aquí almacenaremos el camino más corto encontrado
        distancia_mas_corta = float('inf')  # Se usa infinito como referencia inicial

        # Iterar sobre todos los caminos encontrados
        print("\nCalculando la distancia de cada camino...")
        for idx, camino in enumerate(todo_camino):
            distancia = 0  # Inicializar la distancia del camino actual

            # Calcular la distancia total del camino actual
            print(f"\nCamino {idx + 1}: {' -> '.join([i.id for i in camino])}")
            for i in range(len(camino) - 1):
                # Buscar la distancia entre nodos consecutivos en el camino
                for conexion in camino[i].conexiones:
                    # Verificar si la conexión une los nodos consecutivos
                    if conexion.destination == camino[i + 1] or conexion.origen == camino[i + 1]:
                        distancia += conexion.distancia  # Sumar la distancia de la calle
                        print(f"  - De {camino[i].id} a {camino[i + 1].id}: {conexion.distancia} km")
                        break  # Salir del bucle interno porque ya encontramos la conexión
            print(f"  Distancia total del camino {idx + 1}: {distancia} km")

            # Comparar la distancia actual con la más corta encontrada hasta ahora
            if distancia < distancia_mas_corta:
                distancia_mas_corta = distancia  # Actualizar la distancia más corta
                camino_mas_corto = camino  # Actualizar el camino más corto

        # Devolver el camino más corto y su distancia total
        print("\nEl camino más corto encontrado es:")
        print(" -> ".join([i.id for i in camino_mas_corto]))
        print(f"Distancia total: {distancia_mas_corta} km")
        return camino_mas_corto

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


'''Flujo del código y pruebas de debugging, Luis Sánchez 24-0057'''
gps = GPS()

# Aquí se definen las intersecciones y sus identificadores
interseccion_a = Interseccion("A")
interseccion_b = Interseccion("B")
interseccion_c = Interseccion("C")
interseccion_d = Interseccion("D")
interseccion_e = Interseccion("E")
interseccion_f = Interseccion("F")

# Agregando intersecciones, las calles se agregan con las intersecciones
gps.agregarInterseccion(interseccion_a)
gps.agregarInterseccion(interseccion_b)
gps.agregarInterseccion(interseccion_c)
gps.agregarInterseccion(interseccion_d)
gps.agregarInterseccion(interseccion_e)
gps.agregarInterseccion(interseccion_f)

# Aqui se definen las calles, sus nombres, longitudes, y qué conectan
calle_ab = Calle("Máximo Gómez", interseccion_a, interseccion_b, 14)
calle_bc = Calle("Gustavo Mejía Ricart", interseccion_b, interseccion_c, 7)

calle_ad = Calle("27 de Febrero", interseccion_a, interseccion_d, 25)
calle_bd = Calle("Calle Ramón Santana", interseccion_b, interseccion_d, 5)

calle_ef = Calle("Calle César Nicolas Penson", interseccion_e, interseccion_f, 12)

calle_de = Calle("Avenida Abraham Lincoln", interseccion_d, interseccion_e, 10)
calle_ce = Calle("Avenida México", interseccion_c, interseccion_e, 3)


# Y buscamos el camino más corto entre varios nodos de ejemplo
print("\n---------------------------EJEMPLO DE CONEXIÓN DIRECTA---------------------------")
imprimirCaminos(gps.caminoMasCorto(interseccion_a, interseccion_b))
print("------------------------------------------------------\n\n")
print("---------------------------EJEMPLO DE CONEXIÓN INDIRECTA CERCANA---------------------------")
imprimirCaminos(gps.caminoMasCorto(interseccion_a, interseccion_c))
print("------------------------------------------------------\n\n")
print("---------------------------EJEMPLO DE CONEXIÓN INDIRECTA LEJANA---------------------------")
imprimirCaminos(gps.caminoMasCorto(interseccion_a, interseccion_f))
print("------------------------------------------------------\n\n")
print("---------------------------EJEMPLO DE CONEXIÓN INDIRECTA LEJANA EN REVERSA---------------------------")
imprimirCaminos(gps.caminoMasCorto(interseccion_f, interseccion_a))
print("------------------------------------------------------\n\n")
