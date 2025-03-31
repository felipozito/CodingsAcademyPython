""" 
    Manejo de archivos texto plano
    uso open y readlines para leer archivos de texto plano
    uso writelines para escribir archivos de texto plano
    uso append para agregar contenido a un archivo de texto plano
    
"""
def leerArchivo(nombreArchivo):
    try:
        archivo = open(nombreArchivo, 'r')
        lineas = archivo.readlines()
        archivo.close()
        return lineas
    except FileNotFoundError:
        print(f"Error: El archivo '{nombreArchivo}' no fue encontrado.")
        return []
    
def escribirArchivo(nombreArchivo, txt):
    try:
        archivo = open(nombreArchivo, 'a')
        for data in txt:
            archivo.writelines(f"{data["N"]};{data["Item"]};{data["Cantidad"]}\n")
        archivo.close()
    except Exception as e:
        print(f"Error: {str(e)}")
def transformarDatos(datos):
    info=[]
    ans=[]
    titulos=datos[0].strip().strip("\ufeff").split(';')
    print(len(datos))
    for i in range(1,len(datos)):
        valores=datos[i].strip().split(';')
        ans.append(dict(zip(titulos,valores)))  
    return ans

datos=leerArchivo('Libro1.csv')
print(transformarDatos(datos))
#escribirArchivo('Libro1.csv', transformarDatos(datos))

"""
    Manejo de archivos excel
    necesitas instalar pandas para poder leer excel
    necesitamos instalar openpyxl para poder leer excel
"""
import pandas as pd


def leerExcel(nombreArchivo):
    try:
    # Read Excel file
        data = pd.read_excel(nombreArchivo)
        ##return data.to_dict('records')
        return data.values.tolist()
    except Exception as e:
        print(f"Error al leer el archivo: {str(e)}")
        return []
    
#print(leerExcel('Libro1.xlsx'))

def escribirExcel(nombreArchivo):
    try:
        # New data to append
        new_data = {
            'N': [1, 2, 3],
            'Item': ['Marker Red', 'Marker Blue', 'Marker Black'],
            'Cantidad': [10, 10, 10]
        }
        new_df = pd.DataFrame(new_data)
        try:
            # Try to read existing file
            existing_df = pd.read_excel(nombreArchivo)
            # Combine existing and new data
            combined_df = pd.concat([existing_df, new_df], ignore_index=True)
        except FileNotFoundError:
            # If file doesn't exist, use only new data
            combined_df = new_df
        # Write back to Excel
        combined_df.to_excel(nombreArchivo, index=False)
        print("Data appended successfully")
    except Exception as e:
        print(f"Error writing to Excel file: {str(e)}")

# Example usage
escribirExcel('Libro1.csv')


