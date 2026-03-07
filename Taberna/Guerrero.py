from Aventurero import Aventurero   

class Guerrero(Aventurero):
    
    print("\n======================== GUERRERO ==================================")
    
    def __init__(self, nombre, nivel, arma):
        super().__init__(nombre, nivel)
        self.arma = arma

    def usar_habilidad(self):
        super().usar_habilidad()
        print(f"{self.nombre} ataca con su {self.arma}!")
        
        