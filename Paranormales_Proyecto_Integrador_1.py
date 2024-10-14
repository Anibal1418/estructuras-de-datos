import numpy as np
import scipy as sp

#Esta función lee una versión en minúsculas y sin espacios de la ecuación de entrada y encuentra los valores de a, b, c, d y el término independiente
#Esta función asume que la ecuación está organizada de la forma x, y, z, w, independiente.
#Si encuentran una manera de, antes de llamar esta función, forzar la ecuación a entrar en esa organización, fuera perfecto
#si no logran hacerlo, crear sus funciones asumiendo que el orden está bien hecho, ya que haré una función que devuelve el control al usuario si el orden es incorrecto
def leerInput (stringinput):

    if(stringinput.count('x') > 1 or stringinput.count('y') > 1 or stringinput.count('z') > 1 or stringinput.count('w') > 1):
        print("Asegúrese que la ecuación esté en su forma más simplificada")
        return False

    elif(stringinput.count('x') == 0 and stringinput.count('y') == 0 and stringinput.count('z') == 0 and stringinput.count('w') == 0):
        print("Una expresión sin variables no es ecuación")
        return False

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

#crea una lista repleta de caracteres inválidos que no deberían aparecer en la ecuación
charsInvalidos = []
for i in range (48):
    if(chr(i) != '+' and chr(i) != '-' and chr(i) != ' '):
        charsInvalidos.append(chr(i))
for i in range(58, 65):
    if(chr(i) != '='):
        charsInvalidos.append(chr(i))
for i in range(91, 97):
    charsInvalidos.append(chr(i))

welcomeMsg = ("Bienvenido al programa de resolución de sistemas de ecuaciones lineales usando el método de Cramer.\n\nEste programa le permitirá ingresar un sistema de ecuaciones y determinará si es resolvible.\nEl método de Cramer requiere que el número de ecuaciones sea igual al número de variables y que el determinante de la matriz de coeficientes no sea cero.\nPor favor, siga las instrucciones cuidadosamente para ingresar las ecuaciones en el formato correcto.\nAsegúrese de que las ecuaciones estén en la forma general: ax + by + cz + dw = i.\n\nEmpecemos...\n")
print(welcomeMsg)

#loop que pide al usuario el número de ecuaciones, y confirma que este sea válido
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

#Listas de coeficientes X, Y, Z, W respectivamente, convertidas en vectores numpy

coeficientesX = np.array([])
coeficientesY = np.array([])
coeficientesZ = np.array([])
coeficientesW = np.array([])
terminosIndependientes = np.array([])

#loop que toma input del usuario para construir todas las ecuaciones que este pide
while(i < numeroDeEcuaciones):

    invalid = 0
    ecuacion = input("Administre la ecuación en cuestión con el formato y orden correcto: \n Estructura ejemplo: ax + by +cz +dw = i:\n")

    #Chequea que no hayan caracteres inválidos en la ecuación
    for char in charsInvalidos:
        if char in ecuacion:
            print("Caracter inválido detectado, asegúrese de limpiar su ecuación de entrada")
            invalid = -1
            break
    if invalid==-1:
        continue

#El programa se asegura de hacer esto con cada ecuación para ignorar whitespace y mayúsculas
    ecuacion = ecuacion.lower().replace(" ", "")
    success = leerInput(ecuacion)

#Si la lectura fue exitosa, extrae las variables globales, las convierte en enteros, y las añade al final de los arreglos correspondientes
    if(success):
        try:
            ai = int(a)
            bi = int(b)
            ci = int(c)
            di = int(d)
            ind = int(independiente)
            coeficientesX = np.append(coeficientesX, ai)
            coeficientesY = np.append(coeficientesY, bi)
            coeficientesZ = np.append(coeficientesZ, ci)
            coeficientesW = np.append(coeficientesW, di)
            terminosIndependientes = np.append(terminosIndependientes, ind)
            i += 1
        except:
            print("Ocurrió un error al transformar los valores a enteros, asegúrese de estar usando el formato correcto de una ecuación e intente de nuevo.")

#Esta impresión es solo para debugging, será borrada en la entrega final
print(f"Coeficientes de X: {coeficientesX}")
print(f"Coeficientes de Y: {coeficientesY}")
print(f"Coeficientes de Z: {coeficientesZ}")
print(f"Coeficientes de W: {coeficientesW}")
print(f"Términos independientes: {terminosIndependientes}")

#Crear matriz general que será usada en el método de Cramer
matrizGeneral = np.array([])
#teorema de rouché-frobenius para determinar si las ecuaciones forman un sistema compatible determinado
#de paso, ir añadiendo los vectores de coeficientes no vacíos a la matriz general
numeroDeVariables = 0
for element in coeficientesX:
    if element != 0:
        numeroDeVariables += 1
        matrizGeneral = np.append(matrizGeneral, coeficientesX, axis=0)
        matrizX = np.array([])
        xi = 0
        break
    else:
        matrizX = np.array([None])
        xi = -1
for element in coeficientesY:
    if element != 0:
        numeroDeVariables += 1
        matrizGeneral = np.append(matrizGeneral, coeficientesY, axis=0)
        matrizY = np.array([])
        yi = xi+1
        break
    else:
        matrizY = np.array([None])
        yi = xi
for element in coeficientesZ:
    if element != 0:
        numeroDeVariables += 1
        matrizGeneral = np.append(matrizGeneral, coeficientesZ, axis=0)
        matrizZ = np.array([])
        zi = yi+1
        break
    else:
        matrizZ = np.array([None])
        zi = yi
for element in coeficientesW:
    if element != 0:
        numeroDeVariables += 1
        matrizGeneral = np.append(matrizGeneral, coeficientesW, axis=0)
        matrizW = np.array([])
        wi = zi+1
        break
    else:
        matrizW = np.array([None])
        wi = zi
if(numeroDeVariables == numeroDeEcuaciones):
    print("El sistema de ecuaciones cumple con las condiciones de Rouché-Frobenius.")
else:
    #Si el sistema es tildado como no resolvible, salir del programa
    print("El sistema no es resolvible por Cramer.")
    exit()

#Aquí iría código para confirmar la segunda parte del teorema, consultar el documento para más información

matrizGeneral.shape =  (numeroDeVariables,numeroDeEcuaciones)
print(f"La Matriz General formada es: \n{np.transpose(matrizGeneral)}")

# Comprobar que el determinante de la matriz de coeficientes no sea cero
if matrizGeneral.shape[0] == matrizGeneral.shape[1]:  # Solo si es cuadrada
    determinanteGeneral = np.linalg.det(matrizGeneral)
    if determinanteGeneral == 0:
        print("Pero las ecuaciones son linealmente dependientes. Por lo que el sistema no es resolvible por Cramer.")
        exit()
    else:
        print("Y las ecuaciones son linealmente independientes, por lo que el sistema es resolvible por Cramer.")
else:
    print("No se pudo calcular el determinante, asegúrese que el número de ecuaciones es igual al número de variables.")
    exit()
#con la matriz general ya hecha, el resto es trabajo simple

#Si las matrices fueron creadas correctamente, borra los elementos de sus coeficientes correspondientes,
#y los sustituye por los términos independientes, estilo Cramer
if(None not in matrizX):
    matrizX = np.delete(matrizGeneral, xi, 0)
    matrizX = np.insert(matrizX, xi, terminosIndependientes, axis = 0)
    print(matrizX.transpose())

if(None not in matrizY):
    matrizY = np.delete(matrizGeneral, yi, 0)
    matrizY = np.insert(matrizY, yi, terminosIndependientes, axis = 0)
    print(matrizY.transpose())

if(None not in matrizZ):
    matrizZ = np.delete(matrizGeneral, zi, 0)
    matrizZ = np.insert(matrizZ, zi, terminosIndependientes, axis = 0)
    print(matrizZ.transpose())

if(None not in matrizW):
    matrizW = np.delete(matrizGeneral, wi, 0)
    matrizW = np.insert(matrizW, wi, terminosIndependientes, axis = 0)
    print(matrizW.transpose())
