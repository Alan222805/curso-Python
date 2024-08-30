#Creando mi propia excepcion personalizada
class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"Impresionante, cometiste el siguiente error: {err}")
    
# raise ZeroDivisionError("Que boludo, dividiste por cero")    

# Lanzando mi propia excepcion
raise MiExcepcion("JAJAJA, Persona mensa")

#Manejando la excepcion
try:
    raise MiExcepcion("JAJAJA, Persona mensa")
except:
    print("Como vas a cometer ese error?")
    

    