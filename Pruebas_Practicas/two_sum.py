def two_Sum(array,target):
    for i in array:
        for j in array:
            plus = i + j
            i_Temp = numbers.index(i)
            j_Temp = numbers.index(j)
            if plus == target:
                equal = [i_Temp, j_Temp]
                return equal
            elif i == len(array) and j == len(array):
                if plus != target:
                    print("No se puede obtener el objetivo con los datos proporcionados")
            else:
                print('{}. resultado = {}'.format(i,plus))

def array_numbers():
    numbers = []
    opc = 1
    while(opc != 0):
        loop = int(input('Cuantos numeros desea agregar: '))
        if loop < 0:
            print('La cantidad de numeros es incorrecta ingresar un numero positivo \n intente nuevamente')
        else:
            for i in range(loop):
                number = float(input('\nIngrese el valor del numero {}: '.format(i+1)))
                numbers.append(number)
            return numbers
            break

numbers = array_numbers()
print(numbers)
target = int(input('Ingrese el resultado de la suma objetivo: '))
equal = two_Sum(numbers, target)
print(equal)