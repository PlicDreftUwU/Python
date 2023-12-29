names = []
long = []
size = int(input('Cuantos nombres desea ingresar al arreglo: '))
for i in range(size):
    names.append(input('Ingrese el nombre desado: '))
    long.append(len(names[i]))
print(names)
print(long)