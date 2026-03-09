from Platillo import Platillo

class Comida(Platillo):
    
    def __init__(self, nombre, precio, categoria):
        super().__init__(nombre, precio)
        self.categoria = categoria

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Tipo de comida: {self.categoria}")

    def tipo(self):
        return f"Comida del tipo: {self.categoria}"

