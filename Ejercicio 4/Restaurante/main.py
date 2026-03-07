from Comida import Comida

chile_relleno = Comida("Chile Relleno", 150.00, "Mexicana")
chile_relleno.mostrar_informacion()
chile_relleno.tipo()

from Postre import Postre

chocoflan = Postre("Chocoflan", 80.00,False)
chocoflan.mostrar_informacion() 
chocoflan.tipo()

from Aperitivos import Aperitivo

guacamole = Aperitivo("Guacamole", 60.00, "Grande")
guacamole.mostrar_informacion()     


