#
#
#import time
from delay_general import *
from elemtryHS_calc import start_calculadora #importando calculadora 01
from distance_calc import start_Distancia as main_distancia

def menu_calc():
    print("\n"+"="*40)
    print("\nMENU PRINCIPAL".center(40))
    print("1. Calculadora (Ed basica-Media)")
    print("2. Calculadora de Distancias")
    print("3. otra calculadora")
    print("0. Salir")
    print("\n"+"="*40)

def main():
    while True:
        menu_calc()
        opcion = input("\nSelecciona una opción (0-2): ")
        
        if opcion == "1":
            loadScreen(". . . Cargando calculadora . . .", 50)
            start_calculadora()  # Llama a la calculadora completa
        elif opcion == "2":
            loadScreen(". . . Cargando CDistancia . . .", 50)
            main_distancia() #Llamamos a la calculadora de distancias
        elif opcion == "3":
            loadScreen(". . . Cargando opcion3 . . .")
        elif opcion == "0": #nuevo: Funcion salir == 0
            print("\n")  # Espacio antes del mensaje
            loadScreen(". . . Saliendo del programa . . .", 50)  # Delay de 150ms
            loadScreen(" ¡Gracias por utilizar este proyecto! Vuelve pronto :) ", 50)  # Delay de 100ms
            print("\n")  # Espacio final
            break
        else:
            print("Opcion no valida. Intente de nuevo.")

if __name__ == "__main__":
    main()

