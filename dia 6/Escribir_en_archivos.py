"""archivo = open('dia 6/prueba2.txt', 'a')

 archivo.write('''Hola
Mundo
Estoy 
Aqui
''') """

""" palabras = ["Hola", "Mundo","estoy", "aqui"]

for palabra in palabras:
    archivo.write(palabra + '\n') 
    
archivo.write('¿Como estan?')



archivo.close()
"""


# EJERCICIO 1

archivo = open('dia 6/mi_archivo.txt', 'w')

archivo.write("Nuevo texto")

archivo.close()

archivo = open('dia 6/mi_archivo.txt')

print(archivo.read())

archivo.close()


# EJERCICIO 2
archivo = open('dia 6/mi_archivo.txt', 'a')

archivo.write("\nNuevo inicio de sesión")

archivo.close()

archivo = open('dia 6/mi_archivo.txt')

print(archivo.read())

archivo.close()

# EJERCICIO 3
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
archivo = open('dia 6/mi_archivo.txt', 'a')
for registro in registro_ultima_sesion:
    archivo.write(registro + '\t')
archivo.close()

archivo = open('dia 6/mi_archivo.txt')
print(archivo.read())
archivo.close()