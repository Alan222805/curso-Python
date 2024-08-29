class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    @property
    def get_nombre(self):
        return self.__nombre
    
    @get_nombre.setter
    def get_nombre(self, new_nombre):
        self.__nombre = new_nombre
        
    @get_nombre.deleter
    def get_nombre(self):
        del self.__nombre
    

alan = Persona("Alan", 21)
print(alan.get_nombre)

alan.get_nombre = "Javier"
print(alan.get_nombre)

# del alan.get_nombre

print(alan.get_nombre)

