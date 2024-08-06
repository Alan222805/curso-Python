class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print("JAJAJA")
        
    def hablar(self):
        print("Que tal!")

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

print(Nieto.__mro__)