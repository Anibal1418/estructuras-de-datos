from collections import deque 

class Grafo(object):
    def __init__(self):
        self.relaciones = {}
    def __str__(self):
        return str(self.relaciones)
 
def agregar(grafo, elemento):
    grafo.relaciones.update({elemento:[]})

def relacionar(grafo, elemento1, elemento2):
    relacionarUnilateral(grafo, elemento1, elemento2)
    relacionarUnilateral(grafo, elemento2, elemento1)
   
def relacionarUnilateral(grafo, origen, destino):
    grafo.relaciones[origen].append(destino)

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

def anchoPrimero(grafo, elementoInicial, funcion, cola = deque(), elementosRecorridos = []):

    '''El primer paso es muy similar al anterior, con la diferencia de que en vez de retornar inmediatamente encuentre
    un objeto repetido, la función simplemente no va a ejecutar este bloque condicional, pero sí la última línea de código
    de la función.'''
    if not elementoInicial in elementosRecorridos:

        '''En segundo lugar, aplica la función al elemento en cuestión, igual a la función profundidadPrimero.'''
        funcion(elementoInicial)

        '''Agrega el elemento a la lista de Recorridos para asegurar que no pasemos por ahí otra vez.'''
        elementosRecorridos.append(elementoInicial)

        '''Aquí comienzan las diferencias principales. En esta functión, a parte de la lista de elementos Recorridos, creamos
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

def imprimir (elemento):
    print (elemento)


#Para crear el grafo, debemos primero inicializar el objeto y luego crear, agregar, y relacionar todos los elementos
#Por separado

grafo = Grafo() #Creamos objeto Grafo

#Inicializamos los elementos que vamos a añadir
A = 'A'
B = 'B'
C = 'C'
D = 'D'
E = 'E'

#Agregamos los elementos al grafo en orden alfabético
agregar(grafo, A)
agregar(grafo, B)
agregar(grafo, C)
agregar(grafo, D)
agregar(grafo, E)

#Relacionamos los elementos como se nos proveyó en la asignación
relacionar(grafo, A, B)
relacionar(grafo, A, C)
relacionar(grafo, B, D)
relacionar(grafo, B, E)

#Llamamos la función profundidadPrimero empezando por el primero elemento añadido (A) y llamando la función imprimir
print("========================================")
print("Recorremos Profundidad Primero")
print("========================================")
profundidadPrimero(grafo, A, imprimir)

''''''

#Llmamos la función anchoPrimero empezando por la misma A
print("========================================")
print("Recorremos Ancho Primero")
print("========================================")
anchoPrimero(grafo, A, imprimir)

''''''

#Como se puede observar, el resultado de ambas funciones es diferente, el por qué se explica más arriba.
