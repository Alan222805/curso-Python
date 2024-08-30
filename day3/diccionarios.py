"""cliente = {'name':'Juan', 'apellido': 'Fuentes', 'Peso': 88, 'talla': 1.76}
consulta = cliente['name']
print(consulta)

diccionario = {'c1':55, 'c2':[10,20,30], 'c3': {'s1': 100, 's2': 200}}
print(diccionario['c3']['s1'])


dic = {1:'a', 2:'b'}
print(dic)

dic[3] = 'c'
print(dic)


print(dic.values())
print(dic.items())

print('b' in dic.keys()) """


datos_personales = {
    "nombre": "Alan",
    "apellido": "Sanchez",
    "edad": 21
}

for k, v in datos_personales.items():
    print(f"La clave es: '{k}' y el valor es: {v}")
    
for e in enumerate(datos_personales.items()):
    print(e)
