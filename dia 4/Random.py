from random import *

aleatorio = round(uniform(1,5),1)
print(aleatorio)

# randint(min, max) => Elige un numero entero aleatorio entre un numero minimo y un maximo especificados.


# uniform(min, max) => Elige un numero decimal aleatorio entre un numero minimo y un maximo especificados.

# choice(secuencia) => elige un elemento de una secuencia aleatoriamente.

colores = ('azul', 'verde')
color_random = choice(colores)
print(color_random)


# sufle(secuencia) => cambia el orden de los elementos de la secuencia de forma aleatoria

numeros = list(range(5, 50, 5))
shuffle(numeros)
print(numeros)


# random() => retorna un numero aleatorio entre 0 y 1

