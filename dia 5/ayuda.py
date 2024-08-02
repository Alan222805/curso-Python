""" dic = {'clave1': 100, 'clave2': 500}
a = dic.popitem()
print(a)
print(dic) """

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# PRIMER EJERCICIO
texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
texto_nuevo = texto.lstrip(',:_#,,,,,,:::____##')
print(texto_nuevo)

# SEGUNDO EJERCICIO
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"] 
frutas.insert(4, "Naranja")
print(frutas)

# TERCER EJERCICIO
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)