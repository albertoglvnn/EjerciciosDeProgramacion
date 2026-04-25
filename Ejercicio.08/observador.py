from jugador import Jugador
#Clase observador
class Observador(Jugador):
    def __init__(self, nombre, num_control, nivel, puntos, partidas_vistas):
        super().__init__(nombre, num_control, nivel, puntos)
        self.partidas_vistas = 0

    def mostrar_perfil(self):
        super().mostrar_perfil()
        print("Espectador del torneo")
        print(f"Partidas vistas: {self.partidas_vistas}")
        
    def observar_partidas(self, competidor):
            print(f"{self.nombre} ha espectado la partida de {competidor.nombre}. aumenta 5 puntos, ahora tiene {self.puntos} puntos.   y sus partidas vistas son: {self.partidas_vistas}")
            self.puntos += 5
            self.partidas_vistas += 1   
            
    