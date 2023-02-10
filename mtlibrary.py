'''
Name: MTLibrary
Versión: 2.0
Versión-desarrollo: 2.0.5
Description: MTLibrary es una libreria para Python para fácilitar las matemáticas en Python en español.
Author: Estuardo Ramírez
Social: @estuardodev | Twitter, GitHub, Instagram
'''

# Libreria Necesaria
import math

# Variables globales
pi = 3.141592653589793
tau = 6.283185307179586
e = 2.718281828459045
nan = float('nan')

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
    
def arcocoseno(dato1=0):
    '''
    ARCOSENO:\n
    Devolvera el arcocoseno del valor dado
    '''
    try:
        resultado = math.acos(dato1)
        return resultado
    except TypeError:
        tipo = "arcoseno"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error

def cosenoh(dato1=0):
    '''
    COSENO HIPERBÓLICO:\n
    Devolvera el COSENO HIPERBÓLICO del valor dado
    '''
    try:
        resultado = math.acosh(dato1)
        return resultado
    except TypeError:
        tipo = "coseno Hiperbólico"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error


def seno_h(dato1=0):
    '''
    SENO HIPERBÓLICO:\n
    Devolvera el seno hiperbólico del valor dado
    '''
    try:
        resultado = math.asinh(dato1)
        return resultado
    except TypeError:
        tipo = "seno Hiperbólico"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error

def tangente_a(dato1=0):
    '''
    TANGENTE DE ARCO:\n
    Devuelve la tangente de arco de diferentes números
    '''
    try:
        resultado = math.atan(dato1)
        return resultado
    except TypeError:
        tipo = "tangente de arco"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error

def tangente_a2(dato1=0, dato2=0):
    '''
    TANGENTE DE ARCO EN RADIANES:\n
    Devuelve la tangente de arco de y/x en radianes
    '''
    try:
        resultado = math.atan2(dato1, dato2)
        return resultado
    except TypeError:
        tipo = "tangente de arco en radianes"
        error = f"Se ha ingresado un valor invalido en la {tipo}"
        return error

def arcotangente_h(dato1=0):
    '''
    ARCOTANGENTE HIPERBÓLICO:\n
    Encuentre el valor de arcotangente hiperbólico del valor dado
    '''
    try:
        resultado = math.atanh(dato1)
        return resultado
    except TypeError:
        tipo = "arcotangente Hiperbólico"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error

def redondear_arriba(dato1=0):
    '''
    REDONDEAR ARRIBA:\n
    Redondea el valor dado hacia arriba hasta el siguiente entero
    '''
    try:
        resultado = math.ceil(dato1)
        return resultado
    except TypeError:
        tipo = "redondear arriba"
        error = f"Se ha ingresado un valor invalido para {tipo}"
        return error


def combinaciones(dato1=0, dato2=0):
    '''
    COMBINACIONES:\n
    Devolvera las combinaciones del valor dado en el primer argumento (dato1) y el segundo argumento (dato2)
    '''
    try:
        resultado = math.comb(dato1, dato2)
        return resultado
    except TypeError:
        tipo = "combinaciones"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error

def copiar_signo(dato1=0, dato2=0):
    '''
    COPIAR SIGNO:\n
    Retornara el valor del primer argumento (dato1) con el mismo signo que el segundo argumento (dato2)
    '''
    try:
        resultado = math.copysign(dato1, dato2)
        return resultado
    except TypeError:
        tipo = "copiar signo"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error


def coseno(dato1=0):
    '''
    COSENO:\n
    Retornara el coseno del valor dado
    '''
    try:
        resultado = math.cos(dato1)
        return resultado
    except TypeError:
        tipo = "coseno"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error

def coseno_h(dato1=0):
    '''
    COSENO HIPERBÓLICO:\n
    Devolvera el coseno hiperbólico del valor dado
    '''
    try:
        resultado = math.cosh(dato1)
        return resultado
    except TypeError:
        tipo = "coseno Hiperbólico"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error


def angulos_radianes_g(dato1=0):
    '''
    ANGULOS RADIANES G:\n
    Convierte los angulos de radianes a grados
    '''
    try:
        resultado = math.degrees(dato1)
        return resultado
    except TypeError:
        tipo = "angulos radianes a grados"
        error = f"Se ha ingresado un valor invalido al convertir {tipo}"
        return error


def distancia(dato1=0, dato2=0):
    '''
    DISTANCIA:\n
    Devolvera la distancia del valor dado en el primer argumento (dato1) y el segundo argumento (dato2)
    '''
    try:
        resultado = math.hypot(dato1, dato2)
        return resultado
    except TypeError:
        tipo = "distancia"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error


def error_print(dato1=0):
    '''
    ERROR PRINT:\n
    Función que imprime el dato dado de forma erronea
    '''
    try:
        resultado = math.erf(dato1)
        return resultado
    except TypeError:
        tipo = "error print"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error


def error_print_complementaria(dato1=0):
    '''
    ERROR PRINT COMPLEMENTARIO:\n
    Imprime la función de error complementaria para diferentes números
    '''
    try:
        resultado = math.erfc(dato1)
        return resultado
    except TypeError:
        tipo = "error print complementario"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error


def e_elevado(dato1=0):
    '''
    E ELEVADO:\n
    La función eleva el número e (2.718281828459045) a la potencia indicada como argumento
    '''
    try:
        resultado = math.exp(dato1)
        return resultado
    except TypeError:
        tipo = "e elevado"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error


def e_elevado_1(dato1=0):
    '''
    E ELEVADO X -1:\n
    Retorna el valor de e elevado a la potencia indicada como argumento menos uno
    '''
    try:
        resultado = math.expm1(dato1)
        return resultado
    except TypeError:
        tipo = "e elevado x - 1"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error


def valor_absoluto(dato1=0):
    '''
    VALOR ABSOLUTO:\n
    Retornara el valor absoluto del valor dado
    '''
    try:
        resultado = math.fabs(dato1)
        return resultado
    except TypeError:
        tipo = "valor absoluto"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error


def factorial(dato1=0):
    '''
    FACTORIAL:\n
    Retorna todos los numeros enteros menores o iguales al valor dado
    '''
    try:
        resultado = math.factorial(dato1)
        return resultado
    except TypeError:
        tipo = "factorial"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error 


def redendeo_abajo(dato1=0):
    '''
    REDONDEO ABAJO:\n
    Retorna el valor redondeado a la parte menor o igual del valor dado
    '''
    try:
        resultado = math.floor(dato1)
        return resultado
    except TypeError:
        tipo = "redondeo abajo"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error


def frexp(dato1=0):
    '''
    FREXP:\n
    Devolvera el frexp del valor dado
    '''
    try:
        resultado = math.frexp(dato1)
        return resultado
    except TypeError:
        tipo = "frexp"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error


def suma_iterables(dato1=0, dato2=0):
    '''
    SUMA ITERABLES:\n
    El método devuelve la suma de todos los elementos en cualquier iterable (tuplas, matrices, listas, etc.)
    '''
    try:
        resultado = math.fsum(dato1, dato2)
        return resultado
    except TypeError:
        tipo = "suma iterables"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error


def gamma(dato1=0):
    '''
    GAMMA:\n
    Devolvera el gamma del valor dado
    '''
    try:
        resultado = math.gamma(dato1)
        return resultado
    except TypeError:
        tipo = "gamma"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error


def mayor_divisor_comun(dato1=0, dato2=0):
    '''
    MAYOR DIVISOR COMÚN:\n
    Encuentra el mayor divisor común de los dos enteros
    '''
    try:
        resultado = math.gcd(dato1, dato2)
        return resultado
    except TypeError:
        tipo = "mayor divisor comun"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error


def hipotenusa(dato1=0, dato2=0):
    '''
    HIPOTENUSA:\n
    Devolvera el la hipotenusa de los dos valores dados
    '''
    try:
        resultado = math.hypot(dato1, dato2)
        return resultado
    except TypeError:
        tipo = "hipotenusa"
        error = f"Se ha ingresado un valor invalido en la {tipo}"
        return error


def valores_cerca(dato1=0, dato2=0, rtol=0, atol=0):
    '''
    VALORES CERCA:\n
    Compruebe si dos valores están cerca el uno del otro
    '''
    try:
        resultado = math.isclose(dato1, dato2, rtol, atol)
        return resultado
    except TypeError:
        tipo = "isclose"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error


def finito(dato1=0):
    '''
    FINITO:\n
    Compruebe si un valor es finito o no lo es
    '''
    try:
        resultado = math.isfinite(dato1)
        return resultado
    except TypeError:
        tipo = "finito"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error


def infinito(dato1=0):
    '''
    INFINITO:\n
    Compruebe si un valor es infinito o no lo es
    '''
    try:
        resultado = math.isinf(dato1)
        return resultado
    except TypeError:
        tipo = "infinito"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error


def es_nan(dato1=0):
    '''
    NAN:\n
    Compruebe si un valor es nan o no lo es
    '''
    try:
        resultado = math.isnan(dato1)
        return resultado
    except TypeError:
        tipo = "es nan"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error


def redondar_raiz_abajo(dato1=0):
    '''
    REDONDEAR RAIZ ABAJO:\n
    Redondea el numero de la raiz cuadrada al siguiente numero entero menor o igual
    '''
    try:
        resultado = math.isqrt(dato1)
        return resultado
    except TypeError:
        tipo = "redondar raiz abajo"
        error = f"Se ha ingresado un valor invalido al {tipo}"
        return error

def minimo_comun_multiplo(dato1=0, dato2=0):
    '''
    LCM:\n
    Devolvera el mínimo común multiplo del valor dado
    '''
    try:
        resultado = math.lcm(dato1, dato2)
        return resultado
    except TypeError:
        tipo = "mínimo común multiplo"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error


def multi_por_2_elevado_a_la_potencia_de_un_exponente(dato1=0, dato2=0):
    '''
    Multiplicar por 2 elevado a la potencia de un exponente:\n
    Devolvera el multiplicar por 2 elevado a la potencia de un exponente del valor dado
    '''
    try:
        resultado = math.ldexp(dato1, dato2)
        return resultado
    except TypeError:
        tipo = "multiplicar por 2 elevado a la potencia de un exponente"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error


def logaritmo_natural_del_valor_absoluto(dato1=0):
    '''
    LGAMMA:\n
    Devolvera el logaritmo natural del valor absoluto del valor dado
    '''
    try:
        resultado = math.lgamma(dato1)
        return resultado
    except TypeError:
        tipo = "logaritmo natural del valor absoluto"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error


def log(dato1=0, base=0):
    '''
    LOG:\n
    Devolvera el log del valor dado
    '''
    try:
        resultado = math.log(dato1, base)
        return resultado
    except TypeError:
        tipo = "log"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error


def log10(dato1=0):
    '''
    LOG10:\n
    Devolvera el log10 del valor dado
    '''
    try:
        resultado = math.log10(dato1)
        return resultado
    except TypeError:
        tipo = "log10"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error


def log1p(dato1=0):
    '''
    LOG1P:\n
    Devolvera el log1p del valor dado
    '''
    try:
        resultado = math.log1p(dato1)
        return resultado
    except TypeError:
        tipo = "log1p"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error


def log2(dato1=0):
    '''
    LOG2:\n
    Devolvera el log2 del valor dado
    '''
    try:
        resultado = math.log2(dato1)
        return resultado
    except TypeError:
        tipo = "log2"
        error = f"Se ha ingresado un valor invalido en el {tipo}"
        return error


