""" class Ave:
    def volar(self):
        return "Estoy volando"
    
class Pinguino(Ave):
    def volar(self):
        return  "No puedo volar"

def hacer_volar(ave:Ave):
    return ave.volar()

print(hacer_volar(Pinguino())) """

class Ave:
    def __init__(self, nombre):
        self.nombre = nombre

class AveVoladora(Ave):
    def volar(self):
        return f"Soy un {self.nombre} y puedo volar"
    
class AveNoVoladora(Ave):    
    def nadar(self):
        return f"Soy un {self.nombre} y puedo volar"
    
    
aguila = AveVoladora("Aguila")
pinguino = AveNoVoladora("Pinguino")

print(aguila.volar())
print(pinguino.nadar())

        