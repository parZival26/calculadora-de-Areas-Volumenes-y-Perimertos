from math import pi
from utils import cargando

def perimetro_circulo():
    radio = int(input("Ingrese el radio del circulo en (m): "))
    cargando()
    return round(2 * pi * radio)

def perimetro_cuadrado():
    lado = int(input("Ingrese el lado del cuadrado en (m): "))
    cargando()
    return round(4 * lado)

def perimetro_rectangulo(lado1, lado2):
    lado1 = int(input("Ingrese el primer lado del rectangulo en (m): "))
    lado2 = int(input("Ingrese el segundo lado del rectangulo en (m): "))
    cargando()
    return round(2 * (lado1 + lado2))

def perimetro_triangle():
    lado1 = int(input("Ingrese el primer lado del triangulo en (m): "))
    lado2 = int(input("Ingrese el segundo lado del triangulo en (m): "))
    lado3 = int(input("Ingrese el tercer lado del triangulo en (m): "))
    cargando()
    return round(lado1 + lado2 + lado3)
    