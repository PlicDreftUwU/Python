number = int(input('Desde que numero comienzo: '))
limite = int(input('Cuantas veces quieres que me repita: '))
for i in range(limite):
    number = (number + 1) * 2
    print(number)