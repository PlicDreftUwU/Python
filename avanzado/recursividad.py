def jugar(intento = 3):
    respuesta = (input('De que color es una naranja?: '))
    respuesta = respuesta.lower()
    if respuesta != 'naranja':
        print('Incorrecto las naranjas no son de color {}'.format(respuesta))
        if intento > 0:
            print ('\n Sigue intentando!')
            intento -= 1
            #Recursividad
            jugar(intento) #La funcion se llama a si misma para poder volver a ejecutarse
        else:
            print('Has agotado todas tus vidas')
    else:
        print('Ganaste')

def main():
    jugar()

if __name__ == '__main__':
    main()