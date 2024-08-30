def suma():
    
    while True:
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        try:
            resultado = int(a) + int(b)
        #Si lanzo una excepcion, perdirle que reingrese los datos
        except Exception as e:
            print("Eso no es un numero, hazlo de nuevo!")
            print(f"Error: {e}")
        #Si todo salio bien, terminamos el bucle
        else:
            break
        #El finally se ejecuta siempre
        finally:
            print("Manejo de excepcion finalizado")
    return resultado

print(suma())