import pyabf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
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
#Comprobamos que haya más de un dato para poder trabajar
if abf.sweepCount > 0:
    # Obtenemos dimensiones de los datos
    dimensiones = abf.sweepY
    print('Dimensiones Datos: ',dimensiones.shape)
    # Obtener datos del tiempo solo para corroborar
    tiempo = np.transpose(abf.sweepX)
    np.transpose(tiempo)
    print('Dimensiones tiempo: ',tiempo.shape)
    # Definimos una matriz para poder ingresarla a un DataFrame
    abf.setSweep(sweepNumber=0,channel=2)
    dataMatrix = np.array([abf.sweepY])
    dataMatrix = np.transpose(dataMatrix)
    # DataFrame con pandas
    df = pd.DataFrame(dataMatrix, columns = ['Datos'])
    # Eliminamos los datos de los primeros 4 segundos
    df = df.drop(df.index[:4000])
    # Encontramos el valor mas pequeño del DataFrame
    print(f'Min Value: {df.min().min()}')
    # Graficamos cada canal para obtener la informacion en graficas independientes
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