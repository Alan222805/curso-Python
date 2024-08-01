""" nombres = ["Alan", "Juan", "Mariana", "Julieta", "Amanda"]

for nombre in nombres:
    if nombre.startswith('A'):
        print(nombre)
else:
    print("son todos los nombres")
        
        
numeros = [1,2,3,4,5]
suma = 0

for numero in numeros:
    suma += numero

print(f"La suma de todos mis numeros es de {suma}")


objetos = [[1,2], [3,4], [5,6]]

for objeto1, objeto2 in objetos:
    print(objeto1)
    print(objeto2)
    
    
dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}
for item in dic.items():
    print(item)
    
for clave, valor in dic.items():
    print(clave, valor)
"""

nombre = "Rodrigo"
for letra in nombre:
    if letra == 'i':
        continue
    print(letra)