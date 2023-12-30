from io import open
#Usar path absoluto
import pathlib as path
#Abrir archivo
# archivo = open("fichero.txt","a+")
#Abrir desde el directorio absoluto
ruta = str(path.Path().absolute()) + "/fichero.txt" #--> Tener en cuenta la conversion
print ("Ruta del fichero: ", ruta)
archivo = open(ruta,'a+')
#Escritura en un archivo
archivo.write('Ejemplo')