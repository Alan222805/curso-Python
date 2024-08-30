""" mi_set = set([1,2,3,4])
print(type(mi_set))


otro_set = {1,2,3,4}
print(type(otro_set))


s = {1,2,3,4,5,6,(5,2,4),33}
print(3 in s, '\n')


s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2) # {1,2,3,4,5}
print(s3)

s3.add(7)# {1,2,3,4,5,7}

s3.remove(3)# {1,2,4,5,7}
s3.discard(4)# {1,2,5,7}
s3.pop()
s3.pop()
print(s3)  """


# Iterando un conjunto

numeros = {1,2,3,4,5,6}

for n in enumerate(numeros):
    print(n)
    

numeros.add(7)
print(numeros)

lista = [1,2,3,4,5]

lista_a_set = set(lista)
print(lista_a_set)