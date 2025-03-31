"""Cree un archivo de python con el nombre taller2_ejercicio3.py 
1). Escribir un programa que pida al usuario una frase y muestre cada uno de sus elementos.
2). Desarrolle un software que sea un menú de opciones y que muestre el día Lunes si el usuario ingresa el número 1, que muestre Martes si ingresa 2, y asi hasta llegar al 7. 
Al software del día de la semana agreguele más funcionalidad, por ej.  pregunte tambien un nombre al usuario y una actividad fisica y en el día miercoles, muestre el día, el nombre y la actividad fisica. 
Si ingresa el día viernes muestre el nombre del día y muestre un mensaje que diga "Feliz Fin de Semana".
    """
name=input("Ingrese su nombre: ")
activity=input("Ingrese una actividad fisica: ")    
phrase=input("Ingrese una frase: ")
for i in phrase:
    print(i)
print("---------------------")
num=int (input("Ingrese un numero del 1-7: "))
if num==1:
    print("Lunes y ",name," realizara : ",activity)
elif num==2:
    print("Martes y ",name," realizara : ",activity)
elif num==3:
    print("Miercoles y ",name," realizara : ",activity)
elif num==4:
    print("Jueves y ",name," realizara : ",activity)
elif num==5:
    print("Viernes y ",name," realizara : ",activity)
elif num==6:
    print("Sabado y ",name," realizara : ",activity)
elif num==7:
    print("Domingo y ",name," realizara : ",activity)
else:
    print("Numero incorrecto")
