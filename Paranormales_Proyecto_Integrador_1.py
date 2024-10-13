import numpy as np
import scipy as sp

def leerInput (stringinput):
    if(stringinput.count('x') > 1 or stringinput.count('y') > 1 or stringinput.count('z') > 1 or stringinput.count('w') > 1):
        print("Asegúrese que la ecuación esté en su forma más simplificada")
    elif(stringinput.count('x') == 0 and stringinput.count('y') == 0 and stringinput.count('z') == 0 and stringinput.count('w') == 0):
        print("Una expresión sin variables no es ecuación")
    else:
        if 'x' in stringinput:
            posicionX = stringinput.find('x')
            a = stringinput[0:posicionX]
        else:
            posicionX = 0
            a = 0
        if 'y' in stringinput:
            posicionY = stringinput.find('y')
            b = stringinput[posicionX+1:posicionY]
        else:
            posicionY = posicionX
            b = 0
        if 'z' in stringinput:
            posicionZ = stringinput.find('z')
            c = stringinput[posicionY+1:posicionZ]
        else:
            posicionZ = posicionY
            c = 0
        if 'w' in stringinput:
            posicionW = stringinput.find('w')
            d = stringinput[posicionZ+1:posicionW]
        else:
            posicionW = posicionZ
            d = 0
        independiente = stringinput[posicionW+1::]
        print(f"{a}x, {b}y, {c}z, {d}w, {independiente}")


ecuacion = input("Administre la ecuación en cuestión con el formato y orden correcto: ")
ecuacion = ecuacion.replace(' ', '')
leerInput(ecuacion.lower())
