# comment
# Delay en forma de mensaje, simula un tiempo de carga
# archivo delay_general.pay    - delay predeterminado   
#  
# Creado el: 27/05/2025    @Author coconutPineappl
# îî  version: 1.0.0  îî
#  PANTALLA DE CARGA
# Saliendo del programa

import time
def loadScreen(texto, delay_ms=200):
    #
    for char in texto:
        print(char, end='', flush=True) #flush=True asegura que se impriman inmediatamente
        time.sleep(delay_ms/1000) #convierte milisegundos a segundos
    print()