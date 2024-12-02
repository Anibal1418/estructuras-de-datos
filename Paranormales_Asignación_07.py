class ColaNotificaciones:

    # Construye una cola vacía
    def __init__(self):
        self.notis = []
        self.pila_temp = [] # Pila para notificaciones temporales - Agregado por Yordi Polanco 24-0937

    #- Eduardo Alba 24-0050
    # Representa el contenido de la cola para imprimir
    def __repr__(self):
        if not self.notis:
            return "La cola está vacía."
        resultado = "\n"
        for noti in self.notis:
            resultado += f"[{noti['hora']}] {noti['aplicación']}: {noti['mensaje']}\n"
        return resultado.strip()  


    # Devuelve la longitud o número de elementos de la cola
    def __len__(self):
        return len(self.notis)
    
    # Añade un elemento a la cola - Aquí comienza el trabajo de Yordi Polanco 24-0937 and Alisha Nunez 24-0813
    def enqueue(self, time, app, message):
        # Convertir la hora a minutos para facilitar la comparación
        def hora_a_minutos(hora):
            horas, minutos = map(int, hora.split(':'))
            return horas * 60 + minutos

        noti = {"hora": time, "aplicación": app, "mensaje": message}
        self.notis.append(noti)

        # Verificar y almacenar en la pila temporal si está entre 11:43 y 15:57
        hora_actual = hora_a_minutos(time)
        hora_inicio = hora_a_minutos("11:43")
        hora_fin = hora_a_minutos("15:57")

        if hora_inicio <= hora_actual <= hora_fin:
            self.pila_temp.append(noti)

    # Método para mostrar las notificaciones almacenadas temporalmente
    def mostrar_notificaciones_temporales(self):
        print("Notificaciones entre 11:43 y 15:57:")
        for noti in reversed(self.pila_temp):
            print(f"[{noti['hora']}] {noti['aplicación']}: {noti['mensaje']}")
        print(f"Total de notificaciones en este rango: {len(self.pila_temp)}") 
        
    # Aquí termina el trabajo de Yordi Polanco 24-0937 and Alisha Nunez 24-0813

    # Devuelve el primer elemento de la cola sin eliminarlo
    def peek(self):
        if self.isEmpty():
            raise IndexError('Cola vacía')
        else:
            return self.notis[0]

    # Devuelve True si la cola está vacía
    def isEmpty(self):
        return self.notis == []
    
    # Luis Sánchez 24-0057
    # Implementación del primer ejercicio, función que borra todas las notificaciones de Facebook
    def borrarNotisFacebook(self):

        ilist = [] # Crea una lista que almacenará los índices de mensajes que provienen de Facebook
        for i in range(0, self.__len__()):
            if(self.notis[i]["aplicación"] == "Facebook"):
                ilist.append(i)

        # Elimina los elementos en los índices almacenados en modo reversa para que no nos dé un IndexError
        for element in reversed(ilist):
            self.notis.pop(element)

    # Luis Sánchez 24-0057
    # Implementación del segundo ejercicio, función que muestra las notificaciones de Twitter con "Python" en su mensaje
    def verNotisTwitter(self):
        temp = ColaNotificaciones() # Crear cola temporal
        for i in range (0, self.__len__()): # Por cada mensaje que venga de la aplicación "Twitter" y tenga "Python" en su mensaje
            if(self.notis[i]["aplicación"] == "Twitter" and ("Python" in self.notis[i]["mensaje"])):
                temp.enqueue(self.notis[i]["hora"], self.notis[i]["aplicación"], self.notis[i]["mensaje"]) # Añadirlo a la cola temporal
        print(temp) # Imprimir la cola temporal

 #- Luis Muñoz 24-0345 and Alisha Nunez 24-0813
cola = ColaNotificaciones()

# Conjunto de notificaciones
cola.enqueue("15:35", "Facebook", "Un amigo te ha enviado un mensaje")
cola.enqueue("16:02", "Twitter", "Python Account ha publicado un tweet")
cola.enqueue("16:23", "Instagram", "User ha subido una foto después de mucho tiempo")
cola.enqueue("16:24", "Facebook", "Un amigo te ha enviado un mensaje")
cola.enqueue("17:30", "Facebook", "Anuncio: nuevo juego móvil")
cola.enqueue("17:35", "Tiktok", "User te ha enviado un mensaje")
cola.enqueue("18:00", "Youtube", "KSI ha subido un video")
cola.enqueue("19:23", "Youtube", "MrBeast ha subido un video")
cola.enqueue("20:20", "Twitter", "User ha publicado un tweet")
cola.enqueue("11:50", "WhatsApp", "Mensaje importante")
cola.enqueue("14:15", "Telegram", "Nueva actualización")
cola.enqueue("21:59", "Instagram", "User te ha enviado un reel")
cola.enqueue("22:35", "Twitter", "Python Account ha publicado un tweet")

# Impresión de las funciones
print("\nCola antes de eliminar notificaciones de Facebook:")
print(cola) # Cola antes
cola.borrarNotisFacebook()
print("\nCola después de eliminar notificaciones de Facebook:")
print(cola) # Cola después

print("\nNotificaciones de Twitter con la palabra 'Python':")
cola.verNotisTwitter() # Imprime por si mismo los elementos deseados, ya que es una función de lectura

# Mostrar notificaciones temporales
print()
cola.mostrar_notificaciones_temporales() # Imprime por sí mismo todo lo que necesita
print()
