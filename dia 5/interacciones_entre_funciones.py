""" from random import shuffle

# Lista inicial
palitos = ['-', '--', '---', '----']
# Mezclar a los palitos
def mezclar(lista_palitos):
    shuffle(lista_palitos)
    return lista_palitos
# Pedir al usuario el intento
def probar_suerte():
    intento = ''
    while intento not in ['1', '2', '3', '4']:
        intento = input("Elige un numero del 1 al 4: ")
    return int(intento)
# Comprobar el intento
def chequear_intento(lista_palitos, intento_usuario):
    if lista_palitos[intento_usuario-1] == '-':
        print("A lavar los platos")
    else:
        print("Esta vez te has salvaldo")
        
    print(f"Te ha tocado {lista_palitos[intento_usuario-1]}")
    
palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion) """

# EJERCICIO 1

from random import *
def lanzar_dados():
    dado1 = randint(1,7)
    dado2 = randint(1,7)
    return dado1, dado2

dado1, dado2 = lanzar_dados()
def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return (f"La suma de tus dados es {suma_dados}. Lamentable")
    elif suma_dados > 6 and suma_dados < 10:
        return (f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
        
    elif suma_dados >= 10:
        return (f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")
        
print(evaluar_jugada(dado1, dado2))


# EJERCICIO 2

lista_numeros = [1,2,15,7,2]

def reducir_lista (lista_numeros : list):
    lista_sin_duplicados = []
    for numero in lista_numeros:
        if(numero not in lista_sin_duplicados):
            lista_sin_duplicados.append(numero)
    valor_mayor = max(lista_sin_duplicados)
    lista_sin_duplicados.remove(valor_mayor)
    return lista_sin_duplicados

def promedio(lista_numeros : list):
    promedio_final = sum(lista_numeros) / len(lista_numeros)
    return promedio_final

lista_reducida = reducir_lista(lista_numeros)
print(round(promedio(lista_reducida), 2))

# EJERCICIO 3

def lanzar_moneda():
    opciones_modena = ['Cara', 'Cruz']
    return choice(opciones_modena)

lista_numeros2 = list(range(1, 50, randint(5,10)))
shuffle(lista_numeros2)
def probar_suerte(opcion_moneda:str, lista_numeros:list):
    if(opcion_moneda == 'Cara'):
        print("La lista se autodestruirá")
        lista_numeros.clear()
        
    elif opcion_moneda == 'Cruz':
        print("La lista fue salvada")
    
    return lista_numeros
    
moneda = lanzar_moneda()
print(moneda)
print(probar_suerte(moneda, lista_numeros2))
    