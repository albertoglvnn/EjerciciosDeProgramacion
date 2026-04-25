print("PARTE 5: Excepciones personalizadas con clases")
print("=" * 50)

class EdadInvalidaError(Exception):
    def __init__(self, edad):
        super().__init__(f"Edad inválida: {edad}. Debe estar entre 0 y 120.")
        self.edad = edad


class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, monto):
        super().__init__(f"Saldo insuficiente. Tienes ${saldo}, necesitas ${monto}.")
        self.saldo = saldo
        self.monto = monto


# --- Funciones ---

def registrar_edad(edad):
    if not (0 <= edad <= 120):
        raise EdadInvalidaError(edad)
    return f"Edad {edad} registrada correctamente."


def retirar(saldo, monto):
    if monto > saldo:
        raise SaldoInsuficienteError(saldo, monto)
    return saldo - monto


# --- Validación de edad ---
while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        print(registrar_edad(edad))
        break
    except EdadInvalidaError as e:
        print(f"❌ {e}")
        print("🔁 Intenta de nuevo.\n")
    except ValueError:
        print("❌ Debes ingresar un número válido.\n")


# --- Validación de retiro ---
saldo = float(input("\nIngresa tu saldo: "))

while True:
    try:
        monto = float(input("Monto a retirar: "))
        saldo = retirar(saldo, monto)
        print(f"✅ Retiro exitoso. Nuevo saldo: ${saldo}")
        break
    except SaldoInsuficienteError as e:
        print(f"❌ {e}")
        print(f"   Te faltan ${e.monto - e.saldo}")
        print("🔁 Intenta con otro monto.\n")
    except ValueError:
        print("❌ Ingresa una cantidad válida.\n")

print("✅ Operación finalizada")