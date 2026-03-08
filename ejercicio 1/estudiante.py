class Estudiante:
    
    def __init__(self, nombre, edad, carrera):
       
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.calificaciones = []  
        
        def setCalificaciones(self, calificacion):
            self.calificaciones.append(calificacion)
            
        def getNombre(self):
            return self.nombre
        
    def mostrarPromedio(self):
        if len(self.calificaciones) == 0:
            return 0
        return sum(self.calificaciones) / len (self.calificaciones)
    
    
    def mostrarInformacionUsuario(self):
        return f"hola, soy {self.nombre}, tengo {self.edad} años y estudio {self.carrera}"
    
    # crear los objetos de la clase
estudiante1 = Estudiante("juan", 20, "ingenieria")
estudiante2 = Estudiante("maria", 22, "medicina")   
estudiante3 = Estudiante("pedro", 19, "arquitectura")

print(estudiante1.mostrarInformacionUsuario())
   


