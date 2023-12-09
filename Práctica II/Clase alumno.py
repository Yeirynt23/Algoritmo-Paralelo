class Estudiante:
    #contenido de la clase.
    nombre = ""
    apellidos = ""
    edad = ""
    sexo = ""
    matrícula = ""
    dirección = ""
    carrera = ""
    email = ""
    teléfono = ""

    def NombreCompleto(self, nombre, apellidos, edad, sexo, matrícula, direccion, carrera, email, teléfono): 
        return nombre +" "+ apellidos +" " + edad +" " + sexo +" " + matrícula +" " + direccion +" " + carrera +" " + email +" " + teléfono
    
alu = Estudiante()
nombre = input("Nombre..:")
apellido = input("Apellido..:")
edad = input("Edad..:")
sexo = input("Sexo..:")
direccion = input("Dirección..:")
email = input("Email..:")
teléfono = input("Teléfono..:")
carrera = input("Carrera..:")
matrícula = input("Matrícula..:")
email = input("Email..:")
teléfono = input("Teléfono..:")


print(alu.NombreCompleto(nombre, apellido, edad, sexo, matrícula, direccion, carrera, email, teléfono))
