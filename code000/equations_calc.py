# comment
# 
#  Creado el: 07/06/2025    @Author coconutPineappl
# îî  version: 1.0.0  îî
#  Procesos de calculadora avanzada
#  ecuaciones varias (lineal, cuadratica). Suma y resta de matricas (2x2, 3x3)
# IHR 22 de mayo 2025
# 

# advanced_calc.py
import numpy as np
from delay_general import *

def pedir_coeficientes(*nombres):
    return [float(input(f"Ingrese el valor de {n}: ")) for n in nombres]

def resolver_ecuacion_lineal():
    print("Resolviendo ecuación lineal: ax + b = 0")
    a, b = pedir_coeficientes("a", "b")
    if a == 0:
        print("No hay solución o hay infinitas soluciones dependiendo de b.")
    else:
        print(f"Solución: x = {-b} / {a} = {-b / a}")

def resolver_ecuacion_cuadratica():
    print("Resolviendo ecuación cuadrática: ax² + bx + c = 0")
    a, b, c = pedir_coeficientes("a", "b", "c")
    d = b**2 - 4*a*c
    print(f"Discriminante = {d}")
    if d < 0:
        print("No hay soluciones reales.")
    else:
        sqrt_d = d**0.5
        x1, x2 = (-b + sqrt_d)/(2*a), (-b - sqrt_d)/(2*a)
        print(f"Soluciones: x1 = {x1}, x2 = {x2}")

def ingresar_matriz(n):
    print(f"Ingrese los valores de la matriz {n}x{n} fila por fila (separados por espacio):")
    return np.array([list(map(float, input().split())) for _ in range(n)])

def operar_matrices(operacion):
    tipo = int(input("Tamaño de la matriz (2 o 3): "))
    if tipo not in [2, 3]:
        print("Tamaño no válido.")
        return

    print("Ingrese la primera matriz:")
    matriz1 = ingresar_matriz(tipo)
    print("Ingrese la segunda matriz:")
    matriz2 = ingresar_matriz(tipo)

    operaciones = {
        'suma': (matriz1 + matriz2, '+'),
        'resta': (matriz1 - matriz2, '-'),
        'multiplicacion': (np.dot(matriz1, matriz2), '*')
    }

    resultado, simbolo = operaciones[operacion]
    print(f"Procedimiento: matriz1 {simbolo} matriz2")
    print("Resultado:")
    print(resultado)

def start_calculadora_avanzada():
    opciones = {
        '1': resolver_ecuacion_lineal,
        '2': resolver_ecuacion_cuadratica,
        '3': lambda: operar_matrices('suma'),
        '4': lambda: operar_matrices('resta'),
        '5': lambda: operar_matrices('multiplicacion'),
    }

    while True:
        print("\n--- Calculadora Matemática Avanzada ---")
        print("1. Resolver ecuación lineal")
        print("2. Resolver ecuación cuadrática")
        print("3. Suma de matrices")
        print("4. Resta de matrices")
        print("5. Multiplicación de matrices")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '0':
            loadScreen(". . . Saliendo del programa . . .", 50)  
            loadScreen(" Regresando al Menu Principal . . . ", 50)
            break
        elif opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción no válida.")
