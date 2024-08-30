import re

texto = '''Hola maestro, esta es la cadena 1. ¿como estas mi capitan?
Esta es la segunda linea 245 de texto.
Y esta es la final (linea 3) definitiva mi capitan. abababab'''

#Haciendo una busqueda simple
# resultado = re.findall("esta", texto, flags=re.IGNORECASE)

# \d  --> Busca digitos numericos del 0-9
resultado = re.findall(r"\d",texto)

# \D busca todo menos digitos numericos
resultado = re.findall(r"\D", texto)

# \w busca caracteres alfanumericos [a-z, A-Z, 0-9, _]
resultado = re.findall(r"\w", texto)
# print(resultado)
# \W busca todo menos caracteres alfanumericos [a-z, A-Z, 0-9, _]
resultado = re.findall(r"\W", texto)

# \s busca espacios en blanco -> espacion, tabs, saltos de linea
resultado = re.findall(r"\s", texto)

# \S busca todo menos espacios en blanco -> espacion, tabs, saltos de linea
resultado = re.findall(r"\S", texto)

# '.' busca todo menos saltos de linea
resultado = re.findall(r".", texto)

# \n busca saltos de linea
resultado = re.findall(r"\n", texto)


# \  --> cancelar caracteres especiales, cancelando la funcion del punto y buscando puntos
resultado = re.findall(r"\?", texto)

# armando una cadena que busque un numero, seguido de un punto y un espacio
resultado = re.findall(r"\d\.\s", texto)

# ^ --> busca el comienzo de una linea
# flags=re.M --> activa la multilinea
resultado = re.findall(r"^Esta", texto, flags=re.M)

# $ --> busca el final de una linea
resultado = re.findall(r"capitan.$", texto, flags=re.M)

# {n} --> busca n cantidad de veces el valor de la izquierda {3 numeros juntos esta vez}
resultado = re.findall(r"\d{3}", texto)

# {n,m} --> al menos n, como maximo m
resultado = re.findall(r"\d{1,4}", texto)
resultado = re.findall(r"(ab){3}", texto)

# | --> busca una cosa o la otra
resultado = re.findall(r"\d{2,4}|Hola", texto)

print(resultado)