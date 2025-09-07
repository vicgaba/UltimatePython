nombre_curso = "Ultimate Python"
descripcion_curso = """
Ulitmate Python es un curso de Python avanzado.
En este curso aprenderas a usar Python para crear aplicaciones web.
"""
print(nombre_curso, descripcion_curso)
print(len(nombre_curso), len(descripcion_curso))  # 97
print(nombre_curso[0])  # U
print(nombre_curso[0:8])  # l le paso desde donde y cuantos caracteres quiero
# Python le paso desde donde quiero que extraiga y como no tiene fin, extrae hasta el final
print(nombre_curso[9:])
print(nombre_curso[:8])  # Ultimate
print(nombre_curso[:])
print(nombre_curso[-1])  # n
print(nombre_curso[-6:])  # Python
