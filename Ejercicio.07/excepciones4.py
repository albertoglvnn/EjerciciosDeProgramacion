print("=" * 50)
print("PARTE 4: Leer un archivo con manejo de errores")
print("=" * 50)

nombre = input("Nombre del archivo (.txt): ")

try:
    with open(nombre, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
    print("\n--- Contenido ---")
    print(contenido)

except FileNotFoundError:
    print(f"❌ El archivo '{nombre}' no existe.")

except PermissionError:
    print("❌ No tienes permisos para leer ese archivo.")

except Exception as e:
    print(f"❌ Error inesperado: {e}")

finally:
    print("\n✅ Intento de lectura concluido.")