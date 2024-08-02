def suma(*args):
    return sum(args)

print(suma(5,6,7,2))


# EJERCICIO 1

def suma_cuadrados(*args):
    total = 0
    for n in args:
        total += n**2
    return total

print(suma_cuadrados(1,2,3))

# EJERCICIO 2

def suma_absolutos(*args):
    total = 0
    for n in args:
        if n < 0:
            total += abs(n)
        else:
            total += n
    return total

print(suma_absolutos(-4, -1, 2, 6))

# EJERCICIO 3

def numeros_persona(nombre : str, *args):
    suma_numeros = 0
    for n in args:
        suma_numeros += n
    return(f"{nombre}, la suma de tus numeros es {suma_numeros}")

print(numeros_persona("Alan", 1,2,3,4,5))