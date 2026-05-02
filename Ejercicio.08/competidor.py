from Jugador import Jugador 

#Clase derivada
class Competidor(Jugador):
    
    print("\n======================== COMPETIDOR ==================================")
    
    def __init__(self, nombre, num_control, nivel, puntos,equipo):
        super().__init__(nombre, num_control, nivel, puntos)
        self.equipo = equipo
    
    def equipo(self, equipo):
        self.equipo = equipo
        print(f"{self.nombre} pertenece al equipo {self.equipo}.")
        
    def mostrar_perfil(self):
        super().mostrar_perfil()
        print(f"Equipo: {self.equipo}")
        print("Competidor en el torneo")    