from Aventurero import Aventurero

class Mago(Aventurero):
   
    print("\n======================== MAGO ==================================")
    
    def __init__(self, nombre, nivel, hechizo):
        super().__init__(nombre, nivel)
        self.hechizo = hechizo
    
    def usar_habilidad(self):
        super().usar_habilidad()
        print(f"{self.nombre} imboca el hechizo {self.hechizo}!")
        
    