# Excepciones basicas

# parte 1: try / except simple
print("=" * 50)
print("PARTE 1: Division con manejo de errores")
print("=" * 50)

try:
    a = int(input("Ingresa el numerador: "))
    b = int(input("Ingresa el denominador: "))
    total = a / b

except ValueError:
    print("Error: Solo numeros.")

except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")

else:
    print(f"El resultado de {a} / {b} es: {total}")

finally:
    print("Fin del programa.")