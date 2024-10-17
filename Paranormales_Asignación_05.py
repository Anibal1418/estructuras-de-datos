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
cola1.enqueue(1)
print(cola1)
print(repr(cola1))
print(len(cola1))
