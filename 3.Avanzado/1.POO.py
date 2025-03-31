class Pikachu():
    # Atributos de Clase
    tipo='Electrico'
    #Atributos de Instancia
    def __init__(self,nombre,ataque,defensa,vida,voltaje,amperaje):
        self.nombre=nombre
        self.__ataque=ataque
        self.__defensa=defensa
        self.__voltaje=voltaje
        self.__amperaje=amperaje
        self.__vida=vida
    # ? Forma Generica    
    def get_ataque(self):
        return self.__ataque
    def set_ataque(self,ataque):
        self.__ataque=(ataque if ataque >= 0 else self.__ataque)
    def get_defensa(self):
        return self.__defensa
    def set_defensa(self,defensa):
        self.__defensa=defensa
    def get_voltaje(self):
        return self.__voltaje
    def set_voltaje(self,voltaje):
        self.__voltaje=voltaje
    def get_amperaje(self):
        return self.__amperaje
    def set_amperaje(self,amperaje):
        self.__amperaje=amperaje
        
    # ? Forma Pythonica    
    @property    
    def vida(self):
        return self.__vida
    @vida.setter
    def vida(self,vida):
        self.__vida=(vida if vida >= 0 else self.__vida)
        
    
    #Metodos
    def atacar(self):
        power=self.__ataque/10
        print(f'el pokemon {self.nombre} esta atacando con {power} de poder')
    
        
        
pikachu1=Pikachu('Pika',100,100,5,10,5)
pikachu2=Pikachu('Pika',10,20,10,10,5)

print(f'el nombre del pokemon es {pikachu2.nombre} el ataque es {pikachu2.get_ataque()} la defensa es {pikachu2.get_defensa()} y la vida es {pikachu2.vida}')
pikachu1.atacar()
print("Entrenando un tiempo ,,,,,,,,,,")
#* Encapsulamiento en Python todo es publico
#Buenas practicas un guion bajo antes de un atributo o metodo privado para que no se pueda acceder desde fuera de la clase
#Doble Guion Bajo antes de un atributo o metodo para que no se pueda acceder desde fuera de la clase oculta para el uso SIMULADO
#* Forma Generica
pikachu1.set_ataque(500)
pikachu1.atacar()
#* Getters y Setters en Python
#* Getters: Son metodos que nos permiten obtener el valor de un atributo
#* Setters: Son metodos que nos permiten modificar el valor de un atributo
#* Para crear un getter usamos la palabra reservada @property
pikachu1.vida=2
print(pikachu1.vida)

##* Herencia
class pokemon():
    def __init__(self,nombre,ataque,defensa,vida):
        self.nombre=nombre
        self.__ataque=ataque
        self.__defensa=defensa
        self.__vida=vida
    
class pikachus(pokemon):
    def __init__(self,nombre,ataque,defensa,vida,voltaje,amperaje):
        super().__init__(nombre,ataque,defensa,vida)
        self.nombre=nombre
        self.__ataque=ataque
        self.__defensa=defensa
        self.__vida=vida
        self.__voltaje=voltaje
        self.__amperaje=amperaje
    def atacar(self):
        power=self.__ataque/10
        print(f'el pokemon {self.nombre} esta atacando con {power} de poder')        

pikachu1=pikachus('Pika',100,100,5,10,5)
pikachu1.atacar()
print(pikachu1.nombre)
print(pikachu1._pokemon__ataque)