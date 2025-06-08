# comment
# Calculadora de funciones multiples 'CG'
# archivo Main.pay    menu de General Option 
# 
#  Creado el: 22/05/2025    @Author coconutPineappl
# îî  version: 1.0.0  îî
#  Procesos de calculadora basica
# IHR 22 de mayo 2025
# calculadora - Main.py
# 

from delay_general import *
from elemtryHS_calc import start_calculadora #importando calculadora basica
from distance_calc import start_Distancia #importando calculadora avanzada (distancias)
from equations_calc import start_calculadora_avanzada

def menu_calc():
    print("\n"+"="*40)
    print("\nMENU PRINCIPAL".center(40))
    print("1. Calculadora Basica (Ed basica-Media)")
    print("2. Calculadora de Distancias")
    print("3. Calculadora Avanzada (Ed Media Superior)")
    print("0. Salir")
    print("\n"+"="*40)

def main():
    while True:
        menu_calc()
        opcion = input("\nSelecciona una opción (0-3): ")
        
        if opcion == "1":
            loadScreen(". . . Cargando Calculadora . . .", 50)
            start_calculadora()  # Llama a la calculadora completa
        elif opcion == "2":
            loadScreen(". . . Cargando Calculadora de Distancias . . .", 50)
            start_Distancia() #Llamamos a la calculadora de distancias
        elif opcion == "3":
            loadScreen(". . . Cargando Calculadora Avanzada . . .", 50)
        elif opcion == "0": #nuevo: Funcion salir == 0
            print("\n")  # Espacio antes del mensaje
            loadScreen(". . . Saliendo del programa . . .", 50)
            loadScreen(" ¡Gracias por utilizar este proyecto! Vuelve pronto :) ", 50)
            print("\n")  # Espacio final
            break
        else:
            print("Opcion no valida. Intente de nuevo.")

if __name__ == "__main__":
    main()
    