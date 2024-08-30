from pathlib import Path

ruta = Path("cursoPython_Dalto", "trabajar con archivos")/ "x.txt"

with open(ruta, "w", encoding="UTF-8") as archivo:
    archivo.write("Nuevo texto desde python\nmanteniendo el anterior")
    archivo.writelines(["\nUltimo cambio", "\nDesde python"])
    