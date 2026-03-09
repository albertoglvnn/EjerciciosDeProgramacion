from Platillo import Platillo
class Bebida (Platillo):
    def __init__(self, nombre, precio, temperatura):
        super().__init__(nombre, precio)
        self.temperatura = temperatura  

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Tipo de bebida: {self.tipo}")
    
   