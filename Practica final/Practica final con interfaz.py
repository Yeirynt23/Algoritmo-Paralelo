import tkinter as tk
from tkinter import simpledialog, messagebox

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
        self.cliente_autenticado = None

    def validar_usuario(self, numero_cuenta, contrasena):
        for cliente in self.clientes:
            if cliente.numero_cuenta == numero_cuenta and cliente.contrasena == contrasena:
                self.cliente_autenticado = cliente
                return True
        return False

    def mostrar_menu(self):
        return (
            "¿Qué desea hacer?\n"
            "1. Retirar efectivo\n"
            "2. Ingresar efectivo\n"
            "3. Pagar factura\n"
            "    a. Pago de préstamo\n"
            "    b. Factura de tarjeta de crédito\n"
            "4. Transferir fondos"
        )

    def ejecutar_operacion(self, opcion, cantidad=None, info_adicional=None):
        if opcion == 1:
            self.retirar_efectivo(cantidad)
        elif opcion == 2:
            self.ingresar_efectivo(cantidad)
        elif opcion == 3:
            if info_adicional == 'a':
                self.pagar_factura("Pago de Préstamo")
            elif info_adicional == 'b':
                self.pagar_factura("Tarjeta de Crédito")
            else:
                messagebox.showinfo("Error", "Subopción de factura no válida.")
        elif opcion == 4:
            self.transferir_fondos(info_adicional, cantidad)
        else:
            messagebox.showinfo("Error", "Opción no válida.")

    def retirar_efectivo(self, cantidad):
        if self.cliente_autenticado.saldo >= cantidad:
            self.cliente_autenticado.saldo -= cantidad
            messagebox.showinfo("Retiro Exitoso", f"Se retiraron {cantidad} de la cuenta de {self.cliente_autenticado.nombre}. Saldo restante: {self.cliente_autenticado.saldo}")
        else:
            messagebox.showinfo("Error", "Saldo insuficiente.")

    def ingresar_efectivo(self, cantidad):
        self.cliente_autenticado.saldo += cantidad
        messagebox.showinfo("Ingreso Exitoso", f"Se ingresaron {cantidad} a la cuenta de {self.cliente_autenticado.nombre}. Nuevo saldo: {self.cliente_autenticado.saldo}")

    def obtener_cuenta_cliente(self, numero_cuenta):
        for cliente in self.clientes:
            if cliente.numero_cuenta == numero_cuenta:
                return Cuenta(numero_cuenta, 0, 0, "Corriente")

    def pagar_factura(self, info_factura):
        if self.cliente_autenticado is not None:
            messagebox.showinfo("Pago Exitoso", f"Se pagó la factura {info_factura} desde la cuenta {self.cliente_autenticado.numero_cuenta}.")
        else:
            messagebox.showinfo("Error", "No se proporcionó una cuenta válida.")

    def transferir_fondos(self, info_cuenta_destino, cantidad):
        messagebox.showinfo("Transferencia Exitosa", f"Se transfirieron {cantidad} desde la cuenta {self.cliente_autenticado.numero_cuenta} a {info_cuenta_destino}.")

class CajeroGUI:

    def __init__(self, root, cajero_automatico):
        self.root = root
        self.cajero_automatico = cajero_automatico

        self.root.title("Cajero Automático")
        self.root.geometry("400x300")

        self.label_numero_cuenta = tk.Label(root, text="Número de Cuenta:")
        self.label_numero_cuenta.pack()

        self.entry_numero_cuenta = tk.Entry(root)
        self.entry_numero_cuenta.pack()

        self.label_contrasena = tk.Label(root, text="Contraseña:")
        self.label_contrasena.pack()

        self.entry_contrasena = tk.Entry(root, show="*")
        self.entry_contrasena.pack()

        self.button_ingresar = tk.Button(root, text="Ingresar", command=self.validar_usuario)
        self.button_ingresar.pack()

        self.menu_label = tk.Label(root, text="")
        self.menu_label.pack()

    def validar_usuario(self):
        numero_cuenta = self.entry_numero_cuenta.get()
        contrasena = self.entry_contrasena.get()

        if self.cajero_automatico.validar_usuario(numero_cuenta, contrasena):
            self.mostrar_menu()
        else:
            messagebox.showinfo("Error", "Usuario o contraseña incorrectos.")

    def mostrar_menu(self):
        menu_text = self.cajero_automatico.mostrar_menu()
        self.menu_label.config(text=menu_text)

        opcion = simpledialog.askinteger("Menú", "Seleccione una opción")
        if opcion:
            if opcion in range(1, 5):
                if opcion == 3:
                    subopcion = simpledialog.askstring("Pago de Factura", "Seleccione el tipo de factura:\na. Pago de préstamo\nb. Factura de tarjeta de crédito")
                    self.cajero_automatico.ejecutar_operacion(opcion, info_adicional=subopcion)
                elif opcion == 4:
                    info_cuenta_destino = simpledialog.askstring("Transferencia de Fondos", "Ingrese la información de la cuenta destino:")
                    cantidad = simpledialog.askfloat("Transferencia de Fondos", "Ingrese la cantidad que desea transferir:")
                    self.cajero_automatico.ejecutar_operacion(opcion, cantidad=cantidad, info_adicional=info_cuenta_destino)
                else:
                    cantidad = simpledialog.askfloat("Operación", "Ingrese la cantidad:")
                    self.cajero_automatico.ejecutar_operacion(opcion, cantidad=cantidad)
            else:
                messagebox.showinfo("Error", "Opción no válida.")

if __name__ == "__main__":
    cliente1 = Cliente("Jerry Núñez", "Jicomé Abajo", "4585548615493128", 50000, "1234")
    cliente2 = Cliente("Melvis Taveras", "Francisco Arias", "8549317594261895", 300000, "4567")
    cliente3 = Cliente("Evelina Luciano", "Esperanza", "25439 415823154951", 500000, "7891")

    banco = Banco("Banco Principal")
    clientes = [cliente1, cliente2, cliente3]
    cajero_automatico = CajeroAutomatico(banco, clientes)

    root = tk.Tk()
    cajero_gui = CajeroGUI(root, cajero_automatico)
    root.mainloop()


