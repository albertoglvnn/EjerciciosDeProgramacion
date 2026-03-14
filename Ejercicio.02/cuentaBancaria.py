class CuentaBancaria:
#constructor
    def __init__(self, titular, numeroCuenta, saldo):
        self.titular = titular
        self.numeroCuenta = numeroCuenta
        self.saldo = saldo
#metodo para depositar dinero

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, retiro):
        if retiro > self.saldo:
            return "Fondos insuficientes"
        else:
            self.saldo -= retiro
            return f"Has retirado {retiro}. Tu nuevo saldo es: {self.saldo}"

    def consultarSaldo(self):
        return f"Tu saldo actual es: {self.saldo} pesos"
#mostrar información de la cuenta

    def mostrarInformacion(self):
        return f"{self.titular} tienes {self.saldo} pesos en tu cuenta."   
    
cuenta1 = CuentaBancaria("julian", "1236652", 20986.0)
cuenta1.depositar(500.0)
cuenta1.retirar(200.0)
print(cuenta1.consultarSaldo())     

print(cuenta1.mostrarInformacion())
