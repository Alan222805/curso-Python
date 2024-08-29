class Celular:
    #ATRIBUTOS de instancia
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo 
        self.camara = camara
    
    # METODOS de instancia    
    def llamar(self):
        print(f"Estas haciendo un llamado desde un: {self.modelo}")
        
    def cortar(self):
        print("Cortaste la llamada")

celular1 = Celular("Samsung", "S23", "48MP")
celular2 = Celular("Apple", "IPhone 15 Pro", "96MP")

print(celular1.marca)
print(celular2.marca)

celular2.llamar()