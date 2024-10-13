import numpy as np
import scipy as sp

#Esta función lee una versión en minúsculas y sin espacios de la ecuación de entrada y encuentra los valores de a, b, c, d y el término independiente
#Esta función asume que la ecuación está organizada de la forma x, y, z, w, independiente.
#Si encuentran una manera de, antes de llamar esta función, forzar la ecuación a entrar en esa organización, fuera perfecto
#si no logran hacerlo, crear sus funciones asumiendo que el orden está bien hecho, ya que haré una función que devuelve el control al usuario si el orden es incorrecto
def leerInput (stringinput):
    if(stringinput.count('x') > 1 or stringinput.count('y') > 1 or stringinput.count('z') > 1 or stringinput.count('w') > 1):
        print("Asegúrese que la ecuación esté en su forma más simplificada")
    elif(stringinput.count('x') == 0 and stringinput.count('y') == 0 and stringinput.count('z') == 0 and stringinput.count('w') == 0):
        print("Una expresión sin variables no es ecuación")
    else:
        global a 
        if 'x' in stringinput:
            posicionX = stringinput.find('x')
            a = stringinput[0:posicionX]
        else:
            posicionX = -1
            a = 0
        global b
        if 'y' in stringinput:
            posicionY = stringinput.find('y')
            b = stringinput[posicionX+1:posicionY]
        else:
            posicionY = posicionX
            b = 0
        global c
        if 'z' in stringinput:
            posicionZ = stringinput.find('z')
            c = stringinput[posicionY+1:posicionZ]
        else:
            posicionZ = posicionY
            c = 0
        global d
        if 'w' in stringinput:
            posicionW = stringinput.find('w')
            d = stringinput[posicionZ+1:posicionW]
        else:
            posicionW = posicionZ
            d = 0
        global independiente
        independiente = stringinput[posicionW+1::]
        if(independiente.replace(' ', '') == ''):
            independiente = 0
        print(f"{a}x {b}y {c}z {d}w {independiente}")
        return True

#crear una lista repleta de caracteres inválidos que no deberían aparecer en la ecuación
charsInvalidos = []
for i in range (48):
    if(chr(i) != '+' and chr(i) != '-' and chr(i) != ' '):
        charsInvalidos.append(chr(i))
for i in range(58, 65):
    charsInvalidos.append(chr(i))
for i in range(91, 97):
    charsInvalidos.append(chr(i))

while(True):
    try:
        numeroDeEcuaciones = int(input("Ingrese el número de ecuaciones a analizar: "))
    except:
        print("Asegúrese que sea un número natural de ecuaciones.")
        continue
    if(numeroDeEcuaciones <= 0):
        print("Asegúrese que sea un número natural de ecuaciones.")
        continue
    break
i = 0

#Listas de coeficientes X, Y, Z, W respectivamente, convertir en matrices si es necesario 
#y no asumir que se utilizarán todas las listas ya que no siempre serán 4 variables a analizar

coeficientesX = []
coeficientesY = []
coeficientesZ = []
coeficientesW =[]
terminosIndependientes = []

while(i < numeroDeEcuaciones):

    invalid = 0
    ecuacion = input("Administre la ecuación en cuestión con el formato y orden correcto: ")

    #Chequea que no hayan caracteres inválidos en la ecuación
    for char in charsInvalidos:
        if char in ecuacion:
            print("Caracter inválido detectado, asegúrese de limpiar su ecuación de entrada")
            invalid = -1
    if invalid==-1:
        continue

    #Asegúrense de hacer esto con cada ecuación para ignorar whitespace y mayúsculas
    ecuacion = ecuacion.lower().replace(" ", "")
    success = leerInput(ecuacion)

    if(success):
        try:
            ai = int(a)
            bi = int(b)
            ci = int(c)
            di = int(d)
            ind = int(independiente)
            coeficientesX.append(ai)
            coeficientesY.append(bi)
            coeficientesZ.append(ci)
            coeficientesW.append(di)
            terminosIndependientes.append(ind)
            i += 1
        except:
            print("Ocurrió un error al transformar los valores a enteros, asegúrese de estar usando el formato correcto de una ecuación e intente de nuevo.")

print(f"Coeficientes de X: {coeficientesX}")
print(f"Coeficientes de Y: {coeficientesY}")
print(f"Coeficientes de Z: {coeficientesZ}")
print(f"Coeficientes de W: {coeficientesW}")
print(f"Términos independientes: {terminosIndependientes}")
