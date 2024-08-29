""" class Diccionario:
    def verificar_palabra(self, palabra):
        #logica para verificar palabras
        pass
    
class CorrectorOrtografico:
    def __init__(self):
        self.diccionario = Diccionario()
        
    def corregir_texto(self, texto):
        #usamos el diccionario para corregir el texto
        pass """
        
from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        pass
class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #Logica para verificar palabras si esta en el diccionario
        pass
class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador
        
    def corregir_texto(self, texto):
        #usamos el verificador para corregir texto
        pass

