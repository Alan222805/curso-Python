from pathlib import Path

""" base = Path.home()
# guia = Path(base, "Europa", "España", Path("Barcelona", "SagradaFamilia.txt"))
guia = Path(base, "Europa")

for a in guia.glob("**/*.txt"):
    print(a) """
    
guia = Path("Europa", "España", "Barcelona", "SagradaFamilia.txt")
en_europa = guia.relative_to(Path("Europa"))
en_espanha = guia.relative_to(Path("Europa", "España"))

print(en_europa)
print(en_espanha)


""" # EJERCICIO 1

ruta_base = Path.home()

# EJERCICIO 2

ruta1 = Path("Curso Python", "Día 6", "practicas_path.py")

# EJERCICIO 3
base = Path.home()
ruta2 = Path(base, "Curso Python", "Día 6", "practicas_path.py")


print(ruta1)
print(ruta2.with_name("hola")) """