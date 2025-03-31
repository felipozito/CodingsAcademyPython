
import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="pistacho",
        database="prueba"
    )
except:
    print("Error")

cursor=connection.cursor()

try:
    cursor.execute("CREATE DATABASE prueba")# Crear la base de datos
    cursor.execute("USE prueba")# Usar la base de datos 
    cursor.execute("CREATE TABLE usuarios (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), edad INT)")# Crear la tabla usuarios
    print("Operacion Correcta")
except:
    print("Ya existe")    

try:
    cursor.execute("USE prueba")
    cursor.execute("SELECT * FROM prueba")
    print("Operacion Correcta")
except:
    print("REspuesta ")


try:
    cursor.execute("USE prueba")
    cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)", ("Juan", 25))# Insertar un usuario
    cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)", ("María", 30))# Insertar un usuario
    print("Operacion Correcta")
except:
    print("Ya existe")
