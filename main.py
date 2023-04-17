import areas
import perimetros
import volumenes
from utils import continuar, clear_terminal
from termcolor import colored



if __name__ == "__main__":
    try:
        while True:
            clear_terminal()
            opcion = input(f"""{colored("Bienvenido a la calculadora de areas, perimetros y volumenes", "cyan", attrs=['bold'])}
{colored("(a)", "yellow", attrs = ['bold'])} Obtener Areas 
{colored("(b)", "blue", attrs = ['bold'])} Obtener Perimetros
{colored("(c)", "green", attrs = ['bold'])} Obtener Volumenes

para salir digite {colored("'Salir'", "red", attrs=["bold"])}

Elige una opcion: """).lower()
            clear_terminal()
            if opcion == "a":
                opciones = int(input(f"""{colored("Que area deseas saber?", "cyan", attrs=['bold'])}
{colored("(1)", "green", attrs=['bold'])} Cuadrado
{colored("(2)", "blue", attrs=['bold'])} Circulo
{colored("(3)", "yellow", attrs=['bold'])} Rectangulo
{colored("(4)", "magenta", attrs=['bold'])} Triangulo

Elige una opcion: """))
                while True:
                    if opciones == 1:
                        print(f"El area es de {areas.area_of_square()} m^2")
                        if continuar() == True:
                            break
                    elif opciones == 2:
                        print(f"El area es de {areas.area_of_circle()} m^2")
                        if continuar() == True:
                            break
                    elif opciones == 3:
                        print(f"El area es de {areas.area_of_rectangle()} m^2")
                        if continuar() == True:
                            break
                    elif opciones == 4:
                        print(f"El area es de {areas.area_of_triangle()} m^2")
                        if continuar() == True:
                            break
                    else:
                        print("Opcion no valida")
                        continue
            elif opcion == "b":
                opciones = int(input(f"""{colored("Que perimetro deseas saber?", "cyan", attrs=['bold'])}
{colored("(1)", "green", attrs=['bold'])} Cuadrado
{colored("(2)", "blue", attrs=['bold'])} Circulo
{colored("(3)", "yellow", attrs=['bold'])} Rectangulo
{colored("(4)", "magenta", attrs=['bold'])} Triangulo

Elige una opcion: """))
                while True:
                    if opciones == 1:
                        print(f"El perimetro es de {perimetros.perimetro_cuadrado()} m")
                        if continuar() == True:
                            break
                    elif opciones == 2:
                        print(f"El perimetro es de {perimetros.perimetro_circulo()} m")
                        if continuar() == True:
                            break
                    elif opciones == 3:
                        print(f"El perimetro es de {perimetros.perimetro_rectangulo()} m")
                        if continuar() == True:
                            break
                    elif opciones == 4:
                        print(f"El perimetro es de {perimetros.perimetro_triangle()} m")
                        if continuar() == True:
                            break
                    else:
                        print("Opcion no valida")
                        continue
            elif opcion == "c":
                opciones = int(input(f"""{colored("Que volumen deseas saber?", "cyan", attrs=['bold'])}
{colored("(1)", "green", attrs=['bold'])} Esfera
{colored("(2)", "blue", attrs=['bold'])} Cubo
{colored("(3)", "magenta", attrs=['bold'])} Cilindro

Elige una opcion: """))
                while True:
                    if opciones == 1:
                        print(f"El volumen es de {volumenes.volume_sphere()} m^3")
                        if continuar() == True:
                            break
                    elif opciones == 2:
                        print(f"El volumen es de {volumenes.volume_cube()} m^3")
                        if continuar() == True:
                            break
                    elif opciones == 3:
                        print(f"El volumen es de {volumenes.volume_cylinder()} m^3")
                        if continuar() == True:
                            break
                    else:
                        print("Opcion no valida")
                        continue         
                    
            elif opcion == "salir":
                print("Gracias por usar la calculadora")
                break
            else:
                print("Opcion no valida")
                continue

    except Exception as e:
        print(e)

