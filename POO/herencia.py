#Clase = Define un conjunto de atributos y metodos
class animal:
    #Esta funcion se conoce como constructor y se necesita inicializar con un "INIT" determinando
    #el constructor
    def __init__(self,tipo,nombre,edad) -> None:
        #Self se usa para referirse al mismo objeto y asi acceder a sus atributos
        #Los atributos son inicializados en el constructor
        self.tipo = tipo
        self.nombre = nombre
        self.edad = edad
    #La siguiente funcion la definimos como un metodo
    def accion(self):
        print('Hola soy un {} mi nombre es {} y tengo {} anios'.format(self.tipo,self.nombre,self.edad))

#Definimos una nueva clase que heredara los atributos de la clase anterior la cual pondremos entre parentesis
class cartoon_Character(animal): #La clase dentro de los parentesis sera la que seda sus atributos
    def __init__(self, tipo, nombre, edad,programa) -> None:
        # super sera usado para inicializar los atributos de la clase padre
        # heredando asi tanto sus atributos como sus metodos
        # es importante no olvidar esta parte y que de no existir podria haber errores
        super().__init__(tipo, nombre, edad)
        self.programa = programa
    def impresion(self):
        print("Soy un personaje del tipo {},mi nombre es {},tengo {} años vengo del programa {}".format(self.tipo,self.nombre,self.edad,self.programa))

def main():
    # Creamos el objeto que recibira atributos heredados de la clase animal
    personaje = cartoon_Character('Anime','Luffy',17,'One piece')
    # Accedemos a la informacion dentro del objeto como en la clase anterior
    print(personaje.nombre)
    print(personaje.programa)
    #Accedemos al metodo
    personaje.impresion()
    #En este caso el objeto tambien heredo los metodos de la clase animal
    # por lo que podriamos ocuparlo, en este caso el mensaje no tiene sentido
    # asi que se debe de tener en cuenta cuando es bueno usar la herencia
    personaje.accion()
if __name__ == '__main__':
    main()