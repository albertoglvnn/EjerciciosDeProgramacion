from Platillo import Platillo

class Postre(Platillo):
    
    def __init__(self, nombre, precio, es_sin_gluten):
        super().__init__(nombre, precio)
        self.es_sin_gluten = es_sin_gluten  

    def mostrar_informacion(self):
        super().mostrar_informacion()
    
    def tipo(self): 
        if self.es_sin_gluten:
           print("Este postre si tiene gluten")
           
        else:
            print("Este postre no tiene gluten")
            
    
        