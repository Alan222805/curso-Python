
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
        self.piar()
        
    def pintar_negro(self):
        self.color = 'negro'
        
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        cls.alas = False
        
    @staticmethod
    def mirar():
        print("El pajaro mira")
        
        
piolin = Pajaro('Piolin', 'amarillo', 'canario')

piolin.poner_huevos(3)
Pajaro.mirar()