#------------------------Competidor---------------------------------------------------------
from Competidor import Competidor

Competidor1 = Competidor("pepeElpollo", "125664", "19", any, "Las Chivas")

Competidor1.ganar_puntos(5)   

Competidor1.perder_puntos(6)

Competidor1.mostrar_perfil()

#------------------------Observador---------------------------------------------------------

from Observador import Observador       

Observador1 = Observador("Juanito Alcachofas", "125214", "20", any, "El America")

Observador1.observar_partidas(Competidor1)

Observador1.mostrar_perfil()

 



        