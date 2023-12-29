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

def main():
    #De esta manera creamos un objeto siguiendo el molde de la clase de arriba
    #Lo que nos permite usar facilmente sus propiedades
    animal1 = animal('Perro','Nacho',2)
    animal2 = animal('Caballo','Juan',5)
    # Si solo usamos un print nos imprimira el espacio de memoria virtual que usa el objeto\
    print(animal1)
    print(animal2)
    # el objeto por lo que para poder acceder a sus datos lo haremos de la siguiente forma
    print(animal1.tipo) #Accedemos a un atributo y lo mostramos
    print(animal2.edad)
    animal1.accion() #Accedemos a un metodo no es necesario imprimirlo
    animal2.accion() #ya que el mismo metodo tiene sus funcionalidades

if __name__ == '__main__':
    main()
