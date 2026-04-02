###
## Excepciones basicas 

# Parte 2: try / except simple
print("=" * 50)
print("PARTE 2: Division con manejo de errores")
print("=" * 50)

# Creamos una lista de ejemplo
colores= ["rojo", "verde", "azul", "amarillo"]
print(f"Lista de colores: {colores} (indices 0,1,2,3)")

try:
    indice= int(input("Que color quieres acceder? (0-3):"))
    print(f"El color seleccionado es: {colores[indice]}")

except ValueError as e:
    print(f"🚩 ValueError: {e} ")

except IndexError as e:
    print(f"🚩IndexError: ´{e} ")
    print(f"Solo puedes usar los numeros del 0 al 3 para acceder")

finally:
    print("Gracias por usar el programa") 
    

