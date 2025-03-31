"""A todos los archivos creado añada registros, actualice registros y eliminine registros. 
"""
def readData(archivos):
    archivo=open(archivos,'r')
    data=archivo.read()
    print(data)
    archivo.close()
def write(archivos):
    archivo=open(archivos,'w')
    archivo.write("Escribo")
    archivo.close()

def update(archivos):
    archivo=open(archivos,'a')
    archivo.write("Hola mundo")
    archivo.close()
def delete(archivos):
    archivo=open(archivos,'r+')
    archivo.truncate()
    archivo.close()

def main():
    readData("test.json")
    write("test.json")
    readData("test.json")
    update("test.json")
    readData("test.json")
    delete("test.json")
    
if __name__=='__main__':
    main()  
