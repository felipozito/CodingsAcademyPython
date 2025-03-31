"""Crear un programa que me permita almacenar materias y 3 calificaciones, crear una funcion que permita calcular el promedio de estas calificaciones almacenadas, otra funcion que permita  mostrar todas las materias y el promedio, ademas si el promedio es mayor a 7 un mensaje que diga materia aprobada y si es inferior reprobado.
"""

materias=[]
calificaciones=[]
def promedio(calificaciones):
    suma=0
    for i in range(len(calificaciones)):
        suma=suma+calificaciones[i]
    return suma/len(calificaciones)
def mostrar(materias,calificaciones):
    for i in range(len(materias)):
        print("La materia ",materias[i]," tiene un promedio de ",promedio(calificaciones[i]))
        if promedio(calificaciones[i])>=7:
            print("La materia ",materias[i]," esta aprobada")
        else:
            print("La materia ",materias[i]," esta reprobada")
def main():
    materias.append(input("Ingrese la materia: "))
    calificaciones.append([])
    for i in range(3):
        calificaciones[len(calificaciones)-1].append(int(input("Ingrese la calificacion: ")))
    mostrar(materias,calificaciones)
main() 