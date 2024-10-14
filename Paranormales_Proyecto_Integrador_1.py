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
            if(a == '+' or a == ''):
                a = '1'
            elif(a == '-'):
                a = '-1'
        else:
            posicionX = -1
            a = 0
        global b
        if 'y' in stringinput:
            posicionY = stringinput.find('y')
            b = stringinput[posicionX+1:posicionY]
            if(b == '+'):
                b = '1'
            elif(b == '-'):
                b = '-1'
        else:
            posicionY = posicionX
            b = 0

        global c
        if 'z' in stringinput:
            posicionZ = stringinput.find('z')
            c = stringinput[posicionY+1:posicionZ]
            if(c == '+'):
                c = '1'
            elif(c == '-'):
                c = '-1'
        else:
            posicionZ = posicionY
            c = 0
        global d
        if 'w' in stringinput:
            posicionW = stringinput.find('w')
            d = stringinput[posicionZ+1:posicionW]
            if(d == '+'):
                d = '1'
            elif(d == '-'):
                d = '-1'
        else:
            posicionW = posicionZ
            d = 0
        global independiente
        if '=' in stringinput:
            independiente = stringinput[posicionW+1::]
        else:
            print("Una ecuación lineal debe ser igualada a un término independiente.")
            return False
        if(independiente.replace(' ', '') == ''):
            independiente = 0
        independiente = independiente.replace('=', '')
        print(f"{a}x {b}y {c}z {d}w {independiente}")
        return True

#crear una lista repleta de caracteres inválidos que no deberían aparecer en la ecuación
charsInvalidos = []
for i in range (48):
    if(chr(i) != '+' and chr(i) != '-' and chr(i) != ' '):
        charsInvalidos.append(chr(i))
for i in range(58, 65):
    if(chr(i) != '='):
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

coeficientesX = np.array([])
coeficientesY = np.array([])
coeficientesZ = np.array([])
coeficientesW = np.array([])
terminosIndependientes = np.array([])

while(i < numeroDeEcuaciones):

    invalid = 0
    ecuacion = input("Administre la ecuación en cuestión con el formato y orden correcto: \n Estructura ejemplo: ax + by +cz +dw = i:\n")

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

#teorema de rouché-frobenius para determinar si las ecuaciones forman un sistema compatible determinado
numeroDeVariables = 0
for element in coeficientesX:
    if element != 0:
        numeroDeVariables += 1
        break
for element in coeficientesY:
    if element != 0:
        numeroDeVariables += 1
        break
for element in coeficientesZ:
    if element != 0:
        numeroDeVariables += 1
        break
for element in coeficientesW:
    if element != 0:
        numeroDeVariables += 1
        break
if(numeroDeVariables == numeroDeEcuaciones):
    print("El sistema de ecuaciones es resolvible por Cramer.")
else:
    print("El sistema no es resolvible por Cramer.")
    exit
