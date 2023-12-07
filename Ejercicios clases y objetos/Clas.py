class Alumno:
    #contenido de la clase.
    nombre = ""
    apellido = ""
    edad = ""
    matrícula = ""
    carrera = ""
    dirección = ""
    teléfono = ""

    def NombreCompleto(self, nombre, apellido): 
        return nombre +" "+ apellido
    
alu = Alumno()
nombre = input("Nombre..:")
apellido = input("Apellido..:")

print(alu.NombreCompleto(nombre, apellido))