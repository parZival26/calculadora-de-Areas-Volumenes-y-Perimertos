import os
from termcolor import colored 
import time

def cargando():
    print("Cargando", end="" ,)
    for i in range(5):
        time.sleep(1)
        print(colored("."), end="", flush=True)
    print("\n")

print(" ¡Listo!")

def clear_terminal():
  os.system('cls' if os.name == 'nt' else 'clear')

def continuar():
        opcion = input("Desea continuar? ({}/{}): ".format(colored("s", "green", attrs=["bold"]), colored("n", "red", attrs=["bold"]))).lower()
        if opcion == "s":
            return True
        elif opcion == "n":
            print("Gracias por usar la calculadora")
            exit()
        else:
            print("Opcion no valida")
            continuar()

