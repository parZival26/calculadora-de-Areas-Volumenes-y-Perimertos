import math
from utils import cargando

def area_of_circle():
    radio = int(input("Ingrese el radio del circulo en (m): "))
    cargando()
    return round(math.pi * math.pow(radio, 2), 2)

def area_of_square():
    lado = int(input("Ingrese el lado del cuadrado en (m): "))
    cargando()
    return round(math.pow(lado, 2), 2)

def area_of_rectangle():
    lado1 = int(input("Ingrese el primer lado del rectangulo en (m): "))
    lado2 = int(input("Ingrese el segundo lado del rectangulo en (m): "))
    cargando()
    return round(lado1 * lado2, 2)

def area_of_triangle():
    base = int(input("Ingrese la base del triangulo en (m): "))
    altura = int(input("Ingrese la altura del triangulo en (m): "))
    cargando()
    return round((base * altura) / 2, 2)
