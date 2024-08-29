class Animal:
    
    def comer(self):
        return "Comiendo...."
    
class Mamifero(Animal):
    
    def amamantar(self):
        return "Amamantando..."
    
class Ave():
    
    def volar(self):
        return "Volando..."
    
class Murcielago(Mamifero, Ave):
    pass

murcielaguin = Murcielago()

print(Murcielago.mro())