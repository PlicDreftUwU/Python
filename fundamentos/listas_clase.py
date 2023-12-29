#Definimos arreglo
arreglo = []
arreglo = [1,2,3,4]
#Imprimimos el arreglo completo
print(arreglo)
#Imprimimos solo un dato del arreglo
print(arreglo[2])
#Agregar datos a un arreglo
agregar = int(input('Ingrese un numero para ingresar en el arreglo: '))
arreglo.append(agregar)
print(arreglo)
#Imprimir arreglo de derecha a izquierda
print(arreglo[::-1])
#Limpiar arreglo completo
arreglo.clear()
print(arreglo)
#Extender arreglo
arreglo = [1,2,3]
arreglo2 = [4,5,6,6,6,7,1,115]
# arreglo = arreglo + arreglo2
arreglo.extend(arreglo2)
print(arreglo)
#Contando items de un arreglo
print(arreglo.count(6))
#Retornar indice de un objeto
print(arreglo.index(4))
#Ingresar objeto en cualquier posicion
arreglo.insert(0,'Hola mundo')
print(arreglo)
#Eliminar el ultimo objeto
arreglo.pop()
print(arreglo)
#Eliminar un dato en especifico segun su indice
arreglo.pop(0)
print(arreglo)
#Eliminar un dato en especifico dentro del arreglo
arreglo.remove(6)
print(arreglo)
#Imprimir un arreglo al reves y opciones
arreglo.reverse()
print(arreglo)
#Ordenar objetos de un arreglo de menor a mayor
arreglo.sort()
print(arreglo)
#Ordenar objetos de un arreglo de mayor a menor
arreglo.sort(reverse=True)
print(arreglo)
#Saber cuantos objetos tiene un arreglo
print(len(arreglo))
#Iterando un arreglo 
for i in range(len(arreglo)):
    print("El valor en la posicion ",i," es ",arreglo[i])