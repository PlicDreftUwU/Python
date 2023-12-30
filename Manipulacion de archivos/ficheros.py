from io import open
#Usar path absoluto
import pathlib as path
#Abrir archivo
# archivo = open("fichero.txt","a+")
#Abrir desde el directorio absoluto
ruta = str(path.Path().absolute()) + "/Manipulacion de archivos/fichero.txt" #--> Tener en cuenta la conversion
print ("Ruta del fichero: ", ruta)
archivo = open(ruta, "a+") #--> Tener en cuenta el permiso
#Escritura en un archivo
archivo.write('Este texto fue escrito con codigo\n')
#Cerrar archivo
archivo.close()

#-------------------Permiso de lectura----------------#
ruta = str(path.Path().absolute()) + "/Manipulacion de archivos/fichero.txt" #--> Tener en cuenta la conversion
print ("Ruta del fichero: ", ruta)
archivo_lec= open(ruta, "r+") #--> Tener en cuenta el permiso
#Leer contenido
# contenido = archivo_lec.read()
# print(contenido)
#Leer contenido y guardarlo en lista
lista = archivo_lec.readlines()
archivo_lec.close()
print('---------------')
for elemento in lista:
    print (elemento)
#Tener en cuenta de que ahora podemos manipular los datos de la lista
for frase in lista:
    if not frase.isnumeric():
        print ('No es numerico: ',frase) #--> Solo indicativo ya que dentro del txt todo es str
    else:
        print('Si es numerico: ' + frase.upper() + '\n')
#Usando split
for frase in lista:
    lista_frase = frase.split()
    print(lista_frase)