from Jugador import Jugador

#Clase observador

class Observador(Jugador):
    
    print("\n======================== OBSERVADOR ==================================")  
    
    def __init__(self, nombre, num_control, nivel, puntos, partidas_vistas):
        super().__init__(nombre, num_control, nivel, puntos)
        self.partidas_vistas = 0

        
    def observar_partidas(self, competidor):
            self.puntos = +5
            self.partidas_vistas += 1   
            print(f"{self.nombre}\n ha espectado la partida de {competidor.nombre}\n Aumentó 5 puntos, ahora tiene {self.puntos} puntos.\n sus partidas vistas son: {self.partidas_vistas}")
            
    def mostrar_perfil(self):
        super().mostrar_perfil()
        print("Espectador del torneo")
        print(f"Partidas vistas: {self.partidas_vistas}")
            
    