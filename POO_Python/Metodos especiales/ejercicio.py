class Personaje:
    def __init__(self, nombre, daño_poder):
        self.nombre = nombre
        self.daño_poder = daño_poder
        
    def __add__(self, otro):
        nuevo_nombre = self.nombre + otro.nombre
        nuevo_daño = round(((self.daño_poder + otro.daño_poder)/2)**1.5)
        
        return Personaje(nuevo_nombre, nuevo_daño)
    
    def __repr__(self):
        return f"Personaje(nombre= '{self.nombre}', daño= '{self.daño_poder}')"
    
goku = Personaje("Goku", 100)
vegeta = Personaje("Vegeta", 99)
jiren = Personaje("Jiren", 130)

gogeta = goku + vegeta
jireta = gogeta + jiren

print(jireta)