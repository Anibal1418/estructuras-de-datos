import numpy as np
import scipy as sp

#Esta función lee una versión en minúsculas y sin espacios de la ecuación de entrada y encuentra los valores de a, b, c, d y el término independiente
#Esta función asume que la ecuación está organizada de la forma x, y, z, w, independiente.
#Si encuentran una manera de, antes de llamar esta función, forzar la ecuación a entrar en esa organización, fuera perfecto
#si no logran hacerlo, crear sus funciones asumiendo que el orden está bien hecho, ya que hice una función que devuelve el control al usuario si el orden es incorrecto
def leerInput (stringinput):
    if(stringinput.count('x') > 1 or stringinput.count('y') > 1 or stringinput.count('z') > 1 or stringinput.count('w') > 1):
        print("Asegúrese que la ecuación esté en su forma más simplificada")
    elif(stringinput.count('x') == 0 and stringinput.count('y') == 0 and stringinput.count('z') == 0 and stringinput.count('w') == 0):
        print("Una expresión sin variables no es ecuación")
    elif(stringinput.find('x') > stringinput.find('y') or stringinput.find('y') > stringinput.find('z') or stringinput.find('z') > stringinput.find('w')):
        print("Asegúrese que la ecuación esté en orden: x, y, z, w, término independiente")
    else:
        global a 
        if 'x' in stringinput:
            posicionX = stringinput.find('x')
            a = stringinput[0:posicionX]
        else:
            posicionX = 0
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
    invalid = 0
    ecuacion = input("Administre la ecuación en cuestión con el formato y orden correcto: ")
    for char in charsInvalidos:
        if char in ecuacion:
            print("Caracter inválido detectado, asegúrese de limpiar su ecuación de entrada")
            invalid = -1
    if invalid==-1:
        continue

    success = leerInput(ecuacion.lower().replace(' ', ''))

    if(success):
        break

a = int(a)
b= int(b)
c=int(c)
d=int(d)
independiente=int(independiente)

print(f"a={a}, b={b}, c={c}, d={d}, termino independiente={independiente}")
