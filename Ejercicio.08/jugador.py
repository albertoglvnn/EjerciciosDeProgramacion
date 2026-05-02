#Clase base
class Jugador:
    
    def __init__(self,nombre,num_control,nivel,puntos=0):
        self.nombre = nombre
        self.num_control = num_control
        self.nivel = nivel
        self.puntos =  puntos
  

    def ganar_puntos(self, puntos_ganados):
        self.puntos = puntos_ganados
        print(f"{self.nombre} ha ganado {puntos_ganados} puntos.\n Total de puntos: {self.puntos}")
    
    def perder_puntos(self, puntos_perdidos):
        self.puntos -= puntos_perdidos
        if self.puntos < 0:
            self.puntos = 0 
        print(f"{self.nombre} ha perdido {puntos_perdidos} puntos.\n Total de puntos: {self.puntos}") 
        
    def mostrar_perfil(self):
        print(f"Nombre: {self.nombre}\n Número de Control: {self.num_control}\n Nivel: {self.nivel}\n Puntos: {self.puntos}\n")