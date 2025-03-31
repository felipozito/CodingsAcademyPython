"""Escribir un programa que permita crear diferentes tipos de archivos como TXT, CSV, XSLX y JSON. 
"""
def crearArchivo():
    archivo=input("Ingrese el nombre del archivo: ")
    tipo=input("Ingrese el tipo de archivo: ")
    if tipo=="txt":
        archivo=archivo+".txt"
    elif tipo=="csv":
        archivo=archivo+".csv"
    elif tipo=="json":
        archivo=archivo+".json"
    else:
        print("Tipo de archivo no valido")
        return
    archivo=open(archivo,"w")
    archivo.close()
crearArchivo() 