#Creamos una clase que funcionara basicamente como un molde para un animal
class Animal:
    #El metodo hablar de la clase animal realmente no tiene ningun comportamiento pre establecido
    def hablar(self):
        pass
#Creamos un molde para crear perros que heredan el metodo "Hablar" de la clase animal
class Perro(Animal):
    #En la clase perro el metodo heredado toma una funcion
    def hablar(self):
        return "Guau!"
#Creamos un molde para crera gatos que heredan igualmente el metodo "Hablar"
class Gato(Animal):
    #En la clase gato el metodo vuelve a tomar otra funcion
    def hablar(self):
        return "Miau!"
#Creamos esta funcion que toma un objeto de tipo "Animal" e invocando su metodo
def hace_hablar(animal):
    print(animal.hablar())

# El polimorfismo nos permite cambiar la naturaleza de un metodo heredado, lo que nos permite 
# cambiar el comportamiento del método en cualquier momento sin tener que modificarlo

#Creamos 2 objetos de tipo animal
mascota1 = Perro()
mascota2 = Gato()

# Al recibir un tipo de animal u otro el comportamiento del metodo cambia de forma automatica
hace_hablar(mascota1)
hace_hablar(mascota2)
