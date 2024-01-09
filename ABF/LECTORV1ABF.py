import pyabf
import matplotlib.pyplot as plt
import numpy as np

# Ruta al archivo ABF
ruta_archivo_abf = 'ABF/15n24009.abf'

# Cargar el archivo ABF
abf = pyabf.ABF(ruta_archivo_abf)

# Imprimir información sobre el archivo
print("Informacion del archivo ABF:")
print(f"Nombre del archivo: {abf.abfID}")
print(f"Duracion del experimento: {abf.sweepLengthSec} segundos")
print(f"Frecuencia de muestreo: {abf.dataRate} Hz")
print(f'Numero de canales: {abf.channelCount}')
print(f"Numero de sweeps: {abf.sweepCount}")

if abf.sweepCount > 0:
    # Obtener todos los datos de los canales
    todos_los_datos = abf.sweepY
    # Dividimos los datos en arreglos diferentes
    # canal1 = abf.sweepY.choose[0,:]
    # canal2 = abf.sweepY[1]
    # canal3 = abf.sweepY[2]
    # print(canal1.shape)
    # Mostramos la cantidad de datos
    
    dimensiones = todos_los_datos.shape
    print('Dimensiones Datos: ',dimensiones)
    # Obtener tiempo
    tiempo = np.transpose(abf.sweepX)
    np.transpose(tiempo)
    dimensiones_tiempo = tiempo.shape
    print('Dimensiones tiempo: ',dimensiones_tiempo)
    # Hacer algo con los datos, por ejemplo, trazarlos usando Matplotlib
    fig, axs = plt.subplots(abf.channelCount,1,figsize=(10,6))
    for i in range(abf.channelCount):
        abf.setSweep(sweepNumber=0,channel=i)
        axs[i].plot(abf.sweepX, abf.sweepY, label=f'Canal {i+1}')
        axs[i].set_title(f"Datos del canales {i+1} durante el experimento")
        axs[i].set_xlabel("Tiempo (s)")
        axs[i].set_ylabel("Datos de la señal")
        axs[i].legend()
    fig.tight_layout()
    plt.show()
else:
    print("No hay sweeps en el archivo ABF.")