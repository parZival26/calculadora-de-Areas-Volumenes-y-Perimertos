import math
from utils import cargando

def volume_sphere():
    radio = int(input("Ingrese el radio de la esfera en (m): "))
    cargando()
    return round(4/3 * math.pi * math.pow(radio, 3))

def volume_cube():
    lado = int(input("Ingrese el lado del cubo en (m): "))
    cargando()
    return round(lado**3)

def volume_cylinder():
    radio = int(input("Ingrese el radio del cilindro en (m): "))
    altura = int(input("Ingrese la altura del cilindro en (m): "))
    cargando()
    return round(math.pi * radio**2 * altura)

