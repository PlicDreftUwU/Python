def resta(n1,n2, operacion = 'resta'):
    print("\nEl resultado es: {}".format(n1-n2))
    print(operacion)

def suma(n1, n2):
    print("\nEl resultado es: {}".format(n1+n2))

def mul(n1, n2):
    print("\nEl resultado es: {}".format(n1*n2))

def div(n1, n2):
    print("\nEl resultado es: {}".format(n1/n2))

def main():
    while True:
        print("\nBienvenido \n")
        print("1.- Suma")
        print("2.- Resta")
        print("3.- Multiplicacion")
        print("4.- Division")
        print("5.- Salir")
        opc = int(input("Ingrese una opcion: "))
        if opc == 1:
            n1 = int(input("Ingrese valor 1: "))
            n2 = int(input("Ingrese valor 2: "))
            suma(n1,n2)
        elif opc == 2:
            n1 = int(input("Ingrese valor 1: "))
            n2 = int(input("Ingrese valor 2: "))
            resta(n1, n2)
        elif opc == 3:
            n1 = int(input("Ingrese valor 1: "))
            n2 = int(input("Ingrese valor 2: "))
            mul(n1, n2)
        elif opc == 4:
            n1 = int(input("Ingrese valor 1: "))
            n2 = int(input("Ingrese valor 2: "))
            div(n1, n2)
        elif opc == 5:
            print("Nos vemos pronto!")
            exit()
        else:
            print("\nDigita una opcion correcta\n")

if __name__ == '__main__':
    main()