import time
import signal
import sys

# Definir la tarea que se ejecutará

class ThreadBursatil():
    
    def __init__(self):
        while True:
            self.tarea()
            time.sleep(10)  # Esperar 10 segundos

    def tarea(sefl):
        print("Ejecutando tarea...")

        # Función para manejar la señal de terminación
    def signal_handler(sig, frame):
        print('Señal recibida, finalizando proceso...')
        sys.exit(0)  # Finaliza el programa con código 0 (éxito)

    # Asignar la señal de interrupción (Ctrl + C) al manejador
    signal.signal(signal.SIGINT, signal_handler)  # Ctrl + C
    signal.signal(signal.SIGTERM, signal_handler)  # Señal de fin

    # Bucle para ejecutar la tarea cada 10 segundos
    