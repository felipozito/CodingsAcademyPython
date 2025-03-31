

"""Cree un archivo de python con el nombre taller1_ejercicio2.py 
Se requiere que el estudiante cree una variable de texto frase = "Las mejores cosas de la vida son gratis“ y que muestre por pantalla la longitud de la cadena. Utilice la función len(). 
Con la misma variable frase, el estudiante deberá mostrar por pantalla las primeras 3 letras de la cadena. Utilizar slicing. 
Con la misma variable frase, el estudiante deberá comprobar si la palabra “vida” está presente en la variable "frase" utilice la palabra clave in. 
Deberá utilizar el bucle for para recorrer los caracteres de la variable frase. 
Utilice el condicional if y compruebe que la palabra “mejores” se encuentre en la variable frase, si es verdadero entonces debe imprimir un mensaje. 
"""
frase = "Las mejores cosas de la vida son gratis"
#Mostrar por pantalla la longitud de la cadena. Utilice la función len().
print(len(frase))
#Con la misma variable frase, el estudiante deberá mostrar por pantalla las primeras 3 letras de la cadena. Utilizar slicing.
print(frase[0:3])
#Con la misma variable frase, el estudiante deberá comprobar si la palabra “vida” está presente en la variable "frase" utilice la palabra clave in.
print("vida" in frase)
#Deberá utilizar el bucle for para recorrer los caracteres de la variable frase.
for i in frase:
    print(i)
#Utilice el condicional if y compruebe que la palabra “mejores” se encuentre en la variable frase, si es verdadero entonces debe imprimir un mensaje.
if "mejores" in frase:
    print("La palabra mejores se encuentra en la variable frase")
