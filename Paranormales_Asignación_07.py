'''Escriba un programa en Python que incluya una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone, 
de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje, para resolver las siguientes actividades:

1. escribir una función que elimine de la cola todas las notificaciones de Facebook;
2. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra ‘Python’, si perder datos en la cola;
3. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57, y determinar cuántas son'''

class ColaNotificaciones:

    # Construye una cola vacía
    def __init__(self):
        self.data = []

    # Representa el contenido de la cola
    def __repr__(self):
        return " | ".join(map(str, self.data))

    # Devuelve la longitud o número de elementos de la cola
    def __len__(self):
        return len(self.data)
    
    # Añade un elemento a la cola
    def enqueue(self, e):
        self.data.append(e)

    # Extrae y elimina un elemento de la cola
    def dequeue(self):
        if self.isEmpty(): # Sube un error en caso de que esté vacía
            raise IndexError('Cola vacía')
        else:
            return self.data.pop(0)

    # Devuelve el primer elemento de la cola sin eliminarlo
    def peek(self):
        if self.isEmpty():
            raise IndexError('Cola vacía')
        else:
            return self.data[0]

    # Devuelve True si la cola está vacía
    def isEmpty(self):
        return self.data == []
