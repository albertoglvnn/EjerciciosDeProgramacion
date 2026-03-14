from Aventurero import Aventurero

class Arquero(Aventurero):
    
    print("\n======================== ARQUERO ==================================")
     
    def __init__(self, nombre, nivel, int, flechas):
        super().__init__(nombre, nivel)
        self.int = int
        self.flechas = flechas  
        
    def usar_habilidad(self):
        super().usar_habilidad()
        self.flechas -= 1
        print(f"{self.nombre} dispara una flecha con su arco, le quedan {self.flechas} flechas!")
        
        