def letras_unicas(palabra:str):
    unicas = []
    for l in palabra:
        if l not in unicas:
            unicas.append(l)
    unicas.sort()
    return unicas

print(letras_unicas("entretenido"))