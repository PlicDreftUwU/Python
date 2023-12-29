import pyabf
import matplotlib.pyplot as plt
import numpy as np
# Ruta al archivo ABF
ruta_archivo_abf = '22807000.abf'

# Cargar el archivo ABF
abf = pyabf.ABF(ruta_archivo_abf)

# Imprimir información sobre el archivo
print("Informacion del archivo ABF:")
print(f"Nombre del archivo: {abf.abfID}")
print(f"Duracion del experimento: {abf.sweepLengthSec} segundos")
print(f"Frecuencia de muestreo: {abf.dataRate} Hz")
print(f"Numero de sweeps: {abf.sweepCount}")

if abf.sweepCount > 0:
    # Obtener datos de los tres canales durante la primera sweep
    datos_canal_1 = abf.sweepY[0]  # Canal 1
    datos_canal_2 = abf.sweepY[1]  # Canal 2
    datos_canal_3 = abf.sweepY[2]  # Canal 3

    # Obtener tiempo
    tiempo = abf.sweepX

    # Hacer algo con los datos, por ejemplo, trazarlos usando Matplotlib
    plt.figure(figsize=(10, 6))
    plt.plot(tiempo, datos_canal_1, label='Canal 1')
    plt.plot(tiempo, datos_canal_2, label='Canal 2')
    plt.plot(tiempo, datos_canal_3, label='Canal 3')
    plt.title("Datos de tres canales durante la primera sweep")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Datos de la señal")
    plt.legend()
    plt.show()
else:
    print("No hay sweeps en el archivo ABF.")