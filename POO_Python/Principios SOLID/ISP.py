from abc import ABC, abstractmethod

class Trabajador(ABC):
    
    @abstractmethod
    def trabajar(self):
        pass
    
    
class Durmiente(Trabajador):
    @abstractmethod
    def dormir(self):
        pass
    
class Comedor(Trabajador):
    @abstractmethod
    def comer(self):
        pass
    
class Humano(Durmiente, Comedor):
    def comer(self):
        return "El humano esta comiendo"
    
    def trabajar(self):
        return "El humano esta trabajando"
    
    def dormir(self):
        return "El humano esta durmiendo"
    
class Robot(Trabajador):
    def trabajar(self):
        return "El Robot esta trabajando"
    
robot = Robot()
humano = Humano()

print(robot.trabajar())
print(humano.comer())