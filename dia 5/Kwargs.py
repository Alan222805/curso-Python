def suma(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    
    return total

print(suma(x=3, y=5, z=2))


def prueba(n1, n2, *args, **kwargs):
    print(f"El primer valor es: {n1}")
    print(f"El segundo valor es: {n2}")
    
    for arg in args:
        print(f"arg = {arg}")
    
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        

valores = [100,200,300,400]
ejes = {'x':'uno', 'y':'dos', 'z':'tres'}

prueba(15,50, *valores , **ejes)


# EJERCICIO 1

def cantidad_atributos(**kwargs):
    return len(kwargs.items())
    

# EJERCICIO 2

def lista_atributos(**kwargs):
    lista_valores = [v for v in kwargs.values()]
    return lista_valores

print(lista_atributos(x='uno', y='dos', z='tres'))

# EJERCICIO 3

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}")
    for c,v in kwargs.items():
        print(f"{c}: {v}")
        
describir_persona("Alambrito", color_ojos='azules', color_pelo='negro')