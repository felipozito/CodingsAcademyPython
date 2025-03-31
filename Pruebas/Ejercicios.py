"""                             EJERCICIO 1
Escribir un programa en Python que imprima una X construida a base de la letra X y
utilizar el carácter de subrayado como espacio. El tamaño de la x se basa en una variable n
 que indicará el tamaño de la letra para imprimir (en una matriz de n x n). Por ejemplo,
 para n = 5 se obtiene:

X___X
_X_X_
__X__
_X_X_
X___X

y para n=6 se obtiene:

X____X
_X__X_
__XX__
__XX__
_X__X_
X____X

Si n es igual a cero imprimir "ERROR"
"""
def ejercicio1(n):
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                print("X", end="")
            else:
                print("_", end="")
        print()
ejercicio1(6)

"""
                            EJERCICIO 2
Tienes un arreglo (llamado myArray) con 5 elementos (enteros en el rango de 1 a 100).
 Escribe un programa en Python que imprima el número más alto del arreglo (Si se repite, 
 solo imprimir una vez). El programa solo debe imprimir el número, sin ningún texto.
"""
def ejercicio2(myArray):
    max = 0
    for i in myArray:
        if i > max:
            max = i
    print(max)

#ejercicio2([1,2,3,4,5,6,7,8,9,10])
"""
                            EJERCICIO 3
Escribir un programa en Python que puede determinar si una matriz es simétrica. Una matriz es simétrica 
si se ve igual si está invertida. Por ejemplo ('a', 'b', 'c', 'd', 'd', 'c', 'b', 'a') 
es simétrica y ('a', 'b', 'c', 'd', 'd', 'b', 'c', 'a') no lo es. Suponga que n será siempre un número par
entre 2 y 10 (No hay necesidad de validar esto). Si es simétrico su programa debe imprimir 'Symmetric', 
de lo contrario imprimir 'Asymmetric'

La salida de los datos para el arreglo en el ejemplo ('a', 'b', 'c', 'd', 'd', 'c', 'b', 'a') sería:
Symmetric
"""

def ejercicios3(array):
    n = len(array)
    array2=[]
    for value in range(n):
       array2.append(array[n-value-1])
    print("Symmetric" if array==array2 else "Asymmetric")
    
def ejercicio3(array):
    n = len(array)
    for i in range(n//2):
        if array[i] != array[n-1-i]:
            return "Asymmetric"
    return "Symmetric"

ejercicios3(['a', 'b', 'c', 'd', 'd', 'c', 'b', 'a'])

"""
                            EJERCICIO 4
Tienes un arreglo (llamado myArray) con 10 elementos (enteros en el rango de 1 a 9). 
Escribe un programa en Python que imprima el número que tiene más ocurrencias seguidas en el arreglo y 
también imprimir la cantidad de veces que aparece en la secuencia.

El código que llena el arreglo ya está escrito, pero puedes editarlo para probar con otros valores. Con el botón de refrescar 
puedes recuperar el valor original que será utilizado para evaluar la pregunta 
como correcta o incorrecta durante la ejecución.
Su programa debe analizar el arreglo de izquierda a derecha para que en caso de que dos números cumplan 
la condición, el que aparece por primera vez de izquierda a derecha será el que se imprima.
La salida de los datos para el arreglo en el ejemplo (1,2,2,5,4,6,7,8,8,8) sería la siguiente:
Longest: 3
Number: 8
"""
def ejercicio4(myArray):
    max = 0
    max2 = 0
    for i in myArray:
        if myArray.count(i) > max:
            max = myArray.count(i)
            max2 = i
    print("Longest:",max)
    print("Number:",max2)
ejercicio4([1,2,2,5,4,6,7,8,8,8])


"""
EJERCICIO 5    
Escribir un programa en Python que recorra un arreglo y genere un histograma en 
base a los números de este. El arreglo se llama myArray y contiene 10 elementos que 
corresponden a números enteros del 1 al 5. Un histograma representa que tanto un elemento 
aparece en un conjunto de datos (Debe mostrar la frecuencia para todos los números del 1 al 5,
 incluso si no están presentes en el arreglo). 

Por ejemplo, para el arreglo: myArray:=(1,2,1,3,3,1,2,1,5,1) el histograma se vería así:
1: *****
2: **
3: **
4:
5: """

def ejercicio5(myArray):
    for i in range(1,6):
        print(i,":","*"*myArray.count(i))
ejercicio5([1,2,1,3,3,1,2,1,5,1])