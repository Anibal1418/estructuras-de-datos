import numpy as np
import re
#Esta función lee una versión en minúsculas y sin espacios de la ecuación de entrada y encuentra los valores de a, b, c, d y el término independiente
#Esta función asume que la ecuación está organizada de la forma x, y, z, w.
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

welcomeMsg = ("Bienvenido al programa de resolución de sistemas de ecuaciones lineales usando el método de Cramer.\n\nEste programa le permitirá ingresar un sistema de ecuaciones y determinará si es resolvible.\nEl método de Cramer requiere que el número de ecuaciones sea igual al número de variables y que el determinante de la matriz de coeficientes no sea cero.\nPor favor, siga las instrucciones cuidadosamente para ingresar las ecuaciones en el formato correcto.\n\nEmpecemos...\n")
print(welcomeMsg)

# Inicializar los arreglos de coeficientes y términos independientes
coeficientesX = np.array([])
coeficientesY = np.array([])
coeficientesZ = np.array([])
coeficientesW = np.array([])
terminosIndependientes = np.array([])

#Funcion para organizar y despejar la ecuacion
#hecho por Eduardo Alba ( linea 100-182)
def organizar_ecuacion(ecuacion):
    ecuacion = ecuacion.lower().replace(" ", "")
    if '=' not in ecuacion:
        print("La ecuacion debe tener un termino igual (=)")
        return None

    izquierda, derecha = ecuacion.split('=')
    
    coef_a = "0"
    coef_b = "0"
    coef_c = "0"
    coef_d = "0"

    terminos = re.findall(r'[\+\-]?\d*[xyzw]', izquierda)
    for termino in terminos:
        if 'x' in termino:
            coef_a = termino.replace('x', '')
        elif 'y' in termino:
            coef_b = termino.replace('y', '')
        elif 'z' in termino:
            coef_c = termino.replace('z', '')
        elif 'w' in termino:
            coef_d = termino.replace('w', '')

    coef_a = coef_a if coef_a not in ["", "+", "-"] else coef_a + "1"
    coef_b = coef_b if coef_b not in ["", "+", "-"] else coef_b + "1"
    coef_c = coef_c if coef_c not in ["", "+", "-"] else coef_c + "1"
    coef_d = coef_d if coef_d not in ["", "+", "-"] else coef_d + "1"

    terminos_izquierda = re.findall(r'[\+\-]?\d+(?![xyzw])', izquierda)
    terminos_derecha = re.findall(r'[\+\-]?\d+(?![xyzw])', derecha)

    termino_independiente_izquierda = sum(int(t) for t in terminos_izquierda)
    termino_independiente_derecha = sum(int(t) for t in terminos_derecha)

    termino_independiente = termino_independiente_derecha - termino_independiente_izquierda

    nueva_ecuacion = f"{coef_a}x {coef_b}y {coef_c}z {coef_d}w = {termino_independiente}"
    nueva_ecuacion = nueva_ecuacion.replace("+-", "-")
    nueva_ecuacion = nueva_ecuacion.replace("-+", "-")
    nueva_ecuacion = nueva_ecuacion.replace("--", "+")
    nueva_ecuacion = nueva_ecuacion.replace("++", "+")
    nueva_ecuacion = nueva_ecuacion.replace("  ", " ")

    return nueva_ecuacion.strip()

while True:
    try:
        numeroDeEcuaciones = int(input("Ingrese el número de ecuaciones al analizar: "))
        if numeroDeEcuaciones <= 0:
            raise ValueError
        break
    except ValueError:
        print("Asegúrese de que sea un número natural de ecuaciones.")

i = 0
while i < numeroDeEcuaciones:
    ecuacion = input("Ingrese la ecuación a analizar: ")
    invalid = False
    
    for char in charsInvalidos:
        if char in ecuacion:
            print("Caracter inválido detectado, asegúrese de limpiar su ecuación de entrada")
            invalid = True
            break
    
    if invalid:
        continue

    nueva_ecuacion = organizar_ecuacion(ecuacion)
    if nueva_ecuacion is None:
        continue

    print("Ecuación reorganizada:", nueva_ecuacion)

    try:
        
        success = leerInput(nueva_ecuacion) 
        if not success:
            continue
    except ValueError as e:
        print("Ocurrió un error al transformar los valores a enteros, asegúrese de estar usando el formato correcto de una ecuación e intente de nuevo.")
        continue

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
#Confirmar rouché-frobenius
if(numeroDeVariables == numeroDeEcuaciones):
    print("El sistema de ecuaciones cumple con las condiciones de Rouché-Frobenius.")
else:
    #Si el sistema es tildado como no resolvible, salir del programa
    print("El sistema no es resolvible por Cramer.")
    exit()

matrizGeneral.shape =  (numeroDeVariables,numeroDeEcuaciones)
print(f"La Matriz General formada es: \n{np.transpose(matrizGeneral)}")

# Comprobar que el determinante de la matriz de coeficientes no sea cero y determinar finalmente si es resolvible
# Hecho por Luis Muñoz
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

# Buscar la matriz transpuesta, el determinante y el valor de cada variable. 
# Hecho por Luis Muñoz y Luis Anibal
if(None not in matrizX):
    matrizX = np.delete(matrizGeneral, xi, 0)
    matrizX = np.insert(matrizX, xi, terminosIndependientes, axis = 0)
    determinanteX = np.linalg.det(matrizX)
    valorX = round(determinanteX / determinanteGeneral, 2)
    print("Matriz X:")
    print(matrizX.transpose())
    print(f"Determinante de Matriz X: {round(determinanteX, 2)}, Valor de X: {valorX}")

if(None not in matrizY):
    matrizY = np.delete(matrizGeneral, yi, 0)
    matrizY = np.insert(matrizY, yi, terminosIndependientes, axis = 0)
    determinanteY = np.linalg.det(matrizY)
    valorY = round(determinanteY / determinanteGeneral, 2)
    print("Matriz Y:")
    print(matrizY.transpose())
    print(f"Determinante de Matriz Y: {round(determinanteY, 2)}, Valor de Y: {valorY}")

if(None not in matrizZ):
    matrizZ = np.delete(matrizGeneral, zi, 0)
    matrizZ = np.insert(matrizZ, zi, terminosIndependientes, axis = 0)
    determinanteZ = np.linalg.det(matrizZ)
    valorZ = round(determinanteZ / determinanteGeneral, 2)
    print("Matriz Z:")
    print(matrizZ.transpose())
    print(f"Determinante de Matriz Z: {round(determinanteZ, 2)}, Valor de Z: {valorZ}")

if(None not in matrizW):
    matrizW = np.delete(matrizGeneral, wi, 0)
    matrizW = np.insert(matrizW, wi, terminosIndependientes, axis = 0)
    determinanteW = np.linalg.det(matrizW)
    valorW = round(determinanteW / determinanteGeneral, 2)
    print("Matriz W:")
    print(matrizW.transpose())
    print(f"Determinante de Matriz W: {round(determinanteW, 2)}, Valor de W: {valorW}")