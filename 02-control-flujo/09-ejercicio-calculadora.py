"""verificar si ya a ingresado un número, si no, solicitarlo y si lo había ingresado, 
pedir que ingrese una operación
Ahora que ingrese otro número
Mostrar el resultado y enviarlo al primer número """

n1 = None
comando = ""

print(""""Bienvenido a la calculadora
Ingrese 'salir' en cualquier momento para terminar
Las operaciones disponibles son: suma, resta, multi y div""")
while True:
    if n1 is None:
        n1 = input("Ingrese un número: ")
        if n1.lower() == "salir":
            break
        n1 = float(n1)
    comando = input("Ingrese una operación: ")
    if comando.lower() == "salir":
        break
    n2 = input("Ingrese siguiente número: ")
    if n2.lower() == "salir":
        break
    n2 = float(n2)
    if comando == "suma":
        n1 += n2
    elif comando == "resta":
        n1 -= n2
    elif comando == "multi":
        n1 *= n2
    elif comando == "div":
        n1 /= n2
    else:
        print("Operación no válida")
        break
    print(f"El resultado es: {n1}")
print("Gracias por usar la calculadora")
