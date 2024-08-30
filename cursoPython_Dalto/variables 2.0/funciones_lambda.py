# Sin funcion lambda

def sumar(n1, n2):
    return n1+n2

print(sumar(5,7))


# Con funcion lambda

suma = lambda n1, n2 : n1+n2

print(suma(5,7))


numeros = [1,2,3,4]
cuadrados = list(map(lambda numero : numero ** 2, numeros))
print(cuadrados)


pares = list(filter(lambda x : x%2==0, numeros))
print(pares)


puntos = [(1,2), (7,1), (5, -1)]
ordenados = sorted(puntos, key=lambda x:x[0])
print(ordenados)


datos_personales = {"nombre": "Alan", "apellido": "Sanchez", "edad": "21"}
datos_ordenados = sorted(datos_personales.keys(), key=lambda x : x)

print(datos_ordenados)