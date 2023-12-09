class persona:

  #contenido de la clase.
    nombre = ""
    apellidos = ""
    edad = ""
    sexo = ""
    dirección = ""

    def ClasePersona( selt , nombre, apellidos, edad, sexo, direccion):
        return nombre +" "+ apellidos +" " + edad +" " + sexo +" " + direccion

Persona = persona()
nombre=input("Nombre...:")
apellidos=input("Apellido...:")
edad=input("Edad....:")
sexo=input("Sexo...:")
direccion=input("Direccion....:")

print(" Informacion de la persona:...", Persona.ClasePersona(nombre, apellidos, edad, sexo, direccion))