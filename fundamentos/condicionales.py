edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Felicidades!, eres mayor de edad")
else:
    print("Lo siento no eres mayor de edad")
if edad < 20:
    print("Eres menor de 20 anios")
elif edad == 20:
    print("Tienes 20 anios")
else:
    print("Tienes mas de 20 anios")
# If pero con cadenas de caracteres
nombre = str(input("Ingresa tu nombre: "))
if nombre == "Francisco":
    print("El nombre coincide")
else:
    print("El nombre no es el mismo")