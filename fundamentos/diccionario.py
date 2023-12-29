diccionario = dict(nombre="PlicDreft",plataforma="Poderosa UATX",edad="16")
print(diccionario['plataforma'])
#items devuelve la llave y el valor en una tupla
items = diccionario.items()
print(items)
#copy
diccionario_copia = diccionario.copy()
print(diccionario_copia)
#keys muestra solo las llaves
solo_llaves = diccionario.keys()
print(solo_llaves)
#values muestra solo los valores
solo_values = diccionario.values()
print(solo_values)
# # recorremos con for
for n in diccionario.keys():
    print('{} Su valor es: {}'.format(n,diccionario[n]))
#Forzando un error
# p = diccionario.nombre()
# print(p)
#Metodo get
valor=diccionario.get('nombre')
print(valor)
#Metodo pop
poppedValue = diccionario.pop('nombre')
print(poppedValue)
print(diccionario.values())
#Metodo clear
diccionario.clear()
print(diccionario)