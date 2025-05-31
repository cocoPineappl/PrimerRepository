# comment
# Creado el: 26/05/2025    @Author coconutPineappl
# îî  version: 1.0.0  îî
#  Calculadora de distancias mm, cm, m, km
# Util para medir, guardar medidas y consultar historial
# 
import re
from typing import List, Tuple
from delay_general import *

#config de unidades y factores de conversion
Unidades = {
    'mm': 0.001,
    'cm': 0.01,
    'm': 0.1,
    'km': 1000.0
}

Compatibles = [
    {'mm', 'cm'},
    {'cm', 'm'},
    {'m', 'km'}
]
    #upgrade 1.0.3 30/Marzo.25

def convertir_a_metros(valor:float, unidad:str) -> float:
    if unidad not in Unidades:
        raise ValueError(f"Unidad desconocida: {unidad}")
    return valor * Unidades[unidad]

    #upgrade 1.0.2 30/Marzo.25

def parsear_entrada(entrada:str) -> List[Tuple[float,str]]:
    patron= r'([\d.]+)\s*([a-zA-Z]+)'
    return [(float(valor), unidad.lower()) for valor, unidad in re.findall(patron,entrada)]

def unidades_compatibles(unidades: List[str]) -> bool:
    conjunto = set(unidades)
    return any(conjunto.issubset(grupo) for grupo in Compatibles)
    #upgrade 1.0.3 30/Marzo.25

def calcular_distancia(entrada:str, historial:List[str]) -> Tuple[float,str]:
    valores_unidades = parsear_entrada(entrada)
    if not valores_unidades:
        raise ValueError("Formato inválido. Ejemplo: '5cm + 10mm'")

    unidades = [unidad for _, unidad in valores_unidades]
    if not unidades_compatibles(unidades):
        raise ValueError("Solo puedes sumar unidades compatibles (mm-cm, cm-m, m-km).")

    total_metros = sum(convertir_a_metros(valor, unidad) for valor, unidad in valores_unidades)
    expresion = " + ".join(f"{valor} {unidad}" for valor, unidad in valores_unidades)

        # Conversión amigable para mostrar resultado final
    if set(unidades).issubset({'mm', 'cm'}):
        total_mm = total_metros * 1000
        cm = int(total_mm // 10)
        mm = round(total_mm % 10)
        resultado = f"{expresion} =\n  {cm}cm {mm}mm"
    elif set(unidades).issubset({'cm', 'm'}):
        total_cm = total_metros * 100
        m = int(total_cm // 100)
        cm = round(total_cm % 100)
        resultado = f"{expresion} =\n  {m}m {cm}cm"
    elif set(unidades).issubset({'m', 'km'}):
        total_m = total_metros
        km = int(total_m // 1000)
        m = round(total_m % 1000)
        resultado = f"{expresion} =\n  {km}km {m}m"
    else:
        resultado = f"{expresion} = {total_metros} m"

    historial.append(resultado)
    if len(historial) > 10:
        historial.pop(0)

    return total_metros, resultado
    #upgrade 1.0.2 30/Marzo.25 
    #upgrade 1.0.3 30/Marzo.25 

def mostrar_historial(historial:List[str]):
    print("\n- - - - HISTORIAL - - - -")
    for idx, operacion in enumerate(historial, 1):
        print(f"{idx}. {operacion}")
    
def menu_sec_distancia():
    print("\n¿Qué deseas hacer ahora?")
    print("1. Realizar otra operación")
    print("2. Volver al menú principal")
    print("3. Salir")
    print("4. Ver historial")

    while True:
        opcion = input("Selecciona una opción (1-4): ")
        if opcion in {"1", "2", "3", "4"}:
            return int(opcion)
        print("Error: Ingresa un número entre 1 y 4.")
    #upgrade 1.0.3 30/Marzo.25

def start_Distancia():
    historial = []
    print("Calculadora de distancias (mm, cm, m, km\n")

    while True:
        entrada = input("Ingresa una suma. (ej. 5cm + 10mm) o ('historial' / 'salir') ").strip()
        if entrada.lower() == 'salir':
            print("\n")  # Espacio antes del mensaje
            loadScreen("... Saliendo del programa ...", 50)  # Delay
            loadScreen(" ¡Gracias por utilizar este proyecto! Vuelve pronto :) ", 50)
            print("\n")  # Espacio final
            break
        elif entrada.lower() == 'historial':
            mostrar_historial(historial)
            continue

        try:
            _, resultado = calcular_distancia(entrada, historial)
            print(f"\nResultado: {resultado}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    start_Distancia()


