import pyabf
import matplotlib.pyplot as plt
import numpy as np

# Ruta al archivo ABF
ruta_archivo_abf = 'ABF/22807000.abf'

# Cargar el archivo ABF
abf = pyabf.ABF(ruta_archivo_abf)

# Imprimir información sobre el archivo
print("Informacion del archivo ABF:")
print(f"Nombre del archivo: {abf.abfID}")
print(f"Duracion del experimento: {abf.sweepLengthSec} segundos")
print(f"Frecuencia de muestreo: {abf.dataRate} Hz")
print(f"Numero de sweeps: {abf.sweepCount}")

if abf.sweepCount > 0:
    # Obtener todos los datos de los canales
    todos_los_datos = abf.sweepY
    dimensiones = todos_los_datos.shape
    print('Dimensiones Datos: ',dimensiones)
    # Obtener tiempo
    tiempo = np.transpose(abf.sweepX)
    np.transpose(tiempo)
    dimensiones_tiempo = tiempo.shape
    print('Dimensiones tiempo: ',dimensiones_tiempo)
    # Hacer algo con los datos, por ejemplo, trazarlos usando Matplotlib
    plt.figure(figsize=(10, 6))
    for i in range(abf.channelCount):
        plt.plot(tiempo, todos_los_datos, label=f'Canal {i+1}')
    plt.title("Datos de todos los canales durante el experimento")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Datos de la señal")
    plt.legend()
    plt.show()
else:
    print("No hay sweeps en el archivo ABF.")