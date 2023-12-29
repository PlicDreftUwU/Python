array1 = []
array2 = []
arrayprueba = []
iterations = int(input('Cuantas palabras desea agregar: '))
for i in range (iterations):
    array1.append(input('Ingrese palabra: '))
for i in range(iterations):
    array2.append(array1[iterations-1 - i])
#Prueba nomas para lo loles xd
for palabra in array1:
    arrayprueba = [palabra] + arrayprueba
print(array1)
print(array2)
print(arrayprueba)