#Definimos una clase sencilla
class MiClase:
    def __init__(self):
        # Para restringir/encapsular/prohibir un atributo para que sea de uso
        # exclusivo de la clase el nombre empieza con un "_"
        self._atributo_protegido = 42
    # Este mismo principio funciona para los metodos aun que se aplica en el nombre
    # del metodo
    def _metodo_protegido(self):
        print("Este es un método protegido.")
    # Si tratamos de usar la herencia nos saldra un error ya que los atributos y metodos
    # son de uso exclusivo de la clase "MI CLASE"

objeto = MiClase()
print(objeto._atributo_protegido)  # Aunque es posible, no se recomienda acceder así
objeto._metodo_protegido()         # Aunque es posible, no se recomienda llamar así