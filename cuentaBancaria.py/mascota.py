class Mascota:
    def __init__(self, nombre, edad, especie, felicidad):
        
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.felicidad = felicidad

    def alimentar(self, cantidad):
        if self.felicidad + cantidad > 100:
            self.felicidad = 100
        else:
            self.felicidad += cantidad

    def jugar(self, cantidad):
        if self.felicidad + cantidad > 100:
            self.felicidad = 100
        else:
            self.felicidad += cantidad

    def mostrarEstado(self):
        return f"{self.nombre} - Felicidad: {self.felicidad}"

    def consultarInformacion(self):
        return f"{self.nombre}, Su especie es:  {self.especie}, y su edad es: {self.edad} años, su felicidad es: {self.felicidad}"
    def esFeliz(self):
        return self.felicidad >= 75
    
#crear una mascota
mascota1 = Mascota("Pako", 4, "perro", 50)
mascota2 = Mascota("Mia", 3, "gato", 80)
mascota1.alimentar(20) #alimentamos a pako con 20 unidades de comida    
mascota2.jugar(10) #mia juega y su animo aumenta en 10



print(mascota1.consultarInformacion()) #mostramos la información de pako
print(f"{mascota1.nombre} tiene {mascota1.edad} años y es un {mascota1.especie}. Su felicidad es de {mascota1.felicidad}.")

print(mascota2.consultarInformacion()) #mostramos la información de mia
    