Palabras = ["Escuela", "País", "Ciudad", "Hospital", "Avión",]
C = 0
for Palabra in Palabras:
    C += Palabra.count('a')

print("Número de veces que aparece 'a':")
print(C)