class Pajaro:
    alas = True #Atributo de clase ==> Todos los objetos comparte el mismo atributo y valor
    def __init__(self,nombre, color, especie): #CONTRUCTOR
        self.nombre = nombre
        self.color = color #Atributo de instancia
        self.especie = especie

    def piar(self):
        print(f"PIOOOO mi color es {self.color}")
    
    def volar(self, metros):
        print(f"{self.nombre} ha volado {metros} metros")
        
piolin = Pajaro('Piolin', 'amarillo', 'canario')
piolin.piar()
piolin.volar(50)