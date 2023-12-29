array = [20, 15, 12, 11, 8, 4, 1]
array.sort()
print(array[0])
array.remove(array[0])
suma = 0
for i in array:
    suma += i
print(suma/len(array))