"""
Las tuplas son una estructura de datos que almacena una secuencia de elementos de un mismo tipo.
Las tuplas pueden almacenar elementos de diferentes tipos, como enteros, flotantes, cadenas de caracteres, etc.
INMUTABLE

se puedes convertir con list   
"""
# Tupla de enteros  
tupla1=(1,2,3,4,5)
print(tupla1)
print(list(tupla1))

for item in tupla1:
    print(item)

"""
Los conjuntos son una estructura de datos que almacena una secuencia de elementos de un mismo tipo. No pueden haber duplicados
se puede agregar o eliminar elementos
"""

conjunto={"uno","dos","tres","cuatro","cinco","uno"}
conjunto2={1,2,3,4,}
print(conjunto2)
conjunto2.add(5)
conjunto2.remove(3)
print(conjunto2)
conjunto2.update([1,"uno"])
print(conjunto2)

for item in conjunto2:
    print(item)