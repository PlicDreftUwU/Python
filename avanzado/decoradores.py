class prueba(object):
    def __init__(self,radio):
        self.radio = radio
    @classmethod #Podemos llamar una funcion sin necesidad de que la clase sea atribuida a un objeto
    def saludo(cls,nombre):
        print("Hola {}".format(nombre))
    @staticmethod #Nos permite crear funciones sin argumentos
    def saludo_static():
        print("Bienvenido")
    @property
    def area_Circulo(self):
        return 3.1416 * (self.radio**2)
def main():
    nombre = input("Ingresa tu nombre: ")
    prueba.saludo(nombre)
    c = prueba(5)
    c.saludo_static()
    area = c.area_Circulo
    print(area)
if __name__ == '__main__':
    main()