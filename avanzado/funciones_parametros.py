def saludo(name,age):
    print("Hola {} veo que tienes {} anios".format(name,age))

def main():
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    saludo(nombre,edad)

if __name__ == '__main__':
    main()