archivo = open("archivo1.txt","w")
nombre = input("Nombre: ")
edad = input("Edad: ")
pais = input("Pais: ")

archivo.write(nombre)
archivo.write("\n")
archivo.write(edad)
archivo.write("\n")
archivo.write(pais)

print("Termine")

archivo.close()