nombres = ["Ana", "Hugo", "Valeria"]
edades = [65,29,42]
ciudades = ['Lima', 'Madrid', 'Mexico']

combinados = list(zip(nombres, edades, ciudades))

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años de edad y vive en {ciudad}")