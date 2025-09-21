def hola():
    print("Hola mundo")
    print("Ultimate Python")


hola()


def hola1(name):  # name dentro de la función se llama parámetro
    print("Hola mundo")
    print(f"Bienvenido {name}")  # Acá hacemos uso del parámetro


hola1("Juan")  # Cuando llamamos a la función le enviamos Argumentos, fuera de la función no se llaman parámtros


def hola2(name, surname):
    print("Hola mundo")
    print(f"Bienvenido {name} {surname}")


hola2("Chanchito", "Feliz")

# Argumentos opcionales


def hola3(name, surname=""):
    print("Hola mundo")
    print(f"Bienvenido {name} {surname}")


hola3("Chanchito")

hola3(surname = "Feliz2", name = "Chanchito2")