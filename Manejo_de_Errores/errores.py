from typing import IO
try:
    raise IOError #Genera errores a gusto
except IOError:
    print("Ocurrio un error")
    while True:
        print("hola")
except NameError: #Se controla el nombre del error
    print("L no esta definida")
except KeyboardInterrupt: #Se interrumpe la corrida de un programa al presionar una tecla
    print("Salida forzosa")
finally:
    print("Se termino la ejecucion")