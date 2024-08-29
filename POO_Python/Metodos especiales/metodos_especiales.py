class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    """ def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}" """
    
    def __repr__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad})"
    
    def __add__(self, otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre, nuevo_valor)
    
    def __sub__(self, otro):
        nuevo_valor = self.edad - otro.edad
        return Persona(self.nombre, nuevo_valor)
    
    def __eq__(self, otro):
        return self.edad == otro.edad
    

alan = Persona("Alan", 21)
paola = Persona("Paola", 21)

nuevo_alan = repr(alan)
print(eval(nuevo_alan))

""" class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    #Sobrecarga del operador '+'
    
    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
v1 = Vector(2,3)
v2 = Vector(5,7)

v3 = v1+v2 #Esto llama a v1.__add__(v2)
print(v3) """