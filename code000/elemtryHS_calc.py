# Procesos de calculadora basica
# 
# 

# IHR 22 de mayo 2025
# calcukadora - main.py
# 

import math #muestra el menu principal del programa
import time #para el delay
from delay_general import *

def mostrar_menu():
    print("\n"+"="*40)
    print("CALCULADORA GUAY".center(40))
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicacion (*)")
    print("4. Division (/)")
    print("5. Raiz Cuadrada (√)")
    print("6. Potencia (^)")
    print("7. Salir")
    print("="*40)

def obtener_numeros(operacion):
    #pedimos al user numeros separados con espacio dependiendo el tamano de su operacion.
    while True:
        entrada = input(f"\nIngresa numeros separados por espacios para {operacion} (Enter para terminar): ").strip()
        if entrada == "":
            return []
        
        numeros = []
        error = False

        for valor in entrada.split():
            try:
                numero = float(valor)
                numeros.append(numero)
            except ValueError:
                print(f"Error: '{valor}' no es un numero. Intenta de nuevo.")
                error = True
                break
        
        if not error:
            return numeros
        
def realizar_operacion_basica(opcion, simbolo):
    numeros = obtener_numeros(simbolo)
    if not numeros:
        print("No se ingresaron numeros.")
        return None
    
    resultado = numeros[0]
    expresion = str(resultado)

    for num in numeros[1:]:
        if opcion == 1:  # Suma
            resultado += num
        elif opcion == 2:  # Resta
            resultado -= num
        elif opcion == 3:  # Multiplicación
            resultado *= num
        elif opcion == 4:  # División
            if num == 0:
                print("No puedes dividir entre cero.  Indeterminado.")
                return None
            resultado /= num
        
        expresion += f" {simbolo} {num}"
    
    print(f"\nOperación: {expresion}")
    print(f"Resultado: {resultado}")
    return resultado

def realizar_operacion_avanzada(opcion):
    #Maneja raíces y potencias con validación de errores.
    while True:
        try:
            if opcion == 5:  # Raíz cuadrada
                num = float(input("\nIngresa un número para calcular su raíz cuadrada: "))
                if num < 0:
                    print("Error: No existe raíz real de un número negativo.")
                    continue
                resultado = math.sqrt(num)
                print(f"√{num} = {resultado}")
                return resultado
            
            elif opcion == 6:  # Potencia
                base = float(input("\nIngresa la base: "))
                exponente = float(input("Ingresa el exponente: "))
                if base == 0 and exponente < 0:
                    print("Error: Indeterminación (0^negativo).")
                    continue
                resultado = base ** exponente
                print(f"{base}^{exponente} = {resultado}")
                return resultado
        
        except ValueError:
            print("Error: Ingresa un número válido.")

def menu_secundario():
    #menu seleccion de operacion 
    """Menú después de cada operación con validación."""
    print("\n¿Qué deseas hacer ahora?")
    print("1. Realizar otra operación")
    print("2. Volver al menú principal")
    print("3. Salir")

    while True:
        opcion = input("Selecciona una opción (1-3): ")
        if opcion in {"1", "2", "3"}:
            return int(opcion)
        print("Error: Ingresa 1, 2 o 3.")

def start_calculadora():
    """Controla el flujo principal de la calculadora."""
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una operación (1-7): ")
        
        if opcion == "7":
            print("\n")  # Espacio antes del mensaje
            loadScreen(". . . Saliendo del programa . . .", 50)  
            loadScreen(" Regresando al Menu Principal . . . ", 50)
            print("\n")  # Espacio final
            break
        
        if opcion not in {"1", "2", "3", "4", "5", "6"}:
            print("Error: Opción inválida. Elige un número del 1 al 7.")
            continue
        
        opcion = int(opcion)
        
        # Operaciones básicas (1-4)
        if 1 <= opcion <= 4:
            simbolos = {1: "+", 2: "-", 3: "*", 4: "/"}
            realizar_operacion_basica(opcion, simbolos[opcion])
        
        # Operaciones avanzadas (5-6)
        elif opcion in {5, 6}:
            realizar_operacion_avanzada(opcion)
        
        # Menú secundario
        while True:
            opcion_sec = menu_secundario()
            if opcion_sec == 1:
                if 1 <= opcion <= 4:
                    realizar_operacion_basica(opcion, simbolos[opcion])
                else:
                    realizar_operacion_avanzada(opcion)
            elif opcion_sec == 2:
                break  # Volver al menú principal
            elif opcion_sec == 3:
                print("\n")  # Espacio antes del mensaje
                loadScreen(". . . Saliendo del programa . . .", 50)  
                loadScreen(" Regresando al Menu Principal . . . ", 50)
                print("\n")  # Espacio final
                return  # Salir del programa


