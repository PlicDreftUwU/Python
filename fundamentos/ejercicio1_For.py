tabla = int(input('Ingrese la tabla deseada: '))
multiplo = int(input('Ingresa hasta que multiplo desea la tabla: '))
for i in range(multiplo+1):
    multiplicacion = tabla *  i
    print('{} x {} =  {}'.format(tabla,i,multiplicacion))