print("=" * 50)
print("PARTE 6: Registro de calificaciones")
print("=" * 50)

class CalificacionFueraDeRangoError(Exception):
    def __init__(self, calificacion):
        super().__init__(f"Calificación inválida: {calificacion}. Debe estar entre 0 y 100.")
        self.calificacion = calificacion


# --- Función para pedir enteros ---
def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("⚠️ Solo se aceptan números enteros.\n")


# --- Función de validación ---
def validar_calificacion(calificacion):
    if not (0 <= calificacion <= 100):
        raise CalificacionFueraDeRangoError(calificacion)
    return calificacion


# --- Programa principal ---
while True:
    nombre = input("Nombre del estudiante (o 'salir'): ")
    
    if nombre.lower() == "salir":
        break

    try:
        calificacion = pedir_entero("Calificación (0-100): ")
        validar_calificacion(calificacion)

        print(f"✅ {nombre} registrado con calificación {calificacion}\n")

    except CalificacionFueraDeRangoError as e:
        print(f"❌ {e}\n")