bandera = 0
while bandera == 0:
    n1 = int(input('Ingrese un numero: '))
    n2 = int(input('Ingrese un numero: '))
    res = n1 + n2
    print(res)
    if res < 0:
        bandera = 1