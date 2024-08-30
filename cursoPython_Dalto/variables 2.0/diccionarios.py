#creando un diccionario con dict()

diccionario = dict(nombre="Alan", apellido="Sanchez", edad=21)

print(diccionario)


#Creando diccionarios con fromkeys() valor por defecto: none
diccionario = dict.fromkeys(["nombre", "apellido"])
print(diccionario)

# Creando diccionarios con fromkeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre", "apellido"], "no se")
print(diccionario)