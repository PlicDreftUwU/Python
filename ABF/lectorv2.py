import os
import numpy as np
import matplotlib.pyplot as plt
from pymeta import ChannelABF

# Cargar el archivo ABF
def load_abf(abf_file):
    # Leer el archivo ABF
    abf = ChannelABF(abf_file)

    # Obtener los datos de tiempo, voltaje y duración de cada sweep
    data = np.zeros((abf.numPoints, abf.numSweeps))
    time = np.zeros((abf.numPoints, abf.numSweeps))
    sweepDuration = np.zeros(abf.numSweeps)

    for i in range(abf.numSweeps):
        data[:, i] = abf.sweepY[i]
        time[:, i] = abf.sweepTimes[i]
        sweepDuration[i] = abf.sweepTimes[i + 1] - abf.sweepTimes[i]

    return data, time, sweepDuration

# Graficar los datos del archivo ABF
def plot_abf(data, time, sweepDuration):
    plt.figure(figsize=(12, 8))

    for i in range(data.shape[1]):
        plt.plot(time[:, i], data[:, i], label=f'Sweep {i + 1}')
        plt.axvline(x=sweepDuration[i], color='k', linestyle='--', alpha=0.5)

    plt.xlabel('Tiempo (s)')
    plt.ylabel('Voltaje (mV)')
    plt.title('Archivo ABF')
    plt.legend()
    plt.show()

# Función principal
def main():
    abf_file = '22807000.abf' # Reemplaza esto con la ruta de tu archivo ABF
    if not os.path.exists(abf_file):
        print(f'Error: No se encuentra el archivo "{abf_file}"')
        return

    data, time, sweepDuration = load_abf(abf_file)
    plot_abf(data, time, sweepDuration)

if __name__ == '__main__':
    main()