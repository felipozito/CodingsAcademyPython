"""
Para el uso de condicionales en Python, se utilizan las palabras clave if, elif y else.

if:
    Este es el bloque de código que se ejecutará si la condición es verdadera.
elif:
    Este es el bloque de código que se ejecutará si la condición es falsa y la condición anterior es verdadera.
else:
    Este es el bloque de código que se ejecutará si la condición es falsa y la condición anterior es falsa.

for:
    Este es el bloque de código que se ejecutará una vez por cada elemento en un conjunto.
    ejemplo: for i in range(1,10):
while:
    Este es el bloque de código que se ejecutará mientras la condición sea verdadera.
    ejemplo: while var>0:
        print(var)
        var=var-1

"""

var='holaa'
var2=55
"""
if var=='hola':
    print("hola")
elif var2==5 :
    print("5")
else:
    print("adios")
    
for i in range(1,var2+1): 
    print(i)
    i=i+1
while var2>0:
    print(var2)
    var2=var2-1"""
    
print((range(1,10)))

word="hola"
print("o" in word)
print("hola" in word)
print(not("pez" not in word))

word=True
print(word)
print(not word)
print(not not word)