# Excepciones basicas

# parte 2: try / Capturar multiples excepciones
print("=" * 50)
print("PARTE 2: Acceso a una lista")
print("=" * 50)

# Creamos una lista de ejemplo
colores = ["rojo", "verde", "azul", "amarillo"]
print(f"Lista de colores: {colores} (indices 0,1,2,3)")
try:
    indice = int(input("Que color quieres acceder? (0-3): " ))
    print(f"El color seleccionado es: {colores[indice]}")

except ValueError as e:
    print(f"✖️ ValueError: {e}")

except IndexError as e:
    print(f"✖️ IndexError: {e}")
    print(f"Solo puedes usar los numeros 0 al 3 para acceder a los colores.")

finally:
    print("-- Fin del programa. --")