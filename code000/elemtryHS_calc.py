# comment
# Calculadora de funciones multiples 'CG'
# archivo Main.pay    menu de General Option 
# 
#  Creado el: 22/05/2025    @Author coconutPineappl
# îî  version: 1.0.0  îî
#  Procesos de calculadora basica
#  suma-resta-multiplicacion-division-potencia-raizCuadrada
# IHR 22 de mayo 2025
# calculadora - Main.py
# 

import math # importamos op matematicas
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
    print("0. Salir")
    print("="*40)

def obtener_numeros(operacion):
    #pedimos al user numeros separados con espacio dependiendo el tamano de su operacion.
    while True:
        entrada = input(f"\nIngresa numeros separados por espacios para {operacion} (Enter para terminar): ").strip()
        if entrada == "":
            return []
        try:
            return list(map(float, entrada.split()))
        except ValueError:
            print("Error: Uno o más valores no son números. Intenta de nuevo.")
    
    #upgrade 1.0.0 > 1.0.1 29/Marzo.25
    #upgrade 1.0.2 30/Marzo.25
        
def realizar_operacion_basica(opcion, simbolo):
    numeros = obtener_numeros(simbolo)
    if not numeros:
        print("No se ingresaron numeros.")
        return None
    #map para convertir entrada float y reducir codigo *30/05
    expresion = f" {simbolo} ".join(map(str, numeros))
    resultado = numeros[0]

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
    print(f"\nOperación: {expresion}")
    print(f"\nResultado: {resultado}")
    return resultado

    #upgrade 1.0.2 30/Marzo.25

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
    #no changes *30/05

def menu_secundario():
    #menu seleccion de operacion 
    """Menú después de cada operación con validación."""
    print("\n¿Qué deseas hacer ahora?")
    print("1. Realizar otra operación")
    print("2. Volver al menú principal")
    print("0. Salir")

    while True:
        opcion = input("Selecciona una opción (0-2): ")
        if opcion in {"1", "2", "0"}:
            return int(opcion)
        print("Error: Ingresa 1, 2 o 0.")

def start_calculadora():
    """Controla el flujo principal de la calculadora."""
    simbolos = {1: "+", 2: "-", 3: "*", 4: "/"}
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opcion (0-6): ")
        
        if opcion == "0":
            print("\n")  # Espacio antes del mensaje
            loadScreen(". . . Saliendo del programa . . .", 50)  
            loadScreen(" Regresando al Menu Principal . . . ", 50)
            print("\n")  # Espacio final
            break
        
        if opcion not in {"1", "2", "3", "4", "5", "6"}:
            print("Error: Opción inválida. Elige un número del 0 al 6.")
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
            elif opcion_sec == 0:
                print("\n")  # Espacio antes del mensaje
                loadScreen(" Regresando al Menu Principal . . . ", 50)
                print("\n")  # Espacio final
                return  # Salir del programa
            
    #upgrade 1.0.2 30/Marzo.25
    #upgrade 1.0.4 07/junio.25
    
