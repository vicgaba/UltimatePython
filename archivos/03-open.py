from io import open

# escritura
# texto = "Hola mundo!"

# archivo = open("archivos/hola-mundo.txt", "w") # si el archivo no existe python lo crea
# archivo.write(texto)
# archivo.close() # Debemos cerrar el archivo ya que open lo deja abierto 

# lectura
# archivo = open("archivos/hola-mundo.txt", "r")
# texto = archivo.read() 
# print(texto)
# archivo.close()

# archivo = open("archivos/hola-mundo.txt", "r")
# texto = archivo.readlines()
# print(texto)
# archivo.close()

# with y seek
# with open("archivos/hola-mundo.txt", "r") as archivo: # con with se cierra automaticamente 
#     print(archivo.readlines())
#     archivo.seek(0) # volvemos al inicio del archivo
#     for linea in archivo:
#         print(linea)

# agregar
# archivo = ("archivos/hola-mundo.txt", "a+") # si el archivo no existe python lo crea
# archivo.write("\nChau mundo")
# archivo.close()

# lectura y escritura 
with open("archivos/hola-mundo.txt", "r+") as archivo: # si el archivo no existe python lo crea
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0] = "Chanchito feliz"
    archivo.writelines(texto)