from pathlib import Path

nombres = ["Alan", "Emmanuel", "Daniela"]
apellidos = ["Sanchez", "Arias", "Lucio"]

ruta_archivo = Path('dia 6', 'nombre_apellidos', 'nombres_apellidos.txt')

with open(ruta_archivo, 'w') as arch:
    arch.writelines("Los datos son: ".center(20, '-'))
    arch.writelines(f"\nNombre: {n}, Apellido: {a} \n" for n,a in zip(nombres, apellidos))