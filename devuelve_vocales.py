print()
print()

frase_usuario = input("Escribe aqui tu texto: ").upper()

vocales = ["A", "E", "I", "O", "U"]

vocales_en_frase = []

for letter in frase_usuario:
    for item in vocales:
        if item == letter:
            vocales_en_frase.append(letter)

print("Estas son las vocales que aparecen: {}".format(vocales_en_frase))
