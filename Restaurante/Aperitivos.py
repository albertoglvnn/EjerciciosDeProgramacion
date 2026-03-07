from Platillo import Platillo

class Aperitivo (Platillo):
    def __init__(self,nombre,precio,tamaño):
        super().__init__(nombre,precio)
        self.tamaño = tamaño
        