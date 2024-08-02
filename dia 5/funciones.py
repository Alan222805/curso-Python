def greeting(name:str):
    '''
        This function serves to greet someone
    '''
    print("Hello " + name)

greeting("Alan")


def multiplicar (num1, num2):
    return num1*num2

print(multiplicar(2, 4))


# EJERCICIO

palabra_invertir = "Tecnologia"
def invertir_palabra(palabra):
    return palabra[::-1].upper()
print(invertir_palabra(palabra_invertir))