import numpy as np
import scipy as sp

def leerInput (stringinput):
    if 'x' in stringinput:
        posicionX = stringinput.find('x')
        a = stringinput[0:posicionX]
    if 'y' in stringinput:
        posicionY = stringinput.find('y')
        b = stringinput[0:posicionY]
    if 'z' in stringinput:
        posicionZ = stringinput.find('z')
        c = stringinput[0:posicionZ]
    if 'w' in stringinput:
        posicionW = stringinput.find('w')
        d = stringinput[0:posicionW]


ecuacion = input("Administre la ecuación en cuestión con el formato correcto: ")
leerInput(ecuacion.lower())
