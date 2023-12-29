def pokemon():
    # Clase base para representar un Pokémon
    class Pokemon:
        def __init__(self, nombre, tipo):
            self.nombre = nombre
            self.tipo = tipo

        def atacar(self):
            pass

    # Clase para representar a Rayquaza, que hereda de Pokémon
    class Rayquaza(Pokemon):
        def __init__(self, nombre, tipo, poder_aereo):
            super().__init__(nombre, tipo)
            self.poder_aereo = poder_aereo

        def atacar(self):
            return f"{self.nombre} utiliza Ataque Aéreo con un poder de {self.poder_aereo}."

    # Clase para representar a un Entrenador
    class Entrenador:
        def __init__(self, nombre):
            self.nombre = nombre
            self.equipo = []
        def agregar_pokemon(self, pokemon):
            self.equipo.append(pokemon)

        def entrenar_pokemon(self):
            while True:
                print('Equipo Actual')
                cont = 1
                for pokemon in self.equipo:
                    print(f"{cont}.- {pokemon.nombre}")
                    cont += 1
                opc = int(input('A que pokemon desea entrenar: '))
                opc -= 1
                print(f"{self.nombre} entrena a {self.equipo[opc].nombre}:")
                print(pokemon.atacar())
                print("-" * 30)
                opc = input('Desea salir? S/N: ')
                if opc.lower() == 's':
                    break
            # for pokemon in self.equipo:
            #     print(f"{self.nombre} entrena a {pokemon.nombre}:")
            #     print(pokemon.atacar())
            #     print("-" * 30)

    # Crear un Pokémon Rayquaza
    rayquaza = Rayquaza("Alex", "Volador/Dragón", 200)
    rayquaza2 = Rayquaza("Puffy", "Volador/Dragón", 200)
    # Crear un Entrenador y agregar a Rayquaza a su equipo
    entrenador = Entrenador("PlicDreft")
    entrenador.agregar_pokemon(rayquaza)
    entrenador.agregar_pokemon(rayquaza2)

    # Entrenar al Pokémon Rayquaza
    print(f"{entrenador.nombre} entrena a su equipo:")
    entrenador.entrenar_pokemon()

def main():
    pokemon()

if __name__ == '__main__':
    main()