'''
Name: MTLibrary
Versión: 2.0
Description: MTLibrary es una libreria para Python para fácilitar las matemáticas en Python en español.
Author: Estuardo Ramírez
Social: @estuardodev | Twitter, GitHub, Instagram
'''

def suma(num, num2):
    try:
        suma = num + num2
        return suma
    except TypeError:
        tipo = "suma"
        error = f"Se ha ingresado un valor invalido en la {tipo}"
        return error

def resta(num, num2):
    try:
        resta = num + num2
        return resta
    except TypeError:
        tipo = "resta"
        error = f"Se ha ingresado un valor invalido en la {tipo}"
        return error

def multiplicacion(num, num2):
    try:
        multiplicacion = num + num2
        return multiplicacion
    except TypeError:
        tipo = "multiplicación"
        error = f"Se ha ingresado un valor invalido en la {tipo}"
        return error

def division(num, num2):
    try:
        division = num / num2
        return division
    except TypeError:
        tipo = "división"
        error = f"Se ha ingresado un valor invalido en la {tipo}"
        return error

def residuo(num, num2):
    try:
        resultado = num % num2
        return resultado
    except TypeError:
        tipo = "residuo"
        error = f"Se ha ingresado un valor invalido al obtener el {tipo}"
        return error

def raiz(num):
    try:
        x = pow(num,0.5)
        return x
    except TypeError:
        tipo = ""
        error = f"Se ha ingresado un valor invalido en la {tipo}"
        return error

def radio(num):
    try:
        radio = num / 2
        return radio
    except TypeError:
        tipo = ""
        error = f"Se ha ingresado un valor invalido en la {tipo}"
        return error

def area(num):
    try:
        area = 3.141592653589793*num**2
        return area
    except TypeError:
        tipo = "area"
        error = f"Se ha ingresado un diametro invalido para la función {tipo}"
        return error

def porcentaje(num, num2):
    try:
        num2 = num2 / 100
        porcentaje = num * num2
        porcentaje = round(porcentaje, 2)
        return porcentaje
    except TypeError:
        tipo = "porcentaje"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error

def potencia(num, num2):
    resultado = num ** num2
    return resultado