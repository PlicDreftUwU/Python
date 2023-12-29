niveles = int(input('Ingrese el nivel de la piramide: '))
for i in range(niveles):
    print('\n')
    for j in range(i):
        print('*', end='')