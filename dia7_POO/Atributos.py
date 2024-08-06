class Pajaro:
    alas = True #Atributo de clase ==> Todos los objetos comparte el mismo atributo y valor
    def __init__(self, color, especie): #CONTRUCTOR
        self.color = color #Atributo de instancia
        self.especie = especie

mi_pajaro = Pajaro('blanco', 'Tucan')

print(f"Mi parajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}")

print(mi_pajaro.alas)