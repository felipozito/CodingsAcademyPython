"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química,Historia y Lengua) en una lista y la muestre por pantalla. 
Inserte después de la materia química y antes de historia una nueva materia que se llamará “programación” .
Eliminar la materia mátematicas. 
"""

Sschedule=["Matematicas","Fisica","Quimica","Historia","Lengua"]
print(Sschedule)
Sschedule.insert(3,"Programacion")
print(Sschedule)
Sschedule.remove("Matematicas")
print(Sschedule)    