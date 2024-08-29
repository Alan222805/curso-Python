class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print(f"{self.nombre} esta hablando un poco")
        

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"
        

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
    def presentarse(self):
        return f"{super().mostrar_habilidad()} y trabajo en {self.empresa}"   
        


class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

roberto = EmpleadoArtista("Roberto", 43, "Mexicano","Cantar", 100000, "Academia")

print(roberto.presentarse())


herencia = issubclass(Artista, Persona)
instancia = isinstance(roberto, Artista)
print(instancia)