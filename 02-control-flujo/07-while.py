# numero = 1
# while numero <= 100:
#     print(numero)
#     numero *= 2
# print("Ya fuera del while el número es: ", numero)

comando = ""
while comando.lower() != "salir":
    comando = input("Ingrese un comando: ")
    print("El comando ingresado es: ", comando)

# Loop infinito

while True:
    comando = input("Ingrese un comando: ")
    if comando.lower() == "salir":
        break
