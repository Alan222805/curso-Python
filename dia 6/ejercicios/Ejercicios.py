'''
EJERCICIO 1
Crea una función llamada abrir_leer() que abra (open) un archivo 
indicado como parámetro, y devuelva su contenido (read).
'''

import os
def abrir_leer(archivo:str):
    archivoAbrir = os.open('archivo', 'r')
    return archivoAbrir.read()

'''
EJERCICIO 2
Crea una función llamada sobrescribir() que abra (open) un 
archivo indicado como parámetro, y sobrescriba cualquier contenido 
anterior por el texto "contenido eliminado"
'''
def sobrescribir(archivo:str):
    archivoAbrir = open(archivo, 'w')
    archivoWrite = archivoAbrir.write("contenido eliminado")
    
'''
EJERCICIO 3
Crea una función llamada registro_error() que abra (open) un archivo
indicado como parámetro, y lo actualice añadiendo una línea al final 
que indique "se ha registrado un error de ejecución". Finalmente, 
debe cerrar el archivo abierto.
'''

def registro_error(name_file:str):
    archivo = open(name_file, 'a')
    archivo_modificado = archivo.write("se ha registrado un error de ejecución")
    archivo.close()
    
    
from pathlib import Path    
ruta = Path('C:/Users/Usuario/Desktop/Curso Python') / 'Cuestionario Día 6' / 'Pregunta 1'
print(ruta)