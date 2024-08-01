from random import randint

numero_pensado = randint(1, 101)
max_intentos = 8
numero_intentos = 0

nombre = input("¿Cual es tu nombre?: ")
respuesta = 0

print(f"Bueno, {nombre}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar")

while max_intentos > 0 and respuesta != numero_pensado:
    respuesta = int(input("¿Cual crees que es el numero?: "))
    max_intentos -= 1
    numero_intentos += 1
    if type(respuesta) is not int:
        print("Ese no es un numero!!")
    elif respuesta < 1 or respuesta > 100:
        print("Ese numero no esta permitido")
    elif respuesta < numero_pensado:
        print("Tu respuesta es incorrecta y ademas es un número menor al número secreto")
    elif respuesta > numero_pensado:
        print("Tu respuesta es incorrecta y ademas es un número mayor al número secreto")
    elif respuesta == numero_pensado:
        print(f"!Has ganado en un total de {numero_intentos} intentos¡")
    print(f"Intentos restantes: {max_intentos}")
    