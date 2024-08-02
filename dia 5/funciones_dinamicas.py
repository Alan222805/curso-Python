""" def chequear_3_cifras (lista):
    lista_3_cifras = []
    for n in lista:
        if n in range(100, 1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras

numeros = [505, 6000, 452]
resultado = chequear_3_cifras(numeros)
print(resultado) """

# EJERCICIO 1

lista_numeros = [1, 50, 502, 755, 34]
def todos_positivos(lista:list):
    for n in lista:
        if n > 0:
            continue
        elif n < 0:
            return False
    return True
print(todos_positivos(lista_numeros))

# EJERCICIO 2
def suma_menores(lista:list):
    suma = 0
    for n in lista:
        if n > 0 and n < 1000:
            suma += n
        else:
            pass
    return suma
print(suma_menores(lista_numeros))
# EJERCICIO 3
def cantidad_pares(lista:list):
    pares = 0
    for n in lista:
        if n%2==0:
            pares += 1
    return pares
print(cantidad_pares(lista_numeros))