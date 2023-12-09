class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, saldo=0.0):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Se depositaron {cantidad} unidades. Nuevo saldo: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Se retiraron {cantidad} unidades. Nuevo saldo: {self.saldo}")
        else:
            print("La cantidad a retirar no es válida o excede el saldo disponible.")

    def calcular_interes(self, tasa_interes):
        interes = self.saldo * (tasa_interes / 100)
        self.saldo += interes
        print(f"Se aplicó un interés del {tasa_interes}%. Nuevo saldo: {self.saldo}")

    def imprimir_informacion(self):
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Titular: {self.titular}")
        print(f"Saldo actual: {self.saldo}")


numero_cuenta = input("Ingrese el número de cuenta: ")
titular = input("Ingrese el nombre del titular: ")
saldo_inicial = float(input("Ingrese el saldo inicial: "))

cuenta = CuentaBancaria(numero_cuenta=numero_cuenta, titular=titular, saldo=saldo_inicial)

cuenta.depositar(float(input("Ingrese la cantidad a depositar: ")))
cuenta.retirar(float(input("Ingrese la cantidad a retirar: ")))
cuenta.calcular_interes(float(input("Ingrese la tasa de interés a aplicar: ")))
cuenta.imprimir_informacion()