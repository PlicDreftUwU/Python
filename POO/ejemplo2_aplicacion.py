import random
# Clase base para representar un Pokémon
class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = 100

    def atacar(self, oponente):
        pass

    def recibir_danio(self, danio):
        self.vida -= danio

    def esta_vivo(self):
        return self.vida > 0

# Clase para representar un Pokémon Rayquaza
class Rayquaza(Pokemon):
    def __init__(self):
        super().__init__("Rayquaza", "Volador/Dragón")

    def atacar(self, oponente):
        poder_aereo = random.randint(15, 25)
        print(f"{self.nombre} utiliza Ataque Aéreo con un poder de {poder_aereo}.")
        oponente.recibir_danio(poder_aereo)

# Clase para representar un Pokémon Pikachu
class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", "Eléctrico")

    def atacar(self, oponente):
        poder_electrico = random.randint(10, 30)
        print(f"{self.nombre} utiliza Ataque Eléctrico con un poder de {poder_electrico}.")
        oponente.recibir_danio(poder_electrico)

# Función para que el usuario elija su Pokémon
def elegir_pokemon(opcion):
    if opcion == '1':
        return Rayquaza()
    elif opcion == '2':
        return Pikachu()
    else:
        print("Opción no válida. Elige de nuevo.")
        return elegir_pokemon()

# Función para que el usuario decida si atacar o esperar durante su turno
def turno_usuario(usuario, oponente):
    print(f"Es tu turno, {usuario.nombre}!")
    print(f"Salud de {usuario.nombre}: {usuario.vida}")
    print(f"Salud de {oponente.nombre}: {oponente.vida}")
    
    print("¿Qué quieres hacer?")
    print("1. Atacar")
    print("2. Esperar")
    opcion = input("Ingresa el número de tu elección: ")
    
    if opcion == '1':
        usuario.atacar(oponente)
    elif opcion == '2':
        print(f"{usuario.nombre} está esperando y recuperando energía.")
    else:
        print("Opción no válida. Elige de nuevo.")
        turno_usuario(usuario, oponente)

# Función para simular una pelea entre el usuario y la computadora
def pelear(usuario, computadora):
    print(f"Comienza la batalla entre {usuario.nombre} y {computadora.nombre}!\n")
    turno_computadora = random.choice([True, False])
    
    while usuario.esta_vivo() and computadora.esta_vivo():
        if turno_computadora:
            # Turno de la computadora
            computadora.atacar(usuario)
            print(f"Salud de {usuario.nombre}: {usuario.vida}")
        else:
            # Turno del usuario
            turno_usuario(usuario, computadora)
        
        turno_computadora = not turno_computadora
    
    if usuario.esta_vivo():
        print(f"Felicidades, ¡{usuario.nombre} ha ganado!")
    else:
        print(f"¡{computadora.nombre} ha ganado!")

def main():
# Interacción con el usuario
    print("¡Bienvenido a la batalla Pokémon!")
    print("Elige tu Pokémon:")
    print("1. Rayquaza")
    print("2. Pikachu")
    opcion = input("Ingresa el número de tu elección: ")  
    usuario_pokemon = elegir_pokemon(opcion)
    #Usamos operador ternario
    computadora_pokemon = elegir_pokemon('2') if opcion == '1' else elegir_pokemon('1')
    # Iniciar la pelea
    pelear(usuario_pokemon, computadora_pokemon)

if __name__ == '__main__':
    main()