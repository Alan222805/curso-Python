from random import choice

idiomas = ["Español", 'Ingles', 'Porstugues', 'Chino']

#Elige un idioma al azar y genera una lista de guiones
def idioma_aleatorio(idiomas:list):
    idioma_aleatorio:str = choice(idiomas)
    guiones:str = idioma_aleatorio.replace(idioma_aleatorio, '_'*len(idioma_aleatorio))
    
    return idioma_aleatorio.lower(), guiones

def pedir_usuario():
    letra = input('Escribe una letra: ')
    return letra
    
#Mostrar la letra elegina en lista de guiones 
def mostrar_letras(letra,indices, lista_guiones:list):
    lista_mostrar = ''
    for n in range(0, len(lista_guiones)):
        for i in indices:
            if i == n:
                lista_mostrar += letra
                break
        else:
            lista_mostrar+='_'
            
    return lista_mostrar
        
        

def obtener_indices(idioma_aleatorio:str, letra:str):
    indices = []
    aux = 0
    #Obtener los indices en que aparecen la letra del usuario
    for p in idioma_aleatorio:
        if letra == p:
            indices.append(aux)
            aux+=1
        else:
            aux+=1   
    return indices

def validar_respuesta(respuesta:str, idioma_aleatorio:str):
    if respuesta.lower() == idioma_aleatorio:
        print(f"Felicidades haz ganado, la respuesta efectivamente era {idioma_aleatorio}")
        return True
    else:
        print("Mala suerte, esa no es la palabra!")
        return False
            

""" def validar_letra_usuario(letra, idioma:str, lista_guiones, vidas, indices):
    if letra in idioma:
        lista_mostrar = mostrar_letras(letra, indices, lista_guiones)
        return lista_mostrar, vidas
    else:
        vidas -= 1
        return f"Lo sentimos, la letra '{letra}' no es parte del idioma.\nte quedan {vidas} vidas", vidas """
def validar_letra_usuario(letra, idioma:str, lista_mostrar, vidas):
    if letra in idioma:
        return lista_mostrar, vidas
    else:
        vidas -= 1
        return f"Lo sentimos, la letra '{letra}' no es parte del idioma.\nte quedan {vidas} vidas", vidas
    
vidas = 6
aleatorio = idioma_aleatorio(idiomas)
idioma_escogido = aleatorio[0]
lista_guiones = aleatorio[1]
respuesta_usuario = ''
respuesta_correcta = False

print("JUEGO DEL AHORCADO")
while vidas > 0:
    letra_usuario = input('Escribe una letra: ').lower()
    indices = obtener_indices(idioma_escogido, letra_usuario)
    # validacion = validar_letra_usuario(letra_usuario, idioma_escogido, lista_guiones, vidas, indices)
    lista_mostrar = mostrar_letras(letra_usuario, indices, lista_guiones)
    validacion = validar_letra_usuario(letra_usuario, idioma_escogido, mostrar_letras(letra_usuario, indices, lista_mostrar),vidas)
    print(validacion[0])
    vidas = int(validacion[1])
    

