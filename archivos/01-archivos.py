from pathlib import Path
from time import ctime

archivo = Path("archivos/mi_archivo.txt")

# archivo.exists()  # Verifica si el archivo existe
# archivo.rename("nuevo_nombre.txt")  # Cambia el nombre del archivo
# archivo.unlink()  # Elimina el archivo

#print(archivo.stat())
print("acceso: ", ctime(archivo.stat().st_atime))
print("modificacion: ", ctime(archivo.stat().st_mtime))
print("creacion: ", ctime(archivo.stat().st_ctime))