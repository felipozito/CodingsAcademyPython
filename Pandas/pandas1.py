import pandas as pd
import numpy as np

# 1. Creando DataFrames
print("1. CREANDO DATAFRAMES")
# Desde un diccionario
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 34, 29, 42],
    'City': ['New York', 'Paris', 'Berlin', 'London'],
    'Salary': [65000, 70000, 62000, 85000]
}
df = pd.DataFrame(data)
print(df)
print("\n")

# Desde un archivo CSV (descomentar para usar)
df_csv = pd.read_csv('Libro1.csv')
print(df_csv)

# Desde un archivo Excel (descomentar para usar)
df_excel = pd.read_excel('Libro1.xlsx')
print(df_excel)

# 2. Información básica del DataFrame
print("2. INFORMACIÓN BÁSICA DEL DATAFRAME")
print("Forma:", df_excel.shape)  # (filas, columnas)
print("Columnas:", df_excel.columns)
print("Tipos de datos:\n", df_excel.dtypes)
print("Estadísticas resumidas:\n", df_excel.describe())
print("\n")

# 3. Accediendo a los datos
print("3. ACCEDIENDO A LOS DATOS")
# Accediendo a columnas
print("Primera columna:\n", df_excel['Nombre'])
print("Múltiples columnas:\n", df_excel[['Apellido', 'Sueldo']])

# Accediendo a filas
print("Primeras 2 filas:\n", df_excel.head(2))
print("Últimas 2 filas:\n", df_excel.tail(2))
print("Fila por índice:\n", df_excel.iloc[0])  # Primera fila
print("Filas 1-2, columnas 0-2:\n", df_excel.iloc[0:3, 0:2])
print("Fila por condición:\n", df_excel[df_excel['Sueldo'] < 1500])
# print("\n")

# # 4. Añadiendo y modificando datos
# print("4. AÑADIENDO Y MODIFICANDO DATOS")
# # Añadiendo una nueva columna
# df['Experience'] = [3, 8, 4, 12]
# print("Columna 'Experience' añadida:\n", df)

# # Modificando valores
# df.loc[0, 'Salary'] = 67000  # Cambiar el salario de John
# print("Salario de John modificado:\n", df)

# # Añadiendo una nueva fila
# new_row = {'Name': 'Maria', 'Age': 31, 'City': 'Madrid', 'Salary': 69000, 'Experience': 6}
# df = df._append(new_row, ignore_index=True)
# print("Nueva fila añadida:\n", df)
# print("\n")

# # 5. Eliminando datos
# print("5. ELIMINANDO DATOS")
# # Eliminando una columna
# df_no_exp = df.drop('Experience', axis=1)
# print("Columna 'Experience' eliminada:\n", df_no_exp)

# # Eliminando filas
# df_filtered = df.drop(index=1)  # Eliminar la segunda fila (Anna)
# print("Fila con índice 1 eliminada:\n", df_filtered)

# # Eliminar filas por condición
# df_young = df[df['Age'] <= 30].copy()  # Mantener solo personas de 30 años o menos
# print("Solo personas de 30 años o menos:\n", df_young)
# print("\n")

# # 6. Guardando DataFrames
# print("6. GUARDANDO DATAFRAMES")
# # Guardar en CSV (descomentar para usar)
# # df.to_csv('output.csv', index=False)
# # print("Guardado en CSV")

# # Guardar en Excel (descomentar para usar)
# # df.to_excel('output.xlsx', index=False)
# # print("Guardado en Excel")

# # 7. Análisis de datos
# print("7. ANÁLISIS DE DATOS")
# print("Edad promedio:", df['Age'].mean())
# print("Salario más alto:", df['Salary'].max())
# print("Agrupando por ciudad:\n", df.groupby('City').mean())
# print("\n")

# # 8. Limpieza de datos
# print("8. LIMPIEZA DE DATOS")
# # Crear un DataFrame con algunos valores faltantes
# data_missing = {
#     'Name': ['John', 'Anna', None, 'Linda'],
#     'Age': [28, None, 29, 42],
#     'City': ['New York', 'Paris', 'Berlin', None],
#     'Salary': [65000, 70000, None, 85000]
# }
# df_missing = pd.DataFrame(data_missing)
# print("DataFrame con valores faltantes:\n", df_missing)

# # Verificando valores faltantes
# print("Conteo de valores faltantes:\n", df_missing.isnull().sum())

# # Rellenando valores faltantes
# df_filled = df_missing.fillna({'Name': 'Unknown', 'Age': df_missing['Age'].mean(), 
#                               'City': 'Unknown', 'Salary': df_missing['Salary'].mean()})
# print("DataFrame con valores rellenados:\n", df_filled)

# # Eliminando filas con valores faltantes
# df_dropped = df_missing.dropna()
# print("DataFrame con filas eliminadas:\n", df_dropped)