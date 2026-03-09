class Aventurero:
    
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel  
        
    def presentarse(self):
        
     print(f"\n Hola, soy {self.nombre} un {self.__class__.__name__} con nivel {self.nivel}.")
    
    def usar_habilidad(self):
        return "Habilidad desconocida." 
 

    

    