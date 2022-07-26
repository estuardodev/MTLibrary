'''
Name: MTLibrary
Versión: 2.0
Versión-desarrollo: 2.0.4
Description: MTLibrary es una libreria para Python para fácilitar las matemáticas en Python en español.
Author: Estuardo Ramírez
Social: @estuardodev | Twitter, GitHub, Instagram
'''

# Variables globales
pi = 3.141592653589793
tau = 6.283185307179586
e = 2.718281828459045

def suma(dato1=0, dato2=0):
    '''
    SUMA:\n
    Ejecutara una suma entre los valores asignados al primer argumento (dato1) y el segundo argumento (dato2)
    '''
    try:
        suma = dato1 + dato2
        return suma
    except TypeError:
        tipo = "suma"
        error = f"Se ha ingresado un valor invalido en la {tipo}"
        return error

def resta(dato1=0, dato2=0):
    '''
    RESTA:\n
    Ejecutara una resta entre los valores asignados al primer argumento (dato1) y el segundo argumento (dato2)
    '''
    try:
        resta = dato1 - dato2
        return resta
    except TypeError:
        tipo = "resta"
        error = f"Se ha ingresado un valor invalido en la {tipo}"
        return error

def multiplicacion(dato1=0, dato2=0):
    '''
    MULTIPLICACIÓN:\n
    Ejecutara una multiplicación en donde el segundo armugento (dato2) multiplicara al primer argumento (dato1)
    '''
    try:
        multiplicacion = dato1 * dato2
        return multiplicacion
    except TypeError:
        tipo = "multiplicación"
        error = f"Se ha ingresado un valor invalido en la {tipo}"
        return error

def division(dato1=0, dato2=0):
    '''
    DIVISIÓN:\n
    Ejecutara una división donde el primer argumento (dato1) sera dividido entre el segundo argumento (dato2)
    '''
    try:
        division = dato1 / dato2
        return division
    except TypeError:
        tipo = "división"
        error = f"Se ha ingresado un valor invalido en la {tipo}"
        return error

def residuo(dato1=0, dato2=0):
    '''
    RESIDUO:\n
    Al ejecutarse devolvera el residuo de la división del primer argumento (dato1) dividido el segundo argumento (dato2)
    '''
    try:
        resultado = dato1 % dato2
        return resultado
    except TypeError:
        tipo = "residuo"
        error = f"Se ha ingresado un valor invalido al obtener el {tipo}"
        return error

def raiz(dato1=0):
    '''
    RAÍZ:\n
    Devolvera la raíz cuadrada del valor dado
    '''
    try:
        x = pow(dato1,0.5)
        return x
    except TypeError:
        tipo = ""
        error = f"Se ha ingresado un valor invalido en la {tipo}"
        return error

def radio(dato1=0):
    '''
    RADIO:\n
    Como resultado devolvera el radio de un circulo del valor dado
    '''
    try:
        radio = dato1 / 2
        return radio
    except TypeError:
        tipo = "radio"
        error = f"Se ha ingresado un valor invalido en la {tipo}"
        return error

def area(dato1=0):
    '''
    ÁREA:\n
    Como resultado sera el área del valor dado en el argumento
    '''
    try:
        area = 3.141592653589793*dato1**2
        return area
    except TypeError:
        tipo = "area"
        error = f"Se ha ingresado un diametro invalido para la función {tipo}"
        return error

def porcentaje(dato1=0, dato2=0):
    '''
    PORCENTAJE:\n
    Devolvera el porcentaje asignado en el segundo argumento (dato2) del primer argumento (dato1)
    '''
    try:
        dato2 = dato2 / 100
        porcentaje = dato1 * dato2
        porcentaje = round(porcentaje, 2)
        return porcentaje
    except TypeError:
        tipo = "porcentaje"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error

def potencia(dato1=0, dato2=0):
    '''
    POTENCIA:\n
    Potenciara el valor asignado en el primer argumento (dato1) al del valor asignado al segundo argumento (dato2)
    '''
    try:
        resultado = dato1 ** dato2
        return resultado
    except TypeError:
        tipo = "potencia"
        error = f"Se ha ingresado un valor invalido en la {tipo}"
        return error
    