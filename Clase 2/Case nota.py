nota = int(input("DIGITE SU NOTA"))

match nota: 
    case _ if nota >=90:
           print("A")
        
    case _ if nota >=80:
           print("B")

    case _ if nota >=70:
           print("C")

    case _ if nota >=60:
           print("D")
    case _:
        print("Selecionar una opción validad")

        