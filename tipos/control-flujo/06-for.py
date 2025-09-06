for numero in range(5):
    print("Número:", numero)

for numero in range(2, 6):
    print("Número:", numero * 'hola mundo ')

buscar = 3

for numero in range(5):
    print("Número:", numero)
    if numero == buscar:
        print("Encontrado! ", buscar)
        break

buscar = 10

for numero in range(5):
    print("Número:", numero)
    if numero == buscar:
        print("Encontrado! ", buscar)
        break
else:
    print("No encontrado! ", buscar)

# Iterables son por ejemplos de listas, tuplas, diccionarios, sets y strings
for char in "Ultimate Python":
    print(char)
