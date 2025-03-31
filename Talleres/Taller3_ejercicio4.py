"""Escribir un programa que almacene las asignaturas datos en un diccionario, que se pueda, añadir un elemento, actualizar el elemento y eliminar el elmento.
Debe iterar el elmento y cuando llegue al item 2 actualice un nuevo valor.
Añada un nuevo elmento color: "rojo"
Elimine el color rojo.
"""

# Crear un diccionario con asignaturas
asignaturas = {
    "Matemáticas": 85,
    "Física": 78,
    "Programación": 92,
    "Historia": 65
}

print("Diccionario original:")
print(asignaturas)

# Añadir un elemento al diccionario
asignaturas["Inglés"] = 88
print("\nDespués de añadir 'Inglés':")
print(asignaturas)

# Iterar el diccionario y actualizar el elemento en la posición 2
for i, (asignatura, valor) in enumerate(asignaturas.items()):
    if i == 2:  # Cuando llegue al tercer elemento (índice 2)
        asignaturas[asignatura] = 95
        print(f"\nActualizando {asignatura} a 95")

print("\nDespués de actualizar el elemento en posición 2:")
print(asignaturas)

# Añadir el elemento color: "rojo"
asignaturas["color"] = "rojo"
print("\nDespués de añadir 'color: rojo':")
print(asignaturas)

# Eliminar el elemento color
if "color" in asignaturas:
    del asignaturas["color"]
    print("\nDespués de eliminar 'color':")
    print(asignaturas)

# Demostración de otras operaciones con diccionarios
print("\nOperaciones adicionales:")

# Actualizar un elemento específico
asignaturas["Matemáticas"] = 90
print("Después de actualizar 'Matemáticas':", asignaturas)

# Eliminar un elemento específico
if "Historia" in asignaturas:
    del asignaturas["Historia"]
    print("Después de eliminar 'Historia':", asignaturas)

# Verificar si existe una clave
print("¿Existe 'Química'?", "Química" in asignaturas)

# Obtener todas las claves
print("Claves:", list(asignaturas.keys()))

# Obtener todos los valores
print("Valores:", list(asignaturas.values()))

