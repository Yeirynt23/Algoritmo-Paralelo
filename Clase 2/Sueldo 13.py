numero =1
suerdo =0
total =0
sueldo13 = int

while numero <=12:
    sueldo = int(input("Entre sueldo :"))

    total = total + sueldo
    
    numero = numero + 1
sueldo13 = total/12
print ("Total de sueldos:", total)
print ("Total de sueldo 13 :", sueldo13)