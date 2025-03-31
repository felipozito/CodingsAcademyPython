
"""
Dado un conjunto de caracteres, crea una función que devuelva el número central en el producto de cada dígito en la cadena.
Ejemplo: 's7d8jd9' -> 7, 8, 9 -> 789=504, por lo tanto, debería devolver 0 como un entero. ok
No todas las cadenas contendrán dígitos y no todas las entradas serán cadenas. En esos casos, devuelve -1. ok
Si el producto tiene un número par de dígitos, devuelve los dos dígitos centrales.
Ejemplo: 1563 -> 56
NOTA: Elimina los ceros iniciales si el producto es par y el primer dígito de los dos es un cero. Ejemplo 2016 -> 1
"""
def find_middle(st):
    if (type(st)!=str):
        return -1
    digits=[int(item) for item in st if item.isdigit()]
    product=1
    for digit in digits:
        product*=digit
    return product

x=[1,2,3,4,5,6,7,8,9]
for x in range(0,2):
    print(x)