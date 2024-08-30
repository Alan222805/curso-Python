
#Abriendo el archivo con with oper
with open("cursoPython_Dalto\\trabajar con archivos\\x.txt", encoding="UTF-8") as archivo:
    
    #Leemos el archivo
    contenido = archivo.read()
    
    #Mostramos el contenido del archivo
    print(contenido)
    
#No es necesario cerrar el archivo al usar with open