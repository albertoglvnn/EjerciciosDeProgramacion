#clase Base
class Animal:
    #Contructor
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def describir(self):
        print(f"Soy {self.nombre} y tengo {self.edad} años.")
        
def hablar(self):
    print("...")
#------------------------------------------------------------    
#clase derivada
#------------------------------------------------------------

class Perro(Animal):
    
    def hablar(self):
        print(f"{self.nombre}: Guau!")
        
#------------------------------------------------------------
#clase derivada 2
#------------------------------------------------------------
        
class Gato(Animal):
    
    def hablar(self):
        print(f"{self.nombre}: Miau!")  
        
#------------------------------------------------------------
#crear las instancias
#------------------------------------------------------------

pakito = Perro("Pakito", 3)
miauricio = Gato("Miauricio", 2)

#------------------------------------------------------------
#usar las instancias
#------------------------------------------------------------

pakito.hablar()
miauricio.hablar()




    
    



    
    
        
        
    