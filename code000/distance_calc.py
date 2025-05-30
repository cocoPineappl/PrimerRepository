# || comment
# || Calculadora de funciones multiples 'CG'
# || archivo Main.pay    menu de General Option 
# || 
# ||  
# || Creado el: 26/05/2025    @Author coconutPineappl
# || îî  version: 1.0.0  îî
# ||  Calculadora de distancias mm, cm, m, km
# || Util para medir guardar medidas y consultar historial
# ||
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

def convertir_a_metros(valor:float, unidad:str) -> float:
    if unidad not in Unidades:
        raise ValueError(f"Unidad desconocida: {unidad}")
    return valor * Unidades[unidad]

    #upgrade 1.0.2 30/Marzo.25

def parsear_entrada(entrada:str) -> List[Tuple[float,str]]:
    patron= r'([\d.]+)\s*([a-zA-Z]+)'
    return [(float(valor), unidad.lower()) for valor, unidad in re.findall(patron,entrada)]

def calcular_distancia(entrada:str, historial:List[str]) -> Tuple[float,str]:
    valores_unidades = parsear_entrada(entrada)
    if not valores_unidades:
        raise ValueError("Formato invalido. Ejemplo:  '5cm + 10mm' ")
    total_metros = sum(convertir_a_metros(valor, unidad) for valor, unidad in valores_unidades)
    expresion = " + ".join(f"{valor} {unidad}" for valor, unidad in valores_unidades)
    resultado = f"{expresion} = {total_metros} m"
    historial.append(resultado)
    if len(historial) > 10:
        historial.pop(0)

    return total_metros, resultado

    #upgrade 1.0.2 30/Marzo.25 

def mostrar_historial(historial:List[str]):
    print("\n- - - - HISTORIAL - - - -")
    for idx, operacion in enumerate(historial, 1):
        print(f"{idx}. {operacion}")
    
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


