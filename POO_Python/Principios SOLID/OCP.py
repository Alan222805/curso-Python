""" class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
        
    def notificar(self):
        raise NotImplementedError
    
    
class NotificadorEmail(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje a {self.usuario.email}")
        
class NotificadorWhatsapp(Notificador):
    def Notificar(self):
        print(f"Enviando whatsapp a {self.usuario.numero_personal}")
        

class Usuario:
    def __init__(self, nombre, email, numero_personal):
        self.nombre = nombre
        self.email = email
        self.numero_personal = numero_personal



alan = Usuario("Alan", "alan@gmail.com", "7716458594")
notificador_email = NotificadorEmail(alan, "Hola, ¿Cómo estas?")
notificador_whatsapp = NotificadorWhatsapp(alan, "Hola, ¿Cómo estas?")

notificador_email.Notificar() """

from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass
    
class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
        
    def calcular_area(self):
        return 3.14 * self.radio ** 2
    
class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
        
    def calcular_area(self):
        return self.lado ** 2
    
class CalculadoraDeArea:
    def calcular(self, forma : Forma):
        return forma.calcular_area()
    
circulo = Circulo(5)
cuadrado = Cuadrado(4)
calculadora = CalculadoraDeArea()

print(calculadora.calcular(circulo))
print(calculadora.calcular(cuadrado))