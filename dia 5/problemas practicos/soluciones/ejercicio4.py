def contar_primos(numero:int):
    primos = 0
    for i in range(2, numero+1):
        for j in range(2, numero+1):
            print(i, j)
                          

contar_primos(12)
