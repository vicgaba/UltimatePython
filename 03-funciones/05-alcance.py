saludo = "Hola global"

def saludar():
    saludo = "Hola mundo"
    print(saludo)

def saludaChanchito():
    saludo = "Hola Chanchito"
    print(saludo)

def saludoGlobal():
    global saludo
    saludo = "Hola desde la función"

print(saludo)
saludoGlobal()
saludar()
saludaChanchito()
saludar()
print(saludo)
