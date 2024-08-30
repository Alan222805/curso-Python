#Metiendo un conjunto dentro de otro conjunto

conjunto1 = frozenset(["dato 1", "dato 2"])
conjunto2 = {conjunto1, "dato 3"}
print(conjunto2)

#Teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {2,4}

# Verificando si conjunto2 es un subconjunto de conjunto1

# resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1
print(resultado)

# Verificando si conjunto1 es un superconjunto de conjunto2

# resultado = conjunto2 < conjunto1
resultado = conjunto1.issuperset(conjunto2)
print(resultado)


# Verificar si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)