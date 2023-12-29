class carro(object):
    def __init__(self,m):
        self.color = "Rojo"
        self.puertas = 4
        self.tipo = "Deportivo"
        self.m = m
    def movilidad(self):
        if self.m == True:
            print("Acelerar")
        else:
            print("Frenar")

def main():
    while True:
        print("1.- Acelerar")
        print("2.- Frenar")
        valor = int(input("Ingrese una opcion: "))
        c = carro(valor)
        if valor == 1:
            c = carro(True)
            c.movilidad()
        else:
            c = carro(False)
            c.movilidad()
    # c = carro()
    # print(c.color)
    # print(c.puertas)
    # print(c.tipo)

if __name__ == '__main__':
    main()