class Banco:
    def __init__(self, nombre):
        self.nombre = nombre

class Cuenta:
    def __init__(self, numero_cuenta, saldo, limite_credito, tipo_cuenta):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.limite_credito = limite_credito
        self.tipo_cuenta = tipo_cuenta

class Cliente:
    def __init__(self, nombre, direccion, numero_cuenta, saldo, contrasena):
        self.nombre = nombre
        self.direccion = direccion
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.contrasena = contrasena  

class Cajero:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

class CajeroAutomatico:

    def __init__(self, banco, clientes):
        self.banco = banco
        self.clientes = clientes

    def validar_usuario(self, numero_cuenta, contrasena):
        for cliente in self.clientes:
            if cliente.numero_cuenta == numero_cuenta and cliente.contrasena == contrasena:
                self.cliente_autenticado = cliente
                return True
        return False

    def mostrar_menu(self):
        print("¿Qué desea hacer?")
        print("1. Retirar efectivo")
        print("2. Ingresar efectivo")
        print("3. Pagar factura")
        print("    a. Factura de servicios públicos")
        print("    b. Factura de tarjeta de crédito")
        print("4. Transferir fondos")


    def ejecutar_operacion(self, opcion, cliente, cantidad, info_adicional=None):
        if opcion == 1:
            self.retirar_efectivo(cliente, cantidad)
        elif opcion == 2:
            self.ingresar_efectivo(cliente, cantidad)
        elif opcion == 3:
            if info_adicional == 'a':
                self.pagar_factura(cliente, "Pago de Préstamo")
            elif info_adicional == 'b':
                self.pagar_factura(cliente, "Tarjeta de Crédito")
            else:
                print("Subopción de factura no válida.")
        elif opcion == 4:
            self.transferir_fondos(cliente, info_adicional, cantidad)
        else:
            print("Opción no válida.")


    def retirar_efectivo(self, cliente, cantidad):
        if cliente.saldo >= cantidad:
            cliente.saldo -= cantidad
            print(f"Se retiraron {cantidad} de la cuenta de {cliente.nombre}. Saldo restante: {cliente.saldo}")
        else:
            print("Saldo insuficiente.")

    def ingresar_efectivo(self, cliente, cantidad):
        cliente.saldo += cantidad
        print(f"Se ingresaron {cantidad} a la cuenta de {cliente.nombre}. Nuevo saldo: {cliente.saldo}")

    def obtener_cuenta_cliente(self, numero_cuenta):
        for cliente in self.clientes:
            if cliente.numero_cuenta == numero_cuenta:
                # Supongamos que cada cliente tiene solo una cuenta
                return Cuenta(numero_cuenta, 0, 0, "Corriente")  # Puedes ajustar los valores iniciales según sea necesario


    def pagar_factura(self, cuenta, info_factura):
        print(f"Se pagó la factura {info_factura} desde la cuenta {cuenta.numero_cuenta}.")

    def transferir_fondos(self, cuenta_origen, info_cuenta_destino, cantidad):
        # Lógica de transferencia de fondos
        print(f"Se transfirieron {cantidad} desde la cuenta {cuenta_origen.numero_cuenta} a {info_cuenta_destino}.")

# Creación de instancias con contraseñas
cliente1 = Cliente("Jerry Núñez", "Jicomé Abajo", "4585548615493128", 50000, "1234")
cliente2 = Cliente("Melvis Taveras", "Francisco Arias", "8549317594261895", 300000, "4567")
cliente3 = Cliente("Evelina Luciano", "Esperanza", "25439415823154951", 500000, "7891")

# Creación de instancia de CajeroAutomatico
banco = Banco("Banco Principal")
clientes = [cliente1, cliente2, cliente3]
cajero_automatico = CajeroAutomatico(banco, clientes)

# Solicitud
numero_cuenta = input("Ingrese el número de cuenta: ")
contrasena = input("Ingrese la contraseña: ")

# Validar
cliente_autenticado = None
for cliente in clientes:
    if cliente.numero_cuenta == numero_cuenta:
        cliente_autenticado = cliente
        break

if cliente_autenticado and cajero_automatico.validar_usuario(numero_cuenta, contrasena):
    print(f"Usuario autenticado como {cliente_autenticado.nombre}.")
    cajero_automatico.mostrar_menu()

    opcion = int(input("Ingrese el número de la operación que desea realizar: "))

    if opcion in range(1, 5):
        if opcion == 3:
         print("Seleccione el tipo de factura:")
         print("a. Pago de préstamo")
         print("b. Factura de tarjeta de crédito")
         subopcion = input("Ingrese la letra correspondiente: ")
         cajero_automatico.ejecutar_operacion(opcion, cliente_autenticado, None, subopcion)
        elif opcion == 4:
            info_cuenta_destino = input("Ingrese la información de la cuenta destino: ")
            cantidad = float(input("Ingrese la cantidad que desea transferir: "))
            cajero_automatico.ejecutar_operacion(opcion, cliente_autenticado, cantidad, info_cuenta_destino)
        else:
            cantidad = float(input("Ingrese la cantidad: "))
            cajero_automatico.ejecutar_operacion(opcion, cliente_autenticado, cantidad)
else:
    print("Usuario o contraseña incorrectos.")
