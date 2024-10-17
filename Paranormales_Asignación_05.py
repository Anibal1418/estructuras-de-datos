from random import randrange

class Cola:
#Definir métodos que nos provean con las operaciones de la cola
    
    #1.Crea una cola vacía
    def __init__(self):
        self.data = []

    #2.Imprime la cola como una lista
    def __str__(self):
        return f"{self.data}"

    #3.Devuelve el contenido de la cola
    def __repr__(self):
        return " | ".join(map(str, self.data))

    #4.Devuelve el número de elementos de la cola
    def __len__(self):
        return len(self.data)
    
    #5.Añade un elemento a la cola
    def enqueue(self, e):
        self.data.append(e)

    #6.Extrae un elemento de la cola
    def dequeue(self):
        if self.isEmpty():
            raise IndexError('Cola vacía') #si la cola está vacía, lanza una excepción
        else:
            return self.data.pop(0)

    #7.Devuelve el primer elemento de la cola sin extraerlo
    def peek(self):
        if self.isEmpty():
            raise IndexError('Cola vacía')
        else:
            return self.data[0]

    #8.Devuelve True si la cola está vacía
    def isEmpty(self):
        return (self.data == [])
    
cola1 = Cola()
cola2 = Cola()
cola3 = Cola()

#No pueden haber más de 5 clientes en una fila a la vez
numMaxClientes = 5

while(True):
    try:
        numClientes = int(input("Provea el número de clientes que asistirán este día: "))
        if(numClientes < 0):
            raise ValueError
        break
    except:
        print("Asegúrese que el número de personas sea un número natural.")

for indiceCliente in range (numClientes):

    numEntrada = randrange(1, 4)
    while(True):
        if numEntrada == 1:
            if len(cola1) < numMaxClientes:
                cola1.enqueue(indiceCliente+1)
                print("Se añadió un cliente a la fila 1")
                break
            else:
                print("Fila 1 está llena, asignando cliente a otra fila...")
                numEntrada = randrange(2,4)
                continue
        elif numEntrada == 2:
            if len(cola2) < numMaxClientes:
                cola2.enqueue(indiceCliente+1)
                print("Se añadió un cliente a la fila 2")
                break
            else:
                print("Fila 2 está llena, asignando cliente a otra fila...")
                numEntrada = randrange(1,4,2)
                continue
        elif numEntrada == 3:
            if len(cola3) < numMaxClientes:
                cola3.enqueue(indiceCliente+1)
                print("Se añadió un cliente a la fila 3")
                break
            else:
                print("Fila 3 está llena, asignando cliente a otra fila...")
                numEntrada = randrange(1,3)
                continue

    print(f"Hay {len(cola1)} cliente{'s' if len(cola1) != 1 else ''} en la fila 1: {cola1}")
    print(f"Hay {len(cola2)} cliente{'s' if len(cola2) != 1 else ''} en la fila 2: {cola2}")
    print(f"Y hay {len(cola3)} cliente{'s' if len(cola3) != 1 else ''} en la fila 3: {cola3}")

    numSalida = randrange(1, 4)
    if numSalida == 1:
        try:
            print(f"Cliente {cola1.peek()} atendido en fila 1.\n")
            cola1.dequeue()
        except:
            print("Se intentó atender un cliente en la fila 1, pero está vacía.\n")
    elif numSalida == 2:
        try:
            print(f"Cliente {cola2.peek()} atendido en fila 2.\n")
            cola2.dequeue()
        except:
            print("Se intentó atender un cliente en la fila 2, pero está vacía.\n")
    elif numSalida == 3:
        try:
            print(f"Cliente {cola3.peek()} atendido en fila 3.\n")
            cola3.dequeue()
        except:
            print("Se intentó atender un cliente en la fila 3, pero está vacía.\n")

print("El día ha llegado a su fin y ya no se admieten más clientes, vaciando las filas restantes...")
while(not cola1.isEmpty()):
    print(f"Atendido cliente {cola1.peek()} en la fila 1")
    cola1.dequeue()
while(not cola2.isEmpty()):
    print(f"Atendido cliente {cola2.peek()} en la fila 2")
    cola2.dequeue()
while(not cola3.isEmpty()):
    print(f"Atendido cliente {cola3.peek()} en la fila 3")
    cola3.dequeue()
