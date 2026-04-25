#Clase base
class Jugador:
    
    def __init__(self,nombre,num_control,nivel,puntos):
        self.nombre = nombre
        self.num_control = num_control
        self.nivel = nivel
        self.puntos = puntos
  

    def ganar_puntos(self, puntos_ganados):
        self.puntos += puntos_ganados
        print(f"{self.nombre} ha ganado {puntos_ganados} puntos. Total de puntos: {self.puntos}")
    
    def perder_puntos(self, puntos_perdidos):
        self.puntos -= puntos_perdidos
        print(f"{self.nombre} ha perdido {puntos_perdidos} puntos. Total de puntos: {self.puntos}") 
        
    def mostrar_perfil(self):
        print(f"Nombre: {self.nombre}, Número de Control: {self.num_control}, Nivel: {self.nivel}, Puntos: {self.puntos}")