class Persona:
    def __init__(self, nombre='', apellidos='', edad=0, sexo='', direccion='', correo='', sueldo=0.0):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.sexo = sexo
        self.direccion = direccion
        self.correo = correo
        self.sueldo = sueldo

    def ingresar_datos(self):
        self.nombre = input("Ingrese el nombre: ")
        self.apellidos = input("Ingrese los apellidos: ")
        self.edad = int(input("Ingrese la edad: "))
        self.sexo = input("Ingrese el sexo: ")
        self.direccion = input("Ingrese la dirección: ")
        self.correo = input("Ingrese el correo electrónico: ")
        self.sueldo = float(input("Ingrese el sueldo: "))

    def AsignarSueldo(self, sueldo):
        self.sueldo = sueldo

    def CalcularAfp(self):
        afp = 0.0287 * self.sueldo
        return afp

    def CalcularSfs(self):
        sfs =0.0304 * self.sueldo
        return sfs

    def CalcularIsr(self):
        # Deducciones de TSS
        sfs = self.sueldo * 0.0304
        afp = self.sueldo * 0.0287
        total_deducciones = sfs + afp

        # Base Imponible
        base_imponible = self.sueldo - total_deducciones

        # Multiplicar por 12 meses
        base_anual = base_imponible * 12

        # Verificar en qué rango cae
        if base_anual <= 416220.00:
            impuesto_mensual= 0
        elif 416220.00 < base_anual <= 624329.00:
            excedente = base_anual - 416220.00
            impuesto_anual = excedente * 0.15
            impuesto_mensual = impuesto_anual / 12
        elif 624329.00 < base_anual <= 867123.00:
            excedente = base_anual - 624329.00
            impuesto_anual = excedente * 0.20 + 31216.00  # Sumar el monto fijo adicional
            impuesto_mensual = impuesto_anual / 12
        elif base_anual > 867123.00:
            excedente = base_anual - 867123.00
            impuesto_anual = excedente * 0.25 + 6516.00
            impuesto_mensual = impuesto_anual / 12
        else:
            impuesto_mensual = 0

        return impuesto_mensual

    
    def imprimir_informacion(self):
        print("Información de la persona:")
        print(f"Nombre: {self.nombre}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Edad: {self.edad}")
        print(f"Sexo: {self.sexo}")
        print(f"Dirección: {self.direccion}")
        print(f"Correo: {self.correo}")
        print(f"Sueldo: {self.sueldo}")
        print(f"AFP: {self.CalcularAfp()}")
        print(f"SFS: {self.CalcularSfs()}")
        print(f"ISR: {self.CalcularIsr()}")


persona1 = Persona()
persona1.ingresar_datos()
persona1.imprimir_informacion()