archivo = open("archivo1.txt", "r")
lista = archivo.read().split("\n")
print(len(lista))
for n in lista:
    print(n)
for l in archivo.read().split("\n"):
    print(l)