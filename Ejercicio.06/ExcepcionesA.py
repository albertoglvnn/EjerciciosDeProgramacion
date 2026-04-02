###
## Excepciones basicas

# Parte 1: try / except simple
print("=" * 50)
print("PARTE 1: Division con manejo de errores")
print("=" * 50)

try:
    a = int(input("ingresa el numerador: "))
    b = int(input("ingresa el denominador: "))
    total = a / b

except ValueError:
    print("Error: SOLO NUMEROS, no otros simbolos.")

except ZeroDivisionError:
    print("Error: No se puede divdir por cero")

else:
    print(f"El resultado de {a} / {b} es {total}")

finally:
    print("¡Gracias por usar el programa de division!")
    
    