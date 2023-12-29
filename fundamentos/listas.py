#Se pueden agregar cosas por medio de un for
#Se puede definir con list o con corchetes
lista = [1,2,3,4,'Hola mundo',5]
#Podemos crear una cadena de caracteres apartir del contenido de una lista
listapalabra = ['h','o','l','a']
listapalabra = ''.join(listapalabra)
print(listapalabra)
#Lo recorremos con un for
for l in lista:
    print(l)
#Si no conocemos el tamanio de una lista
print(lista[len(lista)-1])
#Eliminando un dato de la lista
lista.pop()
print(lista)
#Se puede eliminar un dato especifico usando del
del lista[1]
#Podemos recorrer las lugares que queramos
print(lista[0:4])
#Podemos agregar valores a una lista
for n in range(90,100):
    lista.append(n)
print(lista)