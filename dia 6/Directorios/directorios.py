import os
from pathlib import Path

""" nueva_ruta = os.chdir("C:\\Users\\Alanj\\OneDrive\\Escritorio\\alternativo") #Cambia la ruta del area de trabajo por la especificada
os.mkdir("C:\\Users\\Alanj\\OneDrive\\Escritorio\\alternativo\\otro") #Crea una carpeta con el nombre 'otro'
os.rmdir("C:\\Users\\Alanj\\OneDrive\\Escritorio\\alternativo\\otro") #Elimina la carpeta con el nombre 'otro' """
""" archivo = open('C:\\Users\\Alanj\\OneDrive\\Escritorio\\alternativo\\Otro_archivo.txt') 
print(archivo.read()) """
ruta = os.path.dirname('C:\\Users\\Alanj\\OneDrive\\Escritorio\\alternativo\\Otro_archivo.txt') #Obtiene la ruta completa especificada
nombre_archivo = os.path.basename('C:\\Users\\Alanj\\OneDrive\\Escritorio\\alternativo\\Otro_archivo.txt')#Obtiene el nombre del archivo especificado en la ruta

ruta_split = os.path.split('C:\\Users\\Alanj\\OneDrive\\Escritorio\\alternativo\\Otro_archivo.txt') #Devuelve una tupla con la dirname y basename como elementos.
print(ruta_split)
archivito = open(ruta + f'\\{nombre_archivo}')
print(archivito.read())

""" carpeta = Path('C:/Users/Alanj/OneDrive/Escritorio/alternativo') / "Otro_archivo.txt"

mi_archivo = open(carpeta)
print(mi_archivo.read()) """