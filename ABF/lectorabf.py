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

#------------------------------

# Extraer la duración del experimento (en segundos)
experiment_duration = abf.dataRate * abf.pointsPerScan * abf.sweepCount

# Extraer la información de los canales
channels = [
    {"name": "Channel 1", "color": "blue", "data": abf.data[:, 0]},
    {"name": "Channel 2", "color": "green", "data": abf.data[:, 1]},
    {"name": "Channel 3", "color": "red", "data": abf.data[:, 2]},
]

# Graficar los canales
plt.figure(figsize=(10, 6))

for channel in channels:
    plt.plot(
        np.arange(abf.pointsPerScan) / abf.dataRate,
        channel["data"],
        color=channel["color"],
        label=channel["name"],
    )

plt.title(f"{abf.protocol} (Sweep Count: {abf.sweepCount})")
plt.xlabel("Time (s)")
plt.ylabel("Membrane Potential (mV)")
plt.legend()
plt.show()