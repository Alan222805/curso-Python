""" from random import randint

numeros = [50, 14, 64, 34, 5]

print(max(numeros))
print(min(numeros))

nombres = ['juan', 'pablo', 'HelEn', 'carlos']
numero_random = randint(0, len(nombres)-1)
nombre = nombres[numero_random]
print(numero_random)
print(f"Nombre: {nombre} => letra: {min(nombre.lower())}") """

dic = {'C1': 45, 'C2': 11}

print(min(dic.items())[1])