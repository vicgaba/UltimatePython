#kwargs key words arguments
def get_product(**datos):
    print(datos)
    print(datos["name"], datos["desc"])

get_product(id="id", 
            name="iPhone", 
            desc="Esto es un iPhone") # cuando se usa ** debe enviaar el nombre del parametro