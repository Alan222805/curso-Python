def devolver_distintos(n1:int, n2:int, n3:int):
    lista_numeros = [n1, n2, n3]
    suma = sum(lista_numeros)
    if suma > 15:
        return max(lista_numeros)
    elif suma < 10:
        return min(lista_numeros)
    elif suma >= 10 and suma <=15:
        return lista_numeros[1]
         
print(devolver_distintos(5,3,5))