from random import choice

idiomas = ["Español", 'Ingles', 'Portugues', 'Chino']

def idioma_aleatorio(idiomas:list):
    idioma_aleatorio:str = choice(idiomas)
    guiones:str = idioma_aleatorio.replace(idioma_aleatorio, '_'*len(idioma_aleatorio))
    
    return idioma_aleatorio.lower(), guiones


def pedir_usuario():
    letra = input('Escribe una letra: ')
    return letra

""" def validar(idioma_aleatorio: str, letra:chr):
    vidas = 6
    if """

print(idioma_aleatorio(idiomas))
# print(idioma_aleatorio(idiomas)[0].)

print('pythonp'.index('p'))

aux = 0
indices = []
for p in "ppython":
    if p == 'p':
        indices.append(aux)
        aux += 1
    else:
        aux += 1

print(indices)