from collections import deque 

'''
Clase Grafo:
Un grafo es una estructura que conecta elementos (nodos) a través de relaciones (aristas). 
Aquí usamos un diccionario donde las claves son los nodos, y los valores son listas de sus vecinos.
'''

class Grafo(object):
    def __init__(self):
        self.relaciones = {}
    def __str__(self):
        return str(self.relaciones)
    
'''
Función para agregar nodos:
Cuando queremos incluir un nuevo nodo en el grafo, lo añadimos al diccionario con una lista vacía como valor. 
Esto significa que, inicialmente, el nodo no tiene vecinos.
'''
 
def agregar(grafo, elemento):
    grafo.relaciones.update({elemento:[]})

'''
Función para conectar nodos (relacionar):
Crea una relación entre dos nodos. Esta relación es bidireccional: 
si A está conectado a B, también B estará conectado a A.
'''

def relacionar(grafo, elemento1, elemento2):
    relacionarUnilateral(grafo, elemento1, elemento2)
    relacionarUnilateral(grafo, elemento2, elemento1)

'''
Función auxiliar para una conexión unilateral:
Sólo añade un vecino a la lista del nodo origen.
'''
   
def relacionarUnilateral(grafo, origen, destino):
    grafo.relaciones[origen].append(destino)

<<<<<<< HEAD
'''
Recorrido en profundidad primero (DFS): Yordi Polanco 24-0937
=======
''' Yordi Polanco 24-0937
Recorrido en profundidad primero (DFS):
>>>>>>> 59ba842252fa3dbe419106ed5c89fa3a47ddb648
Este algoritmo explora lo más lejos posible desde un nodo inicial antes de retroceder. 
Se asegura de no visitar nodos repetidos para evitar ciclos infinitos.
'''

def profundidadPrimero(grafo, elementoInicial, funcion, elementosRecorridos = []):

    '''Primero que todo, la función chequea si el elemento en cuestión ya ha sido recorrido. Si es así, la función
    retorna inmediatamente y no ejecuta ningún otro código relevante.'''
    if elementoInicial in elementosRecorridos:
        return

    '''En segundo lugar, aplica la función deseada al elemento en cuestión.'''
    funcion(elementoInicial)

    '''En tercer lugar, añade el elemento en cuestión a la lista de elementosRecorridos, de manera que si pasamos
    por ese elemento otra vez, la función va a retornar inmediatamente llegue al primer paso.'''
    elementosRecorridos.append(elementoInicial)
    
    '''El nombre profundidad primero viene de esto. Básicamente, la función chequea recursivamente cada vecino del elemento inicial
    con el que se está ejecutando, pero antes de pasar al siguiente vecino del elemento inicial, la función va a 
    recurrirse con todos los vecinos del vecino antes de retornar al elemento original. A esto se refiere con
    recorriendo el Grafo en "profundidad", ya que limpia cada "rama" del elemento en cuestión antes de pasar a la próxima.'''
    
    for vecino in grafo.relaciones[elementoInicial]:
        profundidadPrimero(grafo, vecino, funcion, elementosRecorridos)

'''Recorrido en ancho primero (BFS): Eduardo Alba 24-0050'''

def anchoPrimero(grafo, elementoInicial, funcion, cola = deque(), elementosRecorridos = []):

    '''El primer paso es muy similar al anterior, con la diferencia de que en vez de retornar inmediatamente encuentre
    un objeto repetido, la función simplemente no va a ejecutar este bloque condicional, pero sí la última línea de código
    de la función. Yordi Polanco 24-0937'''
    if not elementoInicial in elementosRecorridos:

        '''Después, aplica la función al elemento en cuestión, igual a la función profundidadPrimero.'''
        funcion(elementoInicial)

        '''Agrega el elemento a la lista de Recorridos para asegurar que no pasemos por ahí otra vez.'''
        elementosRecorridos.append(elementoInicial)

        '''Aquí comienzan las diferencias principales. En esta función, a parte de la lista de elementos Recorridos, creamos
        una cola, en la cual estamos añadiendo todos los vecinos de cada elemento a partir del método extend. Este código
        hace un chequeo condicional de que el elemento tenga relaciones en primer lugar, y luego las añade todas en el orden
        en el que están al mismo tiempo.'''
        if(len(grafo.relaciones[elementoInicial]) > 0):
            cola.extend(grafo.relaciones[elementoInicial])

    '''Aquí es donde la función más se diferencia. Primero chequea que la cola extendida con los elementos no esté vacía,
    después ejecuta recursivamente la misma función con cada elemento de la cola en el orden FIFO como es característica de esta,
    usando el método popleft para ejecutar la función con todos sus elementos hasta vaciarlos.
    Esto hace que la función se ejecuta primero con todos los vecinos inmediatos del elemento inicial, antes de pasar al
    siguiente, y es por esto que se gana su nombre de "Ancho Primero".'''
    if len(cola) != 0 :
        anchoPrimero(grafo, cola.popleft(), funcion, cola, elementosRecorridos) 
    #Este código se ejecuta sin importar si el elemento ya ha sido recorrido o no, asegurándose que todos los vecinos
    #De cada uno de los elementos sean chequeados, lo cual puede hacer el código más lento pero más preciso.


'''
Función para imprimir el nodo:
Simplemente muestra el nodo actual en la consola.
'''
def imprimir (elemento):
    print (elemento)


#Para crear el grafo, debemos primero inicializar el objeto y luego crear, agregar, y relacionar todos los elementos por separado.

grafo = Grafo() #Creamos objeto Grafo.

#Inicializamos los elementos que vamos a añadir.
A = 'A'
B = 'B'
C = 'C'
D = 'D'
E = 'E'

#Agregamos los elementos al grafo en orden alfabético.
agregar(grafo, A)
agregar(grafo, B)
agregar(grafo, C)
agregar(grafo, D)
agregar(grafo, E)

#Relacionamos los elementos como se nos proveyó en la asignación.
relacionar(grafo, A, B)
relacionar(grafo, A, C)
relacionar(grafo, B, D)
relacionar(grafo, B, E)

#Llamamos la función profundidadPrimero empezando por el primero elemento añadido (A) y llamando la función imprimir.
print("========================================")
print("Recorremos Profundidad Primero")
print("========================================")
profundidadPrimero(grafo, A, imprimir)

''' Explicación del recorrido función profundidadPrimero Luis Sánchez 24-0057
Siguiendo la lógica explicada más arriba, esta función se ejecuta de la siguiente manera: 
Primero se ejecuta con el elemento inicial A y aplica la función imprimir a este.
Luego itera por sus vecinos empezando por el B que fue el primero con el que se relacionó y lo imprime en la terminal.
Pero antes de pasar con el segundo vecino de A (C) la función chequea por los demás vecinos de B, que en este caso son D y E
Empezando por D, la función se ejecuta y lo imprime a la terminal, y luego chequea por los vecinos de D.
Ya que todos los vecinos de D (que en este caso es solo B) ya han sido chequeados, la función simplemente retorna.
Luego pasamos al otro vecino de B (E) y lo imprime a la terminal, luego ejecutando un proceso similar.
Después de terminar con los vecinos de B, la función vuelve a donde empezamos, A, y termina imprimiendo su último vecino C.
Ya la función no debe preocuparse de más objetos por que ya todos han sido iterados, y la función retorna.'''

#Llamamos la función anchoPrimero empezando por la misma A.
print("========================================")
print("Recorremos Ancho Primero")
print("========================================")
anchoPrimero(grafo, A, imprimir)

''' Explicación del recorrido función anchoPrimero Luis Sánchez 24-0057
Considerando la lógica explicada con anterioridad, la función anchoPrimero se ejecuta así:
Empieza con A y lo imprime, luego añade todos sus vecinos inmediatos a la cola y los va ejecutando uno a uno.
Los vecinos inmediatos de A son B y C, por lo que los termina imprimiendo primero y vacía la cola.
Después la función iría por los elementos B y C, pero ya estos han sido impresos y añadidos a la lista de elementosRecorridos,
por lo que la función los ignora.
La única relación de los elementos D y E es B así que por más que añadan a B a la cola, este no va a imprimirse ni ejecutarse.
La función termina imprimiendo D y E de manera natural, y finalmente retorna.'''

#Como se puede observar, el resultado de ambas funciones es diferente, el por qué se explica más arriba.


# Resumen de funcion Ancho Primera Alisha Nunez 24-0813
# La función de recorrido en anchura (BFS), implementada aquí como anchoPrimero, explora un grafo de manera 
# que primero visita todos los nodos vecinos inmediatos del nodo inicial antes de avanzar hacia los vecinos de esos nodos. 
# Utiliza una cola (deque) para gestionar los nodos pendientes de visitar, asegurando que se procesan en orden FIFO 
# (primero en entrar, primero en salir). A diferencia del recorrido en profundidad (DFS), que prioriza explorar lo más 
# profundo posible antes de retroceder, BFS expande su búsqueda horizontalmente, lo que lo hace útil para encontrar el 
# camino más corto en grafos no ponderados. En este código, la función asegura que cada nodo sea procesado solo una vez 
# mediante una lista de nodos recorridos, evitando visitas redundantes o bucles infinitos en grafos cíclicos.

# Resumen de funcion Profundidad Primera Luis Munoz 24-0345
# Esta función implementa un recorrido en profundidad (Depth-First Search, DFS) en un grafo. Comienza en un nodo inicial
# y explora recursivamente cada uno de sus vecinos antes de pasar al siguiente. Primero verifica si el nodo ya ha sido
# recorrido, en cuyo caso termina el procesamiento para ese nodo. Si no, ejecuta una función específica sobre el nodo,
# lo marca como visitado añadiéndolo a una lista de elementos recorridos, y luego procede a explorar sus vecinos.
# Este enfoque garantiza que cada rama del grafo se recorre completamente antes de regresar al nodo original.
