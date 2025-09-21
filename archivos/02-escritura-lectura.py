from pathlib import Path

archivo = Path("archivos/mi_archivo.txt")
texto = archivo.read_text("utf-8").split("\n")
print(texto)

texto.insert(0, "Hola mundo")
archivo.write_text("n".join(texto), "utf-8")
print(texto)