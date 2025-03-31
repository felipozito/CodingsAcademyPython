"""
Las listas son una estructura de datos que almacena una secuencia de elementos de un mismo tipo.
Las listas pueden almacenar elementos de diferentes tipos, como enteros, flotantes, cadenas de caracteres, etc.
Por ejemplo, si queremos almacenar una lista de números enteros, podemos hacerlo de la siguiente manera:        
metodos de listas
append(elemento): Agrega un elemento al final de la lista.
extend(lista): Agrega todos los elementos de la lista pasada como argumento al final de la lista actual.
insert(indice,elemento): Inserta un elemento en la lista en el índice especificado.
pop(indice): Elimina el elemento en el índice especificado.
remove(elemento): Elimina el primer elemento que coincida con el elemento especificado.
sort(): Ordena la lista en orden ascendente.
reverse(): Invierte la lista.   
"""

list1=[1,2,"hola",4,5]
list1.append(6)
list1.extend([7,8,9])
list1.insert(2,3)
print(list1)
list1.remove('hola')
print(list1)
list1.reverse() 

for item in list1:
    print(item)
# end for

