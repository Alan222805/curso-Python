class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre
        

alan = Persona("Alan")
print(alan.get_nombre())

alan.set_nombre("Javier")

print(alan.get_nombre())
